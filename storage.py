# storage.py
import sqlite3
import json
from datetime import datetime
from typing import Dict, Any, List, Optional

DB_PATH = "tictactoe.db"

def init_db(path: str = DB_PATH):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        player_x TEXT,
        player_o TEXT,
        winner TEXT,
        moves TEXT -- JSON array of 9 elements
    )
    """)
    conn.commit()
    conn.close()

def record_game(player_x: Optional[str], player_o: Optional[str], winner: Optional[str], board: List[Optional[str]], path: str = DB_PATH) -> int:
    conn = sqlite3.connect(path)
    c = conn.cursor()
    ts = datetime.utcnow().isoformat()
    moves_json = json.dumps(board)
    c.execute("INSERT INTO games (timestamp, player_x, player_o, winner, moves) VALUES (?, ?, ?, ?, ?)",
              (ts, player_x, player_o, winner, moves_json))
    gid = c.lastrowid
    conn.commit()
    conn.close()
    return gid

def get_history(limit: int = 50, path: str = DB_PATH) -> List[Dict[str, Any]]:
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("SELECT id, timestamp, player_x, player_o, winner, moves FROM games ORDER BY id DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    history = []
    for r in rows:
        history.append({
            "id": r[0],
            "timestamp": r[1],
            "player_x": r[2],
            "player_o": r[3],
            "winner": r[4],
            "moves": json.loads(r[5])
        })
    return history

def get_leaderboard(path: str = DB_PATH) -> List[Dict[str, Any]]:
    conn = sqlite3.connect(path)
    c = conn.cursor()
    # Count wins per player
    c.execute("""
      SELECT winner, COUNT(*) as wins
      FROM games
      WHERE winner IS NOT NULL
      GROUP BY winner
      ORDER BY wins DESC
      LIMIT 20
    """)
    rows = c.fetchall()
    conn.close()
    return [{"player": r[0], "wins": r[1]} for r in rows]
