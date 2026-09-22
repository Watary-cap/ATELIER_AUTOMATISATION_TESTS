import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "runs.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS runs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  passed INTEGER,
                  failed INTEGER,
                  error_rate REAL,
                  latency_avg REAL,
                  latency_p95 REAL,
                  details TEXT)''')
    conn.commit()
    conn.close()

def save_run(run_data):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    summary = run_data.get("summary", {})
    c.execute('''INSERT INTO runs 
                 (timestamp, passed, failed, error_rate, latency_avg, latency_p95, details)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''', 
              (run_data.get("timestamp"), 
               summary.get("passed", 0), 
               summary.get("failed", 0),
               summary.get("error_rate", 0),
               summary.get("latency_ms_avg", 0),
               summary.get("latency_ms_p95", 0),
               json.dumps(run_data.get("tests", []))))
    conn.commit()
    conn.close()

def list_runs():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM runs ORDER BY id DESC LIMIT 20')
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]
