'''
This class is responsible for storing all th info about the current state of a chess game . It will also be responsible for determining the valid moves at the current state . It will also keep a move log.
'''
class GameState():
    def __init__(self):
        # Board is 8X8 2d list , each  element of teh list has 2 character ,
        # first char shows the color 'b' or 'w'
        # second char shows the type of piece 'K','Q','B','N','R' or 'p'
        # "--" represent empty space
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self,move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved 
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove


class Move():
    # maping keys to value 
    # key :value using dict

    ranksToRows = {
        "1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0
    }
    rowsToRanks = {v : k for k, v in ranksToRows.items()}
    
    filesToCols = {
        "a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7
    }
    colsToFiles = {v : k for k, v in filesToCols.items()}
    
    def __init__(self,startSq,endSq,board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startRow]
        self.pieceCaptured = board[self.endCol][self.endRow] 

    def getChessNotation(self):
        return self.getRankFile(self.startRow , self.startCol) + self.getRankFile(self.endRow,self.endCol)


    def getRankFile(self,r,c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
            
