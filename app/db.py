import sqlite3
from datetime import datetime


def init_db():
    conn = sqlite3.connect("leads.sqlite")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT,
            status TEXT DEFAULT 'New',
            last_contacted TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_lead(name, email, message):
    conn = sqlite3.connect("leads.sqlite")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leads (name, email, message, last_contacted) VALUES (?, ?, ?, ?)",
                   (name, email, message, datetime.now().isoformat()))
    conn.commit()
    conn.close()


def get_one_lead(email):
    conn = sqlite3.connect("leads.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, message, status, last_contacted FROM leads WHERE email = ?", (email,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_all_leads():
    conn = sqlite3.connect("leads.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, message, status, last_contacted FROM leads")
    rows = cursor.fetchall()
    conn.close()
    return rows
