'use strict';

/* ============================================================
   GAME LOGIC
   Pure-ish functions operating on a plain board array.
   Board: 8x8 array, board[row][col] is either null or
   { player: 1 | 2, king: boolean }.
   Row 0 = top (Player 2's home area), row 7 = bottom (Player 1's home area).
   Dark (playable) squares are where (row + col) % 2 === 1.
   ============================================================ */

const BOARD_SIZE = 8;

function isDarkSquare(row, col) {
  return (row + col) % 2 === 1;
}

function inBounds(row, col) {
  return row >= 0 && row < BOARD_SIZE && col >= 0 && col < BOARD_SIZE;
}

function homeRowFor(player) {
  return player === 1 ? 7 : 0;
}

function kingRowFor(player) {
  // The row a chip must reach to be crowned (opponent's home row).
  return player === 1 ? 0 : 7;
}

function opponentOf(player) {
  return player === 1 ? 2 : 1;
}

function createInitialBoard() {
  const board = Array.from({ length: BOARD_SIZE }, () => Array(BOARD_SIZE).fill(null));

  // Player 1 (bottom): rows 6 and 7, dark squares only.
  for (const row of [6, 7]) {
    for (let col = 0; col < BOARD_SIZE; col++) {
      if (isDarkSquare(row, col)) {
        board[row][col] = { player: 1, king: false };
      }
    }
  }

  // Player 2 (top): rows 0 and 1, dark squares only.
  for (const row of [0, 1]) {
    for (let col = 0; col < BOARD_SIZE; col++) {
      if (isDarkSquare(row, col)) {
        board[row][col] = { player: 2, king: false };
      }
    }
  }

  return board;
}

function countChips(board, player) {
  let count = 0;
  for (let r = 0; r < BOARD_SIZE; r++) {
    for (let c = 0; c < BOARD_SIZE; c++) {
      const chip = board[r][c];
      if (chip && chip.player === player) count++;
    }
  }
  return count;
}

function forwardDirsFor(chip) {
  if (chip.king) return [-1, 1];
  return chip.player === 1 ? [-1] : [1];
}

// Returns { simples: [{toR,toC}], captures: [{toR,toC,capR,capC}] } for the
// chip sitting at (row, col). Does not consider whose turn it is or
// mandatory-capture rules — that's handled by getMovablePieces.
function getPieceMoves(board, row, col) {
  const chip = board[row][col];
  const simples = [];
  const captures = [];
  if (!chip) return { simples, captures };

  const rowDirs = forwardDirsFor(chip);
  const colDirs = [-1, 1];

  for (const dr of rowDirs) {
    for (const dc of colDirs) {
      const nr = row + dr;
      const nc = col + dc;
      if (!inBounds(nr, nc)) continue;
      const occupant = board[nr][nc];

      if (!occupant) {
        simples.push({ toR: nr, toC: nc });
      } else if (occupant.player !== chip.player) {
        const jr = row + dr * 2;
        const jc = col + dc * 2;
        if (inBounds(jr, jc) && !board[jr][jc]) {
          captures.push({ toR: jr, toC: jc, capR: nr, capC: nc });
        }
      }
    }
  }

  return { simples, captures };
}

// Determines which of a player's pieces may move this turn, honoring the
// mandatory-capture rule: if ANY piece has a capture available, only
// capturing pieces (and only their capture moves) are legal.
function getMovablePieces(board, player) {
  const withCaptures = [];
  const withSimples = [];

  for (let r = 0; r < BOARD_SIZE; r++) {
    for (let c = 0; c < BOARD_SIZE; c++) {
      const chip = board[r][c];
      if (!chip || chip.player !== player) continue;
      const moves = getPieceMoves(board, r, c);
      if (moves.captures.length > 0) {
        withCaptures.push({ row: r, col: c, moves: moves.captures });
      } else if (moves.simples.length > 0) {
        withSimples.push({ row: r, col: c, moves: moves.simples });
      }
    }
  }

  if (withCaptures.length > 0) {
    return { mandatory: true, pieces: withCaptures };
  }
  return { mandatory: false, pieces: withSimples };
}

function hasAnyLegalMove(board, player) {
  return getMovablePieces(board, player).pieces.length > 0;
}

