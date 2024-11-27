from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):

        row, col = self.position
        moves = []
        if self.color == "black":
            forward = (row - 1, col)
        else:
            forward = (row + 1, col)     

        if self.is_position_on_board(forward):
            moves.append(forward)
        

        return moves
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        
       
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        
        row, col = self.position
        moves = []

        
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for d_row, d_col in directions:
            for step in range(1, 8):  
                new_position = (row + step * d_row, col + step * d_col)
                if self.is_position_on_board(new_position):
                    moves.append(new_position)
                else:
                    break 

        return moves
    


class Rook(Piece):
     def possible_moves(self):

        row, col = self.position
        moves = []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for d_row, d_col in directions:
            for step in range(1, 8): 
                new_position = (row + step * d_row, col + step * d_col)
                if self.is_position_on_board(new_position):
                    moves.append(new_position)
                else:
                    break  

        return moves


class Queen(Piece):
    def possible_moves(self):

        row, col = self.position
        moves = []

        
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1), 
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for d_row, d_col in directions:
            for step in range(1, 8):  
                new_position = (row + step * d_row, col + step * d_col)
                if self.is_position_on_board(new_position):
                    moves.append(new_position)
                else:
                    break  

        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        
        row, col = self.position
        moves = []

    
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Vertikální a horizontální
            (1, 1), (1, -1), (-1, 1), (-1, -1) # Diagonální
        ]

        for d_row, d_col in directions:
            new_position = (row + d_row, col + d_col)
            if self.is_position_on_board(new_position):
                moves.append(new_position)

        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    #testy
    knight = Knight("white", (1, 5))
    print(knight)
    print("Possible moves:", knight.possible_moves())

    pawn = Pawn("black", (5, 2))
    print(pawn)
    print("Possible moves:", pawn.possible_moves())

    bishop = Bishop("white", (6, 4))
    print(bishop)
    print("Possible moves:", bishop.possible_moves())

    rook = Rook("white", (1, 3))
    print(rook)
    print("Possible moves:", rook.possible_moves())

    queen = Queen("white", (6, 4))
    print(queen)
    print("Possible moves:", queen.possible_moves())


    king = King("black", (2, 4))
    print(king)
    print("Possible moves:", king.possible_moves())