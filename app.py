# app.py
from flask import Flask, render_template, request, jsonify
from game import new_board, make_move, game_status
import storage
import json

app = Flask(__name__, static_folder="static", template_folder="templates")

# initialize DB
storage.init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/new", methods=["POST"])
def api_new():
    data = request.json or {}
    board = new_board()
    # client will manage moves; server returns initial state
    return jsonify({"board": board, "status": "in_progress"})

@app.route("/api/move", methods=["POST"])
def api_move():
    payload = request.json or {}
    board = payload.get("board")
    index = payload.get("index")
    player = payload.get("player")
    player_x = payload.get("player_x", "Player X")
    player_o = payload.get("player_o", "Player O")
    if board is None or index is None or player is None:
        return jsonify({"error": "board, index and player required"}), 400
    try:
        board = board.copy()
        board = make_move(board, int(index), player)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    status, win_player = game_status(board)
    if status in ("win", "draw"):
        # record to DB
        winner_name = None
        if status == "win":
            winner_name = player_x if win_player == "X" else player_o
        storage.record_game(player_x, player_o, winner_name, board)
    return jsonify({"board": board, "status": status, "winner": win_player})

@app.route("/api/history", methods=["GET"])
def api_history():
    h = storage.get_history(50)
    return jsonify(h)

@app.route("/api/leaderboard", methods=["GET"])
def api_leaderboard():
    lb = storage.get_leaderboard()
    return jsonify(lb)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