// Applies a single move (simple or capture) to the board in place.
// Returns { captured: boolean, kinged: boolean }.
function applyMove(board, fromR, fromC, move) {
  const chip = board[fromR][fromC];
  board[fromR][fromC] = null;

  let captured = false;
  if (move.capR !== undefined) {
    board[move.capR][move.capC] = null;
    captured = true;
  }

  board[move.toR][move.toC] = chip;

  let kinged = false;
  if (!chip.king && move.toR === kingRowFor(chip.player)) {
    chip.king = true;
    kinged = true;
  }

  return { captured, kinged };
}

/* ------------------------------------------------------------
   REINFORCEMENT RULE
   Each player gets exactly one reinforcement wave per game, delivered to
   the dark squares of their home row (row 7 for Player 1, row 0 for
   Player 2).

   Trigger: the wave fires the moment a player has zero chips remaining
   on their home row (checked after every board mutation, regardless of
   who made the move — an opponent's capture can trigger it just as a
   player's own move can).

   Delivery: up to 4 chips are owed, but none are placed until the home
   row is entirely free of chips of EITHER color — a stray opposing chip
   (e.g. a king that wandered onto that row) blocks the whole deployment,
   not just its own square. The pending chips just wait; once the last
   occupant leaves the row (on some later turn), all of them are placed
   at once. The wave only ever fires once per player, even if the trigger
   condition becomes true again later. A player with zero chips anywhere
   on the board is already out of the game and never receives
   reinforcements.
   ------------------------------------------------------------ */
function checkAndDeployReinforcements(board, reinforcementState) {
  const newlySpawned = []; // {row, col} of chips placed this call, for spawn animation

  for (const player of [1, 2]) {
    const state = reinforcementState[player];
    if (state.triggered) continue; // wave already used - never fires again

    const chipsOnBoard = countChips(board, player);
    if (chipsOnBoard === 0) continue; // eliminated players get nothing

    const homeRow = homeRowFor(player);
    let hasChipOnHomeRow = false;
    for (let c = 0; c < BOARD_SIZE; c++) {
      const chip = board[homeRow][c];
      if (chip && chip.player === player) {
        hasChipOnHomeRow = true;
        break;
      }
    }

    if (!hasChipOnHomeRow) {
      state.triggered = true;
      state.pending = 4;
    }
  }

  // Deploy any pending reinforcements, but only once every dark square on
  // the home row is empty — a chip of either color sitting on the row
  // holds up the entire wave, not just the square it occupies.
  for (const player of [1, 2]) {
    const state = reinforcementState[player];
    if (state.pending <= 0) continue;

    const homeRow = homeRowFor(player);
    let rowFullyClear = true;
    for (let c = 0; c < BOARD_SIZE; c++) {
      if (!isDarkSquare(homeRow, c)) continue;
      if (board[homeRow][c]) {
        rowFullyClear = false;
        break;
      }
    }
    if (!rowFullyClear) continue;

    for (let c = 0; c < BOARD_SIZE; c++) {
      if (state.pending <= 0) break;
      if (!isDarkSquare(homeRow, c)) continue;

      board[homeRow][c] = { player, king: false };
      state.pending--;
      newlySpawned.push({ row: homeRow, col: c });
    }
  }

  return newlySpawned;
}

/* ============================================================
   RENDERING & INTERACTION
   (skipped when there's no DOM, e.g. running under Node for tests)
   ============================================================ */

