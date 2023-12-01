from abc import ABC, abstractmethod
import numpy as np

BOARD = np.zeros((4,7))

class Rock(ABC):
    def __init__(self) -> None:
        self.rested = False
        super().__init__()
    
    @abstractmethod
    def can_move_left(self, row, board):
        pass
    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def can_move_right(self, row, board):
        pass
    @abstractmethod
    def right(self):
        pass

    @abstractmethod
    def cant_move_down(self, row, board):
        pass

    def down(self, row, board, check_move = True):
        if check_move and self.cant_move_down(row, board):
            self.rest(row, board)
            return row
        else:
            row = row+1
            return row
    
    def rest(self):
        self.rested = True

class Horizontal(Rock):
    def __init__(self) -> None:
        self.height = 1
        self.column = np.array([2,3,4,5])
        self.rock = np.ones((self.height,4))
        self.name =  "Horizontal"
        super().__init__()

    def can_move_left(self, row, board):
        left_side = self.column[0] 
        return left_side > 0 and not board[row, left_side-1]

    def left(self, row, board):
        self.column = self.column - 1 if self.can_move_left(row, board) else self.column
    
    def can_move_right(self, row, board):
        right_side = self.column[-1] 
        return right_side < 6 and not board[row, right_side+1]

    def right(self, row, board):
        self.column = self.column + 1 if self.can_move_right(row, board) else self.column
        
    def cant_move_down(self, row, board):
        return row >= board.shape[0]-1 or any(board[row+1, self.column])
         
    def rest(self, row, board):
        board[row, self.column] = self.rock
        super().rest()

class Vertical(Rock):
    def __init__(self) -> None:
        self.height = 4
        self.rock = np.ones((self.height,1))
        self.column = 2
        self.name = "Vertical"
        super().__init__()

    def can_move_left(self, row, board):
        column = self.column
        return column > 0 and (row < self.height - 1 or not any(board[row-self.height+1:row+1,column-1]))

    def left(self, row, board):
        self.column = self.column - 1 if self.can_move_left(row, board) else self.column
        
    def can_move_right(self, row, board):
        column = self.column
        return column < 6 and (row < self.height - 1 or not any(board[row-self.height+1:row+1,column+1]))

    def right(self, row, board):
        self.column = self.column + 1 if self.can_move_right(row, board) else self.column
        
    def cant_move_down(self, row, board):
        return row >= board.shape[0]-1 or board[row+1, self.column]
    
    def rest(self, row, board):
        board[row-self.height+1:row+1, self.column] = np.ones(self.height)
        super().rest()

class Box(Rock):
    def __init__(self) -> None:
        self.height = 2
        self.rock = np.ones((self.height,self.height))
        self.column = np.array([2,3])
        self.name = "Box"
        super().__init__()

    def can_move_left(self, row, board):
        left_column = self.column[0]
        return left_column > 0 and (row < self.height -1 or not any(board[row-self.height+1:row+1, left_column-1]))

    def left(self, row, board):
        self.column = self.column - 1 if self.can_move_left(row,board) else self.column
    
    def can_move_right(self, row, board):
        right_column = self.column[-1]
        return right_column < 6 and (row < self.height - 1 or not any(board[row-self.height+1:row+1, right_column + 1]))

    def right(self, row, board):
        self.column = self.column + 1 if self.can_move_right(row, board) else self.column
        
    def cant_move_down(self, row, board):
        return row >= board.shape[0]-1 or any(board[row+1, self.column])
    
    def rest(self, row, board):
        board[row-self.height+1:row+1, self.column] = self.rock
        super().rest()

class Corner(Rock):
    def __init__(self) -> None:
        self.height = 3
        self.column = np.array([2,3,4])
        self.rock = np.array([[0,0,1],[0,0,1],[1,1,1]])
        self.name = "Corner"
        super().__init__()

    def can_move_left(self, row, board):
        left_side = self.column[0] 
        return left_side > 0 and not board[row, left_side-1]

    def left(self, row, board):
        self.column = self.column - 1 if self.can_move_left(row, board) else self.column

    def can_move_right(self, row, board):
        column = self.column[-1]
        return column < 6 and (row < self.height - 1 or not any(board[row-self.height+1:row+1,column+1]))

    def right(self, row, board):
        self.column = self.column + 1 if self.can_move_right(row, board) else self.column
        
    def cant_move_down(self, row, board):
        return row >= board.shape[0]-1 or any(board[row+1, self.column])
    
    def rest(self, row, board):
        frame = board[row-self.height+1:row+1, self.column]
        board[row-self.height+1:row+1, self.column] = np.logical_or(self.rock, frame)
        super().rest()

class Star(Rock):
    def __init__(self) -> None:
        self.height = 3
        self.column = np.array([2,3,4])
        self.rock = np.array([[0,1,0],[1,1,1],[0,1,0]])
        self.name = "Star"
        super().__init__()

    def can_move_left(self, row, board):
        left_column = self.column[0]
        return left_column > 0 and (row < 2  or 
                                not any(board[[row, row-1, row-2],
                                            [left_column, left_column-1, left_column]]))

    def left(self, row, board):
        self.column = self.column - 1 if self.can_move_left(row, board) else self.column

    def can_move_right(self, row, board):
        right_column = self.column[-1]
        return right_column < 6 and (row < 2 or 
                                not any(board[[row, row-1, row-2],
                                            [right_column, right_column+1, right_column]]))
    def right(self, row, board):
        self.column = self.column + 1 if self.can_move_right(row, board) else self.column
        
    def cant_move_down(self, row, board):
        return row >= board.shape[0]-1 or any(board[row, [self.column[0], self.column[-1]]]) or board[row+1, self.column[1]]
    
    def rest(self, row, board):
        frame = board[row-self.height+1:row+1, self.column]
        board[row-self.height+1:row+1, self.column] = np.logical_or(self.rock, frame)
        super().rest()

ROCKS = [Horizontal, Star, Corner, Vertical, Box]


""" horizontal = Horizontal()
print(horizontal.rested)
horizontal.left()
horizontal.down(3, BOARD)
print(horizontal.rested)
print(BOARD)

box = Box()
print(box.rested)
for i in range(3):
    box.left()
box.down(2, BOARD)
print(box.rested)
print(BOARD) 

vertical = Vertical()
for i in range(3):
    vertical.right()
vertical.down(3, BOARD)
print(BOARD)
 
corner = Corner()
for i in range(3):
    corner.right()
corner.down(3, BOARD)
print(BOARD)
"""
""" horizontal = Horizontal()

horizontal.down(3, BOARD)

print(BOARD)
star = Star()
for i in range(2):
    star.left()
star.down(3, BOARD)
print(BOARD)
 """
""" horizontal = Horizontal()

horizontal.down(3, BOARD)
corner = Corner()
for i in range(3):
    corner.right()
corner.down(2, BOARD)
print(BOARD) """

""" class Board(np.ndarray):
    def __new__(cls) -> None:
        obj = super().__new__(cls, shape = (3,7), buffer = np.zeros((3,7)))
        return obj

    def stack(self,rows = 3):
        np.stack((np.zeros((rows,7)), self) )
        return self


board = Board().stack()
print(board) """