# game.py
from typing import List, Optional, Tuple

Board = List[Optional[str]]  # 9 cells: 'X', 'O', or None

WIN_LINES = [
    (0,1,2), (3,4,5), (6,7,8),  # rows
    (0,3,6), (1,4,7), (2,5,8),  # cols
    (0,4,8), (2,4,6),           # diagonals
]

def new_board() -> Board:
    return [None]*9

def make_move(board: Board, index: int, player: str) -> Board:
    if index < 0 or index >= 9:
        raise ValueError("Index out of range")
    if player not in ("X","O"):
        raise ValueError("Player must be 'X' or 'O'")
    if board[index] is not None:
        raise ValueError("Cell already taken")
    newb = board.copy()
    newb[index] = player
    return newb

def winner(board: Board) -> Optional[str]:
    for a,b,c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_full(board: Board) -> bool:
    return all(cell is not None for cell in board)

def game_status(board: Board) -> Tuple[str, Optional[str]]:
    """
    Return ("in_progress"/"draw"/"win", winner_or_None)
    """
    w = winner(board)
    if w:
        return ("win", w)
    if is_full(board):
        return ("draw", None)
    return ("in_progress", None)