if (typeof document !== 'undefined') {

const CROWN_SVG = `<svg class="crown" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
  <path d="M3 18h18v2H3v-2zm0-2l2-9 4.5 4L12 5l2.5 6L19 7l2 9H3z"/>
</svg>`;

const boardEl = document.getElementById('board');
const statusBarEl = document.getElementById('status-bar');
const newGameBtn = document.getElementById('new-game-btn');
const winOverlayEl = document.getElementById('win-overlay');
const winTitleEl = document.getElementById('win-title');
const rematchBtn = document.getElementById('rematch-btn');

const panelEls = {
  1: document.getElementById('panel-p1'),
  2: document.getElementById('panel-p2'),
};
const countEls = {
  1: document.getElementById('p1-count'),
  2: document.getElementById('p2-count'),
};
const reinforcementEls = {
  1: document.getElementById('p1-reinforcement'),
  2: document.getElementById('p2-reinforcement'),
};

let state = null;

function createInitialState() {
  return {
    board: createInitialBoard(),
    currentPlayer: 1,
    reinforcement: {
      1: { triggered: false, pending: 0 },
      2: { triggered: false, pending: 0 },
    },
    selected: null,       // {row, col}
    forcedPiece: null,     // {row, col} during a mandatory multi-jump
    legalDestinations: [], // moves available for the currently selected piece
    spawnCells: [],         // cells to animate as newly deployed this render
    gameOver: false,
    winner: null,
    invalidCue: null,       // {row, col} to briefly flash as invalid
  };
}

function startNewGame() {
  state = createInitialState();
  winOverlayEl.classList.add('hidden');
  render();
}

// Runs after any board mutation (a simple move, or one jump in a chain):
// deploys reinforcements, then checks win conditions for the player who is
// about to act next, unless the same player must continue a multi-jump.
function afterMutation({ continuingTurn }) {
  state.spawnCells = checkAndDeployReinforcements(state.board, state.reinforcement);

  if (continuingTurn) {
    render();
    return;
  }

  const next = opponentOf(state.currentPlayer);
  const nextChipCount = countChips(state.board, next);

  if (nextChipCount === 0) {
    endGame(state.currentPlayer);
    return;
  }

  if (!hasAnyLegalMove(state.board, next)) {
    endGame(state.currentPlayer);
    return;
  }

  state.currentPlayer = next;
  state.selected = null;
  state.forcedPiece = null;
  state.legalDestinations = [];
  render();
}

function endGame(winner) {
  state.gameOver = true;
  state.winner = winner;
  state.selected = null;
  state.forcedPiece = null;
  state.legalDestinations = [];
  render();
  winTitleEl.textContent = `Player ${winner} wins!`;
  winOverlayEl.classList.remove('hidden');
}

function selectPiece(row, col) {
  const movable = getCurrentMovablePieces();
  const piece = movable.pieces.find((p) => p.row === row && p.col === col);
  if (!piece) return;

  state.selected = { row, col };
  state.legalDestinations = piece.moves.map((m) => ({ ...m }));
  render();
}

function getCurrentMovablePieces() {
  if (state.forcedPiece) {
    const moves = getPieceMoves(state.board, state.forcedPiece.row, state.forcedPiece.col).captures;
    return { mandatory: true, pieces: [{ row: state.forcedPiece.row, col: state.forcedPiece.col, moves }] };
  }
  return getMovablePieces(state.board, state.currentPlayer);
}

function attemptMove(toRow, toCol) {
  const dest = state.legalDestinations.find((m) => m.toR === toRow && m.toC === toCol);
  if (!dest) return;

  const from = state.selected;
  const { kinged } = applyMove(state.board, from.row, from.col, dest);
  const wasCapture = dest.capR !== undefined;

  if (wasCapture && !kinged) {
    const further = getPieceMoves(state.board, dest.toR, dest.toC).captures;
    if (further.length > 0) {
      state.forcedPiece = { row: dest.toR, col: dest.toC };
      state.selected = { row: dest.toR, col: dest.toC };
      state.legalDestinations = further;
      afterMutation({ continuingTurn: true });
      return;
    }
  }

  afterMutation({ continuingTurn: false });
}

function flashInvalid(row, col) {
  state.invalidCue = { row, col };
  render();
  setTimeout(() => {
    if (state.invalidCue && state.invalidCue.row === row && state.invalidCue.col === col) {
      state.invalidCue = null;
      render();
    }
  }, 320);
}

function handleSquareClick(row, col) {
  if (state.gameOver) return;

  const chip = state.board[row][col];
  const isDestination = state.legalDestinations.some((m) => m.toR === row && m.toC === col);

  if (isDestination) {
    attemptMove(row, col);
    return;
  }

  if (chip && chip.player === state.currentPlayer) {
    const movable = getCurrentMovablePieces();
    const isMovable = movable.pieces.some((p) => p.row === row && p.col === col);
    if (isMovable) {
      selectPiece(row, col);
    } else {
      flashInvalid(row, col);
    }
    return;
  }

  if (state.selected) {
    flashInvalid(row, col);
  }
}

/* ---------------- Rendering ---------------- */

function buildBoardSkeleton() {
  boardEl.innerHTML = '';
  for (let r = 0; r < BOARD_SIZE; r++) {
    for (let c = 0; c < BOARD_SIZE; c++) {
      const square = document.createElement('div');
      square.className = `square ${isDarkSquare(r, c) ? 'dark' : 'light'}`;
      square.dataset.row = r;
      square.dataset.col = c;
      boardEl.appendChild(square);
    }
  }
}

function render() {
  const squares = boardEl.children;

  for (let r = 0; r < BOARD_SIZE; r++) {
    for (let c = 0; c < BOARD_SIZE; c++) {
      const idx = r * BOARD_SIZE + c;
      const square = squares[idx];
      square.innerHTML = '';
      square.classList.remove('destination', 'capture', 'invalid-cue', 'clickable');

      const isDest = state.legalDestinations.some((m) => m.toR === r && m.toC === c);
      if (isDest) {
        square.classList.add('destination', 'clickable');
        const dest = state.legalDestinations.find((m) => m.toR === r && m.toC === c);
        if (dest.capR !== undefined) square.classList.add('capture');
      }

      if (state.invalidCue && state.invalidCue.row === r && state.invalidCue.col === c) {
        square.classList.add('invalid-cue');
      }

      const chip = state.board[r][c];
      if (chip) {
        const chipEl = document.createElement('div');
        chipEl.className = `chip p${chip.player}`;

        const isSpawn = state.spawnCells.some((s) => s.row === r && s.col === c);
        if (isSpawn) chipEl.classList.add('spawn');

        const isSelected = state.selected && state.selected.row === r && state.selected.col === c;
        if (isSelected) chipEl.classList.add('selected');

        if (chip.king) chipEl.innerHTML = CROWN_SVG;

        const movable = getCurrentMovablePieces();
        const isClickable = !state.gameOver && chip.player === state.currentPlayer &&
          movable.pieces.some((p) => p.row === r && p.col === c);
        if (isClickable) square.classList.add('clickable');

        square.appendChild(chipEl);
      }
    }
  }

  // Clear spawn markers after this render pass so the fade-in only plays once.
  state.spawnCells = [];

  updateSidePanels();
  updateStatusBar();
}

function updateSidePanels() {
  for (const player of [1, 2]) {
    countEls[player].textContent = `${countChips(state.board, player)} chip${countChips(state.board, player) === 1 ? '' : 's'}`;

    const rState = state.reinforcement[player];
    reinforcementEls[player].textContent = rState.triggered ? 'Deployed' : 'Reinforcements ready';
    reinforcementEls[player].classList.toggle('deployed', rState.triggered);

    panelEls[player].classList.toggle('active', !state.gameOver && state.currentPlayer === player);
  }
}

function updateStatusBar() {
  if (state.gameOver) {
    statusBarEl.textContent = `Player ${state.winner} wins!`;
    return;
  }
  if (state.forcedPiece) {
    statusBarEl.textContent = `Player ${state.currentPlayer} must continue jumping`;
    return;
  }
  const movable = getCurrentMovablePieces();
  const mandatoryNote = movable.mandatory ? ' — capture available, must take it' : '';
  statusBarEl.textContent = `Player ${state.currentPlayer}'s turn${mandatoryNote}`;
}

/* ---------------- Wiring ---------------- */

boardEl.addEventListener('click', (e) => {
  const square = e.target.closest('.square');
  if (!square) return;
  handleSquareClick(Number(square.dataset.row), Number(square.dataset.col));
});

newGameBtn.addEventListener('click', startNewGame);
rematchBtn.addEventListener('click', startNewGame);

buildBoardSkeleton();
startNewGame();

} // end DOM-only section

/* ============================================================
   Exports for automated testing (Node). No effect in the browser.
   ============================================================ */
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    BOARD_SIZE,
    isDarkSquare,
    inBounds,
    homeRowFor,
    kingRowFor,
    opponentOf,
    createInitialBoard,
    countChips,
    getPieceMoves,
    getMovablePieces,
    hasAnyLegalMove,
    applyMove,
    checkAndDeployReinforcements,
  };
}
