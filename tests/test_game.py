# tests/test_game.py
from game import new_board, make_move, winner, game_status, is_full

def test_new_board_empty():
    b = new_board()
    assert len(b) == 9
    assert all(x is None for x in b)

def test_win_row():
    b = [ 'X','X','X', None,None,None, None,None,None ]
    assert winner(b) == 'X'
    status, w = game_status(b)
    assert status == "win" and w == 'X'

def test_draw():
    b = ['X','O','X','X','O','O','O','X','X']
    assert is_full(b)
    status, w = game_status(b)
    assert status == "draw" and w is None

def test_make_move_invalid():
    b = new_board()
    b[0] = 'X'
    try:
        make_move(b, 0, 'O')
        raised = False
    except:
        raised = True
    assert raised
