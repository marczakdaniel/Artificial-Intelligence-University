import random
import sys
import copy
from collections import defaultdict as dd
from turtle import *

#####################################################
# turtle graphic
#####################################################
tracer(0,1)

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

def initial_board():
    B = [ [None] * M for i in range(M)]
    B[3][3] = 1
    B[4][4] = 1
    B[3][4] = 0
    B[4][3] = 0
    return B

wagi1 = [[ 4, -3,  2,  2,  2,  2, -3,  4],
        [-3, -4, -1, -1, -1, -1, -4, -3],
        [ 2, -1,  1,  0,  0,  1, -1,  2],
        [ 2, -1,  0,  1,  1,  0, -1,  2],
        [ 2, -1,  0,  1,  1,  0, -1,  2],
        [ 2, -1,  1,  0,  0,  1, -1,  2],
        [-3, -4, -1, -1, -1, -1, -4, -3],
        [ 4, -3,  2,  2,  2,  2, -3,  4]]

wagi2 = ((100, -20, 10,  5,  5, 10, -20, 100),
           (-20, -50,  -2, -2, -2, -2, -50, -20),
           (10,   -2,   0, -1, -1,  0,  -2,  10),
           (5,    -2,  -1, -1, -1, -1,  -2,   5),
           (5,    -2,  -1, -1, -1, -1,  -2,   5),
           (10,   -2,   0, -1, -1,  0,  -2,  10),
           (-20, -50,  -2, -2, -2, -2, -50, -20),
           (100, -20,  10,  5,  5, 10, -20, 100))

wagi = [[20, -3, 11,  8,  8, 11, -3, 20],
        [-3, -7, -4,  1,  1, -4, -7, -3],
        [11, -4,  2,  2,  2,  2, -4, 11],
        [ 8,  1,  2, -3, -3,  2,  1,  8],
        [ 8,  1,  2, -3, -3,  2,  1,  8],
        [11, -4,  2,  2,  2,  2, -4, 11],
        [-3, -7, -4,  1,  1, -4, -7, -3],
        [20, -3, 11,  8,  8, 11, -3, 20]]


def takeFirst(p):
    return p[0]

