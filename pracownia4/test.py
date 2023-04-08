import random
import sys
from collections import defaultdict as dd
from turtle import *
import copy
import time

#####################################################
# turtle graphic
#####################################################
#tracer(0, 1)

BOK = 50
SX = -100
SY = 0
M = 8


def kwadrat(x, y, kolor):
    fillcolor(kolor)
    pu()
    goto(SX + x * BOK, SY + y * BOK)
    pd()
    begin_fill()
    for i in range(4):
        fd(BOK)
        rt(90)
    end_fill()


def kolko(x, y, kolor):
    fillcolor(kolor)

    pu()
    goto(SX + x * BOK + BOK/2, SY + y * BOK - BOK)
    pd()
    begin_fill()
    circle(BOK/2)
    end_fill()

#####################################################

#słabe
weights2 = ((200, -100, 100,  50,  50, 100, -100,  200),
           (-100, -200, -50, -50, -50, -50, -200, -100),
           (100,  -50, 100,   0,   0, 100,  -50,  100),
           (50,  -50,   0,   0,   0,   0,  -50,   50),
           (50,  -50,   0,   0,   0,   0,  -50,   50),
           (100,  -50, 100,   0,   0, 100,  -50,  100),
           (-100, -200, -50, -50, -50, -50, -200, -100),
           (200, -100, 100,  50,  50, 100, -100,  200))

weights = ((100, -20, 10,  5,  5, 10, -20, 100),
           (-20, -50,  -2, -2, -2, -2, -50, -20),
           (10,   -2,   0, -1, -1,  0,  -2,  10),
           (5,    -2,  -1, -1, -1, -1,  -2,   5),
           (5,    -2,  -1, -1, -1, -1,  -2,   5),
           (10,   -2,   0, -1, -1,  0,  -2,  10),
           (-20, -50,  -2, -2, -2, -2, -50, -20),
           (100, -20,  10,  5,  5, 10, -20, 100))

def initial_board():
    B = [[None] * M for i in range(M)]
    B[3][3] = 1
    B[4][4] = 1
    B[3][4] = 0
    B[4][3] = 0
    return B


def custom_deepcopy(object):
    B = Board()
    B.board = []
    for row in object.board:
        B.board.append(row.copy())
    B.fields = copy.copy(object.fields)
    return B

