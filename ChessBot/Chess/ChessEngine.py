#Class Gamestate stores all information about the board, and all valid moves at the state/
class GameState():
    def __init__(self):
        #8x8 2d List, each element has 2 characters
        #first character represents color (b or w)
        #second character represents peice ( p: pawn, R: Rook, N: knight, B: Bishop, Q: Queen, K: King)
        #"--" is empty space without peice
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp",d"wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.whiteToMove = True
        self.moveLog = []
