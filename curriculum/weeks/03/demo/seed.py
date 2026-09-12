"""Deliberately incomplete seed implementation for the instructor exercise."""


def seed_users(connection, count=100):
    connection.execute(
        "CREATE TABLE IF NOT EXISTS users "
        "(id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE)"
    )
    # Intentional bug: only one user is inserted, irrespective of count.
    connection.execute("INSERT INTO users (email) VALUES ('user0@example.test')")
    connection.commit()
