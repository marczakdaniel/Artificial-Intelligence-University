from re import X


PLANSZA = [['.' for x in range(70)] for y in range(70)]

ZNAKI = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P',
    17: 'Q',
    18: 'R',
    19: 'S',
    20: 'T',
    21: 'U',
    22: 'V',
    23: 'W',
    24: 'X'
}

UZYTE = [0 for x in range(24)]

def ile_pustych():
    wynik = 0
    for x in range(70):
        for y in range(70):
            if PLANSZA[x][y] == '.':
                wynik += 1
    return wynik

def rysuj(ile, x, y, znak):
    if x + ile - 1 >= 70 or y + ile - 1 >= 70:
        return False
    for i in range(ile):
        for j in range(ile):
            if (PLANSZA[x+i][y+j] != '.'):
                return False
            PLANSZA[x+i][y+j] = znak
    return True

def czy_puste(ile, x, y):
    if x + ile - 1 >= 70 or y + ile - 1 >= 70:
        return False
    for i in range(ile):
        for j in range(ile):
            if (PLANSZA[x+i][y+j] != '.'):
                return False
    return True

def najwieksze(X, Y):
    for x in range(24):
        if (UZYTE[23 - x] == 0 and czy_puste(24 - x, X, Y)):
            return 24 - x
    return 0

def RYSUJ_PLANSZE():
    for i in range(70):
        x = ""
        for j in range(70):
            x = x + PLANSZA[i][j]
        print(x)
def zachlannie():
    x = 0
    y = 0
    while(x < 70):
        y = 0
        naj = 0
        while(y < 70):
            ile = najwieksze(x, y)
            if (ile == 0):
                break
            if (y == 0):
                naj = ile
            rysuj(ile, x, y, ZNAKI[ile])
            UZYTE[ile - 1] = 1
            y += ile
        x += naj
zachlannie()
RYSUJ_PLANSZE()
print(ile_pustych())
suma = 0
for i in range(24):
    if (UZYTE[i] == 0):
        print(i + 1, ZNAKI[i + 1])
        suma += (i + 1) * (i + 1)
print(suma)
# Przeszukiwanie zachłanne 
# - wykład 2 - zajmujmemy się tylko obecnym stanem, rozwijamy ten węzeł który wydaje się najbliższy rozwiązaniu
# Haurystyka: First Fail 
# - wykład 4 - zajmujemy się najpierw największymi kwadratami, wymieramy tę zmienną która jest najtrudniejsza