class Board:
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def __init__(self):
        self.board = initial_board()
        self.fields = set()
        self.move_list = []
        self.history = []
        for i in range(M):
            for j in range(M):
                if self.board[i][j] == None:   
                    self.fields.add((j, i))
                                                
    def draw(self):
        for i in range(M):
            res = []
            for j in range(M):
                b = self.board[i][j]
                if b == None:
                    res.append('.')
                elif b == 1:
                    res.append('#')
                else:
                    res.append('o')
            print(''.join(res))
        print()

    def show(self):
        for i in range(M):
            for j in range(M):
                kwadrat(j, i, 'green')
                
        for i in range(M):
            for j in range(M):                
                if self.board[i][j] == 1:
                    kolko(j, i, 'black')
                if self.board[i][j] == 0:
                    kolko(j, i, 'white')
                                   
    def moves(self, player):
        res = []
        for (x, y) in self.fields:
            if any(self.can_beat(x, y, direction, player) for direction in Board.dirs):
                res.append((x, y))
        if not res:
            return [None]
        return res               

    # checking if player's ( = 'player') disk can be placed in (x, y) by checking if it would
    # beat anything lying in direction = 'd'
    def can_beat(self, x, y, d, player):
        dx, dy = d
        x += dx
        y += dy
        cnt = 0
        while self.get(x, y) == 1-player:
            x += dx
            y += dy
            cnt += 1
        return cnt > 0 and self.get(x, y) == player

    def get(self, x, y):
        if 0 <= x < M and 0 <= y < M:
            return self.board[y][x]
        return None
                        
    def do_move(self, move, player):
        self.history.append([x[:] for x in self.board])
        self.move_list.append(move)
        
        if move == None:
            return
        x, y = move
        x0, y0 = move
        self.board[y][x] = player
        self.fields -= set([move])
        for dx, dy in self.dirs:
            x, y = x0, y0
            to_beat = []
            x += dx
            y += dy
            while self.get(x, y) == 1-player:
                to_beat.append((x, y))
                x += dx
                y += dy
            if self.get(x, y) == player:
                for (nx, ny) in to_beat:
                    self.board[ny][nx] = player

    # result > 0  <=> white wins (#)
    def result(self):
        res = 0
        for y in range(M):
            for x in range(M):
                b = self.board[y][x]                
                if b == 0:
                    res -= 1
                elif b == 1:
                    res += 1
        return res
                
    def terminal(self):
        if not self.fields:
            return True
        if len(self.move_list) < 2:
            return False
        return self.move_list[-1] == self.move_list[-2] == None 

    def random_move(self, player):
        ms = self.moves(player)
        if ms:
            return random.choice(ms)
        return [None]

    def heuristic(self):
        res = 0
        for y in range(M):
            for x in range(M):
                b = self.board[y][x]
                if b == 0:
                    res += weights[y][x]
                elif b == 1:
                    res -= weights[y][x]
        return res

    '''def find_best(self, depth, player):
        def alfabetasearch(state, depth, alfa, beta, maximizing_player):
            # depth = 0 or end of the game or no moves possible
            if depth == 0 or state.terminal() or state.moves(maximizing_player) == [None]:
                return state.heuristic()
            children_moves = state.moves(maximizing_player)
            # player == 1 <=> player == white <=> enemy's move
            if maximizing_player:
                for m in children_moves:
                    new_board = custom_deepcopy(state)
                    new_board.do_move(m, maximizing_player)
                    alfa = max(alfa, alfabetasearch(new_board, depth - 1, alfa, beta, 0))
                    if alfa >= beta:
                        break
                return alfa
            # enemy's move
            else:
                for m in children_moves:
                    new_board = custom_deepcopy(state)
                    new_board.do_move(m, maximizing_player)
                    beta = min(beta, alfabetasearch(new_board, depth - 1, alfa, beta, 1))
                    if alfa >= beta:
                        break
                return alfa
        best_move = None
        best_value = -1e9
        for move in self.moves(player):
            new_board = custom_deepcopy(self)
            new_board.do_move(move, player)
            value = alfabetasearch(new_board, depth, -1e9, 1e9, 1 - player)
            #print(depth)
            if value >= best_value:
                best_value = value
                best_move = move
        return best_move'''

    def find_best(self, depth, player):
        def alphabeta(state, depth, alpha, beta, maximizing_player):
            # depth = 0 or end of the game or no moves possible
            if depth == 0 or state.terminal() or state.moves(maximizing_player) == [None]:
                return state.heuristic()

            children = state.moves(maximizing_player)
            # player == 1 <=> player == white <=> enemy's move
            if maximizing_player:
                for move in children:
                    new_board = custom_deepcopy(state)
                    new_board.do_move(move, player)
                    alpha = max(alpha, alphabeta(new_board, depth-1, alpha, beta, False))
                    if alpha >= beta:
                        break
                return alpha
            # our move
            else:
                for move in children:
                    new_board = custom_deepcopy(state)
                    new_board.do_move(move, player)
                    beta = min(beta, alphabeta(new_board, depth-1, alpha, beta, True))
                    if alpha >= beta:
                        break
                return beta

        best_move = None
        best_score = -1e9
        for move in self.moves(player):
            new_board = custom_deepcopy(self)
            new_board.do_move(move, player)

            val = alphabeta(new_board, depth, -1e9, 1e9, 1 - player)
            if val > best_score:
                best_move = move
                best_score = val

        return best_move


white_win = 0
depth = int(input())

for j in range(5):
    start = time.time()
    for i in range(1000):
        player = 0
        B = Board()

        while True:
            if player:
                m = B.random_move(player)
                B.do_move(m, player)
            else:
                m = B.find_best(depth, player)
                B.do_move(m, player)
            player = 1-player
            if B.terminal():
                break

        if B.result() < 0:
            white_win += 1
        print(white_win, i + 1)

    end = time.time()
    print(end - start)
    print(white_win)
    white_win = 0
input('Game over!')
sys.exit(0)         