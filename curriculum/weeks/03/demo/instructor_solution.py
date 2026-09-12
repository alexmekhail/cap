"""Instructor reference: copy as seed.py only in the rehearsal workspace."""


def seed_users(connection, count=100):
    if count < 0:
        raise ValueError("count must be non-negative")
    connection.execute(
        "CREATE TABLE IF NOT EXISTS users "
        "(id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE)"
    )
    connection.executemany(
        "INSERT INTO users (email) VALUES (?) ON CONFLICT(email) DO NOTHING",
        [(f"user{number}@example.test",) for number in range(count)],
    )
    connection.commit()