class Board:
    dirs  = [ (0,1), (1,0), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1) ]
    
    
    def __init__(self):
        self.board = initial_board()
        self.fields = set()
        self.move_list = []
        self.history = []
        for i in range(M):
            for j in range(M):
                if self.board[i][j] == None:   
                    self.fields.add( (j,i) )
                                                
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
        for (x,y) in self.fields:
            if any( self.can_beat(x,y, direction, player) for direction in Board.dirs):
                res.append( (x,y) )
        if not res:
            return [None]
        return res               
    
    def can_beat(self, x,y, d, player):
        dx,dy = d
        x += dx
        y += dy
        cnt = 0
        while self.get(x,y) == 1-player:
            x += dx
            y += dy
            cnt += 1
        return cnt > 0 and self.get(x,y) == player
    
    def get(self, x,y):
        if 0 <= x < M and 0 <=y < M:
            return self.board[y][x]
        return None
                        
    def do_move(self, move, player):
        self.history.append([x[:] for x in self.board])
        self.move_list.append(move)
        
        if move == None:
            return
        x,y = move
        x0,y0 = move
        self.board[y][x] = player
        self.fields -= set([move])
        for dx,dy in self.dirs:
            x,y = x0,y0
            to_beat = []
            x += dx
            y += dy
            while self.get(x,y) == 1-player:
              to_beat.append( (x,y) )
              x += dx
              y += dy
            if self.get(x,y) == player:              
                for (nx,ny) in to_beat:
                    self.board[ny][nx] = player
                                                     
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
    
    def piece_difference(self):
        black = 0
        white = 0
        for i in range(M):
            for j in range(M):
                b = self.board[i][j]                
                if b == 0:
                    white += 1
                elif b == 1:
                    black += 1
        
        if (black == white):
            return 0
        elif (black > white):
            return 100 * (black / (black + white))
        return -100 * (white / (black + white))

    def corner_occupancy(self):
        w = 0
        b = self.board
        if (b[0][0] == 1):
            w += 1
        if (b[0][7] == 1):
            w += 1
        if (b[7][0] == 1):
            w += 1
        if (b[7][7] == 1):
            w += 1

        if (b[0][0] == 0):
            w -= 1
        if (b[0][7] == 0):
            w -= 1
        if (b[7][0] == 0):
            w -= 1
        if (b[7][7] == 0):
            w -= 1
        
        return 25 * w
    
    def corner_closeness(self):
        w = 0
        b = self.board
        if (b[0][0] == None):
            if (b[0][1] == 1):
                w += 1
            if (b[1][0] == 1):
                w += 1
        if (b[0][7] == None):
            if (b[0][6] == 1):
                w += 1
            if (b[1][7] == 1):
                w += 1
        if (b[7][0] == None):
            if (b[6][0] == 1):
                w += 1
            if (b[7][1] == 1):
                w += 1
        if (b[7][7] == None):
            if (b[6][7] == 1):
                w += 1
            if (b[7][6] == 1):
                w += 1
        
        if (b[0][0] == None):
            if (b[0][1] == 0):
                w -= 1
            if (b[1][0] == 0):
                w -= 1
        if (b[0][7] == None):
            if (b[0][6] == 0):
                w -= 1
            if (b[1][7] == 0):
                w -= 1
        if (b[7][0] == None):
            if (b[6][0] == 0):
                w -= 1
            if (b[7][1] == 0):
                w -= 1
        if (b[7][7] == None):
            if (b[6][7] == 0):
                w -= 1
            if (b[7][6] == 0):
                w -= 1
        
        return -12.5 * w
    
    def mobility(self):
        w = len(self.moves(0))
        b = len(self.moves(1))
        if (b == w  or b == 0 or w == 0):
            return 0
        if (b > w):
            return 100 * (b / (b + w))
        return -100 * (w / (b + w))

    def frontier_discs(self):
        b = self.board
        black = 0
        white = 0
        for i in range(M):
            for j in range(M):
                if (b[i][j] != None):
                    czy = False
                    if (i != 0 and b[i - 1][j] == None):
                        czy = True
                    if (i != 7 and b[i + 1][j] == None):
                        czy = True
                    if (j != 0 and b[i][j - 1] == None):
                        czy = True
                    if (j != 7 and b[i][j + 1] == None):
                        czy = True
                    if (i != 0 and j != 0 and b[i - 1][j - 1] == None):
                        czy = True
                    if (i != 7 and j != 7 and b[i + 1][j + 1] == None):
                        czy = True
                    if (i != 0 and j != 7 and b[i - 1][j + 1] == None):
                        czy = True
                    if (i != 7 and j != 0 and b[i + 1][j - 1] == None):
                        czy = True
                    if (czy):
                        if (b[i][j] == 1):
                            black += 1
                        else:
                            white += 1
        if (black == white):
            return 0
        elif (black > white):
            return -100 * (black / (black + white))
        return 100 * (white / (black + white))


    def disk_squares(self):
        wynik = 0
        for i in range(M):
            for j in range(M):
                if (self.board[i][j] == 1):
                    wynik += wagi[i][j]
                else:
                    wynik -= wagi[i][j]
        return ((wynik * 100) / 90) / 4
     
    
    def heuristic_value(self):
        h = [self.piece_difference(),
             self.corner_occupancy(),
             self.corner_closeness(),
             self.mobility(),
             self.frontier_discs(),
             self.disk_squares()]
        w = 0
        v = [10, 801.724, 382.026, 78.922, 74.396, 10]
        for i in range(6):
            w += h[i] * v[i]

        return w


    def best_move(self, player):
        def alphabeta(node, depth, alpha, beta, player):
            if (depth == 0 or node.terminal() == True or node.moves(player) == [None]):
                return node.heuristic_value()
            if player == 1:
                value = -10000000
                '''
                m = []
                for n in node.moves(player):
                    B = copy.deepcopy(node)
                    B.do_move(n, player)
                    #w_h = B.heuristic_value()
                    w_h = random.randint(1, 1000)
                    m.append([w_h, B])
                m.sort(key=takeFirst, reverse=True)
                for n in m:
                    value = max(value, alphabeta(n[1], depth - 1, alpha, beta, 1 - player))
                    if (value >= beta):
                        break
                    alpha = max(alpha, value)
                    return value
                '''
                for m in node.moves(player):
                    B = copy.deepcopy(node)
                    B.do_move(m, player)
                    value = max(value, alphabeta(B, depth - 1, alpha, beta, 1 - player))
                    if (value >= beta):
                        break
                    alpha = max(alpha, value)
                    return value
            else:
                
                value = 10000000
                '''
                m = []
                for n in node.moves(player):
                    B = copy.deepcopy(node)
                    B.do_move(n, player)
                    #w_h = B.heuristic_value()
                    w_h = random.randint(1, 1000)
                    m.append([w_h, B])
                m.sort(key=takeFirst)
                for n in m:
                    value = min(value, alphabeta(n[1], depth - 1, alpha, beta, 1 - player))
                    if (value <= alpha):
                        break
                    beta = min(beta, value)
                    return value
                '''
                for m in node.moves(player):
                    B = copy.deepcopy(node)
                    B.do_move(m, player)
                    value = min(value, alphabeta(B, depth - 1, alpha, beta, 1 - player))
                    if (value <= alpha):
                        break
                    beta = min(beta, value)
                    return value
            return value
        
        najlepszy_ruch = [None]
        koszt_ruchu = -10000000

        for m in self.moves(player):
            B = copy.deepcopy(self)
            B.do_move(m, player)
            value = alphabeta(B, 7, -10000000, 10000000, 1 - player)
            print(value)
            if(value >= koszt_ruchu):
                najlepszy_ruch =  m
                koszt_ruchu = value

        return najlepszy_ruch
            

player = 0
B = Board()

while True:
    B.draw()
    B.show()
    input()
    if (player == 1):
        m = B.best_move(player)
        print(m)
        print(B.moves(player))
        B.do_move(m, player)
    else:
        m = B.random_move(player)
        B.do_move(m, player)
    print(B.heuristic_value())
    player = 1 - player
    if B.terminal():
        break
    
B.draw()
B.show()
'''
wynik = 0
for i in range(1000):
    player = 0
    B = Board()
    #B.draw()
    #B.show()
    while True:
        if (player == 1):
            m = B.best_move(player)
            B.do_move(m, player)
        else:
            m = B.random_move(player)
            B.do_move(m, player)

        player = 1 - player
        if B.terminal():
            break
    if (B.result() >= 0):
        wynik += 1
    print (i + 1, wynik, i + 1 - wynik, B.result(), (wynik / (i + 1)) * 100)
    #B.draw()
    #B.show()
'''
print('Result', B.result())
#print(wynik)
input('Game over!')
  
       
sys.exit(0)                 