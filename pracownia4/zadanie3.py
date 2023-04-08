import random
import sys
import copy


class Jungle:
    PIECES_VALUE = {
        0: 500,
        1: 200,
        2: 300,
        3: 400,
        4: 500,
        5: 800,
        6: 900,
        7: 1000
    }
    PIECES_DEVELOPMENT = {
        0: [[11, 13, 50, 1000000, 50, 13, 13],
            [11, 12, 13, 50, 13, 13, 13],
            [10, 11, 11, 13, 13, 13, 13],
            [8, 9, 9, 11, 12, 12, 13],
            [8, 9, 9, 11, 12, 12, 12],
            [8, 9, 9, 10, 12, 12, 11],
            [8, 8, 8, 9, 10, 10, 10],
            [8, 8, 8, 9, 9, 9, 9],
            [8, 8, 8, 0, 8, 8, 8]],
        1: [[11, 15, 50, 1000000, 50, 15, 11],
            [11, 11, 15, 50, 15, 11, 11],
            [10, 11, 11, 15, 11, 11, 10],
            [10, 0, 0, 10, 0, 0, 8],
            [10, 0, 0, 8, 0, 0, 8],
            [10, 0, 0, 8, 0, 0, 8],
            [10, 10, 10, 8, 8, 8, 8],
            [13, 10, 8, 8, 8, 8, 8],
            [8, 8, 8, 0, 8, 8, 8]],
        2: [[11, 15, 50, 1000000, 50, 15, 11],
            [10, 11, 15, 50, 15, 11, 10],
            [9, 10, 11, 15, 11, 10, 9],
            [9, 0, 0, 10, 0, 0, 9],
            [8, 0, 0, 8, 0, 0, 8],
            [8, 0, 0, 8, 0, 0, 8],
            [8, 8, 10, 8, 8, 8, 8],
            [8, 12, 13, 8, 8, 8, 8],
            [8, 12, 12, 0, 8, 8, 8]],
        3: [[11, 15, 50, 1000000, 50, 15, 11],
            [10, 11, 15, 50, 15, 11, 10],
            [9, 10, 11, 15, 11, 10, 9],
            [9, 0, 0, 10, 0, 0, 9],
            [8, 0, 0, 8, 0, 0, 8],
            [8, 0, 0, 8, 0, 0, 8],
            [8, 8, 8, 8, 8, 8, 8],
            [8, 8, 8, 8, 13, 10, 8],
            [8, 8, 8, 0, 12, 12, 8]],
        4: [[14, 15, 50, 1000000, 50, 15, 14],
            [13, 14, 15, 50, 15, 14, 13],
            [13, 13, 14, 15, 14, 13, 13],
            [12, 0, 0, 15, 0, 0, 12],
            [11, 0, 0, 14, 0, 0, 11],
            [10, 0, 0, 13, 0, 0, 10],
            [9, 9, 9, 10, 10, 9, 9],
            [9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 0, 9, 9, 9]],
        5: [[25, 30, 50, 1000000, 50, 30, 25],
            [25, 25, 30, 50, 30, 25, 25],
            [18, 20, 20, 30, 20, 20, 18],
            [15, 0, 0, 15, 0, 0, 15],
            [15, 0, 0, 15, 0, 0, 15],
            [15, 0, 0, 15, 0, 0, 15],
            [14, 16, 16, 14, 16, 16, 14],
            [12, 14, 12, 12, 12, 12, 12],
            [10, 12, 12, 0, 12, 12, 10]],
        6: [[25, 30, 50, 1000000, 50, 30, 25],
            [25, 25, 30, 50, 30, 25, 25],
            [18, 20, 20, 30, 20, 20, 18],
            [15, 0, 0, 15, 0, 0, 15],
            [15, 0, 0, 15, 0, 0, 15],
            [15, 0, 0, 15, 0, 0, 15],
            [14, 16, 16, 14, 16, 16, 14],
            [12, 12, 12, 12, 12, 14, 12],
            [10, 12, 12, 0, 12, 12, 10]],
        7: [[25, 30, 50, 1000000, 50, 30, 25],
            [25, 25, 30, 50, 30, 25, 25],
            [18, 20, 20, 30, 20, 20, 18],
            [16, 0, 0, 16, 0, 0, 16],
            [14, 0, 0, 14, 0, 0, 14],
            [12, 0, 0, 12, 0, 0, 12],
            [10, 15, 14, 14, 14, 14, 12],
            [11, 11, 11, 11, 11, 11, 11],
            [11, 11, 11, 0, 11, 11, 11]]

    }
    MAXIMAL_PASSIVE = 30
    DENS_DIST = 0.1
    MX = 7
    MY = 9
    traps = {(2, 0), (4, 0), (3, 1), (2, 8), (4, 8), (3, 7)}
    ponds = {(x, y) for x in [1, 2, 4, 5] for y in [3, 4, 5]}
    dens = [(3, 8), (3, 0)]
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    rat, cat, dog, wolf, jaguar, tiger, lion, elephant = range(8)

    def __init__(self):
        self.board = self.initial_board()
        self.pieces = {0: {}, 1: {}}

        for y in range(Jungle.MY):
            for x in range(Jungle.MX):
                C = self.board[y][x]
                if C:
                    pl, pc = C
                    self.pieces[pl][pc] = (x, y)
        self.curplayer = 0
        self.peace_counter = 0
        self.winner = None

    def initial_board(self):
        pieces = """
        L.....T
        .D...C.
        R.J.W.E
        .......
        .......
        .......
        e.w.j.r
        .c...d.
        t.....l
        """

        B = [x.strip() for x in pieces.split() if len(x) > 0]
        T = dict(zip('rcdwjtle', range(8)))

        res = []
        for y in range(9):
            raw = 7 * [None]
            for x in range(7):
                c = B[y][x]
                if c != '.':
                    if 'A' <= c <= 'Z':
                        player = 1
                    else:
                        player = 0
                    raw[x] = (player, T[c.lower()])
            res.append(raw)
        return res

    def random_move(self, player):
        ms = self.moves(player)
        if ms:
            return random.choice(ms)
        return None

    def can_beat(self, p1, p2, pos1, pos2):
        if pos1 in Jungle.ponds and pos2 in Jungle.ponds:
            return True  # rat vs rat
        if pos1 in Jungle.ponds:
            return False  # rat in pond cannot beat any piece on land
        if p1 == Jungle.rat and p2 == Jungle.elephant:
            return True
        if p1 == Jungle.elephant and p2 == Jungle.rat:
            return False
        if p1 >= p2:
            return True
        if pos2 in Jungle.traps:
            return True
        return False

    def pieces_comparison(self):
        for i in range(7,-1,-1):
            ps = []
            for p in [0,1]:
                if i in self.pieces[p]:
                    ps.append(p)
            if len(ps) == 1:
                return ps[0]
        return None
                
    def rat_is_blocking(self, player_unused, pos, dx, dy):        
        x, y = pos
        nx = x + dx
        for player in [0,1]:
            if Jungle.rat not in self.pieces[1-player]:
                continue
            rx, ry = self.pieces[1-player][Jungle.rat]
            if (rx, ry) not in self.ponds:
                continue
            if dy != 0:
                if x == rx:
                    return True
            if dx != 0:
                if y == ry and abs(x-rx) <= 2 and abs(nx-rx) <= 2:
                    return True
        return False

    def draw(self):
        TT = {0: 'rcdwjtle', 1: 'RCDWJTLE'}
        for y in range(Jungle.MY):

            L = []
            for x in range(Jungle.MX):
                b = self.board[y][x]
                if b:
                    pl, pc = b
                    L.append(TT[pl][pc])
                else:
                    L.append('.')
            print(''.join(L))
        print('')

    def moves(self, player):
        res = []
        for p, pos in self.pieces[player].items():
            x, y = pos
            for (dx, dy) in Jungle.dirs:
                pos2 = (nx, ny) = (x+dx, y+dy)
                if 0 <= nx < Jungle.MX and 0 <= ny < Jungle.MY:
                    if Jungle.dens[player] == pos2:
                        continue
                    if pos2 in self.ponds:
                        if p not in (Jungle.rat, Jungle.tiger, Jungle.lion):
                            continue
                        #if self.board[ny][nx] is not None:
                        #    continue  # WHY??
                        if p == Jungle.tiger or p == Jungle.lion:
                            if dx != 0:
                                dx *= 3
                            if dy != 0:
                                dy *= 4
                            if self.rat_is_blocking(player, pos, dx, dy):
                                continue
                            pos2 = (nx, ny) = (x+dx, y+dy)
                    if self.board[ny][nx] is not None:
                        pl2, piece2 = self.board[ny][nx]
                        if pl2 == player:
                            continue
                        if not self.can_beat(p, piece2, pos, pos2):
                            continue
                    res.append((pos, pos2))
        return res

    def victory(self, player):
        oponent = 1-player        
        if len(self.pieces[oponent]) == 0:
            self.winner = player
            return True

        x, y = self.dens[oponent]
        if self.board[y][x]:
            self.winner = player
            return True
        
        if self.peace_counter >= Jungle.MAXIMAL_PASSIVE:
            r = self.pieces_comparison()
            if r is None:
                self.winner = 1 # draw is second player's victory 
            else:
                self.winner = r
            return True
        return False

    def do_move(self, m):
        self.curplayer = 1 - self.curplayer
        if m is None:
            return
        pos1, pos2 = m
        x, y = pos1
        pl, pc = self.board[y][x]

        x2, y2 = pos2
        if self.board[y2][x2]:  # piece taken!
            pl2, pc2 = self.board[y2][x2]
            del self.pieces[pl2][pc2]
            self.peace_counter = 0
        else:
            self.peace_counter += 1    

        self.pieces[pl][pc] = (x2, y2)
        self.board[y2][x2] = (pl, pc)
        self.board[y][x] = None

    def update(self, player, move_string):
        assert player == self.curplayer
        move = tuple(int(m) for m in move_string.split())
        if len(move) != 4:
            raise("WrongMove")
        possible_moves = self.moves(player)
        if not possible_moves:
            if move != (-1, -1, -1, -1):
                raise("WrongMove")
            move = None
        else:
            move = ((move[0], move[1]), (move[2], move[3]))
            if move not in possible_moves:
                raise("WrongMove")
        self.do_move(move)
        
        if self.victory(player):
            assert self.winner is not None
            return 2 * self.winner - 1
        else:
            return None
    
    def heuristic_value(self, player):
        wynik = 0
        for i in self.pieces[player]:
            wynik += Jungle.PIECES_VALUE[i]
        for i in self.pieces[1 - player]:
            wynik -= Jungle.PIECES_VALUE[i]
        return wynik

    def heuristic_development(self, player):
        wynik = 0
        for i in self.pieces[player]:
            poz = self.pieces[player][i]
            x = poz[0]
            y = poz[1]

            wynik += self.PIECES_DEVELOPMENT[i][y][x]
        for i in self.pieces[1 - player]:
            poz = self.pieces[1 - player][i]
            x = poz[0]
            y = poz[1]
            wynik -= self.PIECES_DEVELOPMENT[i][8 - y][6 - x]
        return wynik


    def evaluate(self, player):        
        return self.heuristic_value(player) + self.heuristic_development(player)


    
    def random_agent(self, player):
        moves = self.moves(player)
        if moves:
            move = random.choice(moves)
            return move
        else:
            return None
    
    def smart_random_agent(self, player):
        moves = self.moves(player)
        ile = Jungle.MAXIMAL_PASSIVE + 1 - self.peace_counter
        MOVE = None
        BEST_SCORE = -1000000
        if moves:
            liczba_parti = (int)(10000 / (ile) / len(moves))
            if (ile % 2 == 0):
                ile += 1
            for move in moves:
                best_score = -100000
                for lp in range(liczba_parti):
                    score = 0
                    B = copy.deepcopy(self)
                    B.do_move(move)
                    p = 1 - player
                    for i in range(ile):
                        m = B.random_agent(p)
                        B.do_move(m)
                        p = 1 - p
                        score = max(score, B.evaluate(player))
                    best_score = max(best_score, score)
                if BEST_SCORE < best_score:
                    BEST_SCORE = best_score
                    MOVE = move
            return MOVE
        else:
            return None
    
    def smart_agent(self, player):
        def alphabeta(node, depth, alpha, beta, p):
            if (depth == 0 or node.victory(p) == True or len(node.moves(p)) == 0):
                return node.evaluate(player)
            if p == 0:
                value = -1000000
                for m in node.moves(p):
                    B = copy.deepcopy(node)
                    B.do_move(m)
                    value = max(value, alphabeta(B, depth - 1, alpha, beta, 1 - p))
                    if (value >= beta):
                        break
                    alpha = max(alpha, value)
                    return value
            else:
                value = 1000000
                for m in node.moves(p):
                    B = copy.deepcopy(node)
                    B.do_move(m)
                    value = min(value, alphabeta(B, depth - 1, alpha, beta, 1 - p))
                    if (value <= alpha):
                        break
                    beta = min(beta, value)
                    return value
    
        najlepszy_ruch = None
        koszt_ruchu = -1000000

        for m in self.moves(player):
            B = copy.deepcopy(self)
            B.do_move(m)
            value = alphabeta(B, 3, -1000000, 1000000, 1 - player)
            if (value >= koszt_ruchu):
                najlepszy_ruch = m
                koszt_ruchu = value
        return najlepszy_ruch
                


wynik = 0
all = 0
tury = 0
for i in range(100):
    Board = Jungle()
    player = 0
    while True:
        if (player == 0):
            move = Board.smart_agent(player)
            Board.do_move(move)
        else:
            move = Board.smart_random_agent(player)
            Board.do_move(move)
                
        if (Board.victory(player) == True):
            if (player == 0):
                wynik += 1
            break
        player = 1 - player
    Board.draw()
    print(wynik, i + 1)


