# assignment: PA 5
# author: Zander Dumont-Strom
# date: 3/17/2023
# file: fifteen.py
# program where user must put the tiles in order to win the game

import numpy as np
from random import choice

class Fifteen:
    def __init__(self, size = 4):
        # Initialize the tiles
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        # Initialize the adjacency list
        self.adj = {0: [1,4], 1: [0,2,5], 2: [1,3,6], 3: [2,7], 4: [0,5,8], 5: [1,4,6,9], 6: [2,5,7,10], 7: [3,6,11], 8: [4,9,12], 9: [5,8,10,13], 10: [6,9,11,14], 11: [7,10,15], 12: [8,13], 13: [9,12,14], 14: [10,13,15], 15: [11,14]}
        self.size = size
        self.moves = 0

    def update(self, move):
        # update the puzzle with the move
        if self.is_valid_move(move):
            # Get the index of the move
            index = np.where(self.tiles == 0)[0][0]
            move_index = np.where(self.tiles == move)[0][0]
            # Swap the values
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            self.moves += 1
        else:
            print('Not a valid move!')
        
    def transpose(self, i, j):
        self.update((i,j))
        print(self)
        # Check if the puzzle is solved
        if self.tiles.tolist() == [i for i in range(1,self.size**2)] + [0]:
            print("You won in {} moves!".format(self.moves))
            return True
        return False


    def shuffle(self, steps=100):
        # Shuffle the puzzle
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice(self.adj[index])
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index
        self.moves = 0
        
        
    def is_valid_move(self, move):
        # return true if the move is valid
        index = self.adj[np.where(self.tiles == 0)[0][0]]
        if move in self.tiles[index]:
            return True
        return False

    def is_solved(self):
        # Check if the puzzle is solved
        if self.tiles.tolist() == [i for i in range(1,self.size**2)] + [0]:
            return True
        return False

    def draw(self):
        # Draw the puzzle
        print('+' + '---+'*self.size)
        for i in range(self.size):
            for j in range(self.size):
                char = int(self.tiles[i*self.size+j])
                if char == 0:
                    print('|' + ' '*3, end='')
                else:
                    if char < 10:
                        print('|' + ' ' + str(char) + ' ', end='')
                    else:
                        print('|' + str(char) + ' ', end='')
            print('|')
            print('+' + '---+'*self.size)

    def is_solvable(self):
        # Check if the puzzle is solvable
        moves = []
        for i in range(self.size):
            for j in range(self.size):
                if self.is_valid_move((i,j)):
                    moves.append((i,j))

        solutions = []
        for move in moves:
            new_puzzle = Fifteen()
            new_puzzle.tiles = self.tiles.copy()
            new_puzzle.moves = self.moves
            new_puzzle.update(move)
            if new_puzzle.is_solved():
                solutions.append([move])
            else:
                solution = new_puzzle.solve()
                if solution != None:
                    solutions.append([move] + solution)

        if len(solutions) == 0:
            return False
        else:
            return True


    def solve(self):
        # Solve the puzzle (if solvable)
        if self.is_solvable() == False:
            return None
        
        moves = []
        for i in range(self.size):
            for j in range(self.size):
                if self.is_valid_move((i,j)):
                    moves.append((i,j))

        solutions = []
        for move in moves:
            new_puzzle = Fifteen()
            new_puzzle.tiles = self.tiles.copy()
            new_puzzle.moves = self.moves
            new_puzzle.update(move)
            if new_puzzle.is_solved():
                solutions.append([move])
            else:
                solution = new_puzzle.solve()
                if solution != None:
                    solutions.append([move] + solution)

        if len(solutions) == 0:
            return None
        else:
            return min(solutions, key=len)
        
    def transpose(self, i, j):
        # Transpose the puzzle
        self.update((i,j))
        print(self)
        if self.tiles.tolist() == [i for i in range(1,self.size**2)] + [0]:
            print("You won in {} moves!".format(self.moves))
            return True
        return False

    def __str__(self):
        # string method for the puzzle
        s = ''
        character_space = 2
        dividor_space = 1
        for i in range(self.size):
            for j in range(self.size):
                char = int(self.tiles[i*self.size+j])
                if char == 0:
                    s += ' ' * character_space
                elif char < 10:
                    s += ' ' + str(char)
                else:
                    s += str(char)

                s += ' '*dividor_space
            s += '\n'
        return s
    

if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    # play game
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
