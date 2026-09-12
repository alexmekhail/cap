import { useEffect, useState, type FormEvent } from 'react';
import { createRoot } from 'react-dom/client';
import './style.css';
type Item = { id: number; name: string; category_id: number };
type Category = { id: number; name: string };
async function read<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(path, init);
  if (!response.ok) throw new Error(`Request failed (${response.status}). Check input and server logs.`);
  return response.json() as Promise<T>;
}
function App() {
  const [items, setItems] = useState<Item[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [name, setName] = useState('');
  const [category, setCategory] = useState('');
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');
  useEffect(() => { void Promise.all([read<Item[]>('/api/items'), read<Category[]>('/api/categories')])
    .then(([i, c]) => { setItems(i); setCategories(c); setCategory(c[0] ? String(c[0].id) : ''); })
    .catch(e => setError(String(e))).finally(() => setLoading(false)); }, []);
  async function submit(event: FormEvent) {
    event.preventDefault(); setError(''); setSaving(true);
    try {
      await read<Item>('/api/items', { method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name.trim(), category_id: Number(category) }) });
      setName(''); setItems(await read<Item[]>('/api/items'));
    } catch (e) { setError(String(e)); } finally { setSaving(false); }
  }
  return <main><h1>Inventory reference</h1><p>Classroom starter · synthetic data only</p>
    {error && <p role="alert">{error}</p>}
    {loading ? <p role="status">Loading…</p> : <>
      <form onSubmit={submit}><label>Name <input value={name} onChange={e => setName(e.target.value)} maxLength={80} required /></label>
        <label>Category <select value={category} onChange={e => setCategory(e.target.value)} required>
          {categories.map(c => <option key={c.id} value={c.id}>{c.name}</option>)}
        </select></label><button disabled={saving || !name.trim() || !category}>{saving ? 'Saving…' : 'Add item'}</button></form>
      {!categories.length && <p>Run the seed command to create the reference category.</p>}
      {items.length ? <ul>{items.map(i => <li key={i.id}>{i.name}</li>)}</ul> : <p>No items yet.</p>}
      <p>Showing up to 50 items. Pagination is a student extension.</p>
    </>}
  </main>;
}
createRoot(document.getElementById('root')!).render(<App />);
