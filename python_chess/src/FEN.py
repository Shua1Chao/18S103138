from src.piece import Piece
import re

def fromFEN(fen):
    if(not valid_FEN(fen)):
        raise ValueError("Invalid FEN string.")

    parts = fen.split(' ')
    ranks = parts[0].split('/')
    # TODO: handle rest of FEN string
    board = []
    for r in range(0, len(ranks)):
        rank = ranks[r]
        row = []
        _y = r
        for s in range(0, len(rank)):
            sq = rank[s]
            _x = s
            if(re.match(r"\d", sq)):
                num_spaces = int(sq)
                for i in range(0, num_spaces):
                    _x = i
                    row.append(get_props(_x, _y))
            else:
                row.append(get_props(_x, _y, sq))
        board.append(row)

    return board

def valid_FEN(fen_str):
    fen_form = r"^\s*([rnbqkpRNBQKP1-8]+\/){7}([rnbqkpRNBQKP1-8]+)\s[bw]\s(-|K?Q?k?q?)\s(-|[a-h][36])"
    return re.match(fen_form, fen_str) is not None

def get_props(_x, _y, role=None):
    square_props = { 
        '_x': _x, 
        '_y': _y }

    square_props['piece'] = { 
        'color': 'w' if role.isupper() else 'b', 
        'role': role.lower() } if role else None

    return square_props