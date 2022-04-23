"""
https://docs.python.org/3/library/sqlite3.html
"""
import pytest
import sqlite3


def test_sqlite3_connect():
    conn = sqlite3.connect(':memory:')

    assert conn is not None

    conn.close()


def test_sqlite3_cursor():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    assert cursor is not None

    cursor.close()
    conn.close()


def test_sqlite3_integration():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO test (name) VALUES (?)', ('test',))
    cursor.execute('SELECT * FROM test')
    result = cursor.fetchall()

    assert result is not None
    assert len(result) == 1
    assert result[0][0] == 1
    assert result[0][1] == 'test'

    cursor.close()
    conn.close()
