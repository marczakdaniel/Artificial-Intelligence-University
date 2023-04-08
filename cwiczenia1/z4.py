import random

all_card_points = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
all_card_signs = [1, 2, 3, 4]
card_points_B = [2, 3, 4, 5, 6, 7, 8, 9, 10]
card_points_F = [11, 12, 13, 14]
zbior_F = []
zbior_B = []
zbior_C = []

for i in card_points_F:
    for j in all_card_signs:
        zbior_F.append([i, j])

for i in card_points_B:
    for j in all_card_signs:
        zbior_B.append([i, j])

for i in all_card_points:
    for j in all_card_signs:
        zbior_C.append([i, j])


def losowanie_F(zbio_F):
    random_card = random.choice(zbio_F)
    return random_card

def losowanie_B(zbio_B):
    random_card = random.choice(zbio_B)
    return random_card

def losowanie_talia_F(zbio_F):
    talia = []
    for i in range(5):
        talia.append(losowanie_F(zbio_F))
    return talia

def losowanie_talia_B(zbio_B):
    talia = []
    for i in range(5):
        talia.append(losowanie_B(zbio_B))
    return talia

def zamiana_na_liczby(talia):
    wynik = []
    for i in talia:
        wartosc = i[0]
        a = 0
        if wartosc == 'WALET':
            a = 11
        elif wartosc == 'DAMA':
            a = 12
        elif wartosc == 'KROL':
            a = 13
        elif wartosc == 'AS':
            a = 14
        else:
            a = int(wartosc)
        b = 0
        kolor = i[1]
        if kolor == 'PIK':
            b = 1
        elif kolor == 'KIER':
            b = 2
        elif kolor == 'TREFL':
            b = 3
        elif kolor == 'KARO':
            b = 4
        wynik.append([a, b])
    return wynik

def czy_poker(talia):
    t = zamiana_na_liczby(talia)
    t.sort()
    for i in range(1, 5):
        if (t[i][0] - i != t[0][0]):
            return False
    kolor = t[0][1]
    for i in range(1, 5):
        if (t[i][1] != kolor):
            return False
    return True

def czy_kareta(talia):
    t = zamiana_na_liczby(talia)
    t.sort()
    if (t[0][0] == t[3][0] or t[1][0] == t[4][0]):
        return True
    else:
        return False

def czy_full(talia):
    t = zamiana_na_liczby(talia)
    t.sort()
    if ((t[0][0] == t[2][0] and t[3][0] == t[4][0]) or (t[2][0] == t[4][0] and t[0][0] == t[1][0])):
        return True
    else:
        return False

def czy_kolor(talia):
    t = zamiana_na_liczby(talia)
    t.sort()
    kolor = t[0][1]
    for i in range(1, 5):
        if (t[i][1] != kolor):
            return False
    return True

def czy_strit(talia):
    t = zamiana_na_liczby(talia)
    t.sort()
    for i in range(1, 5):
        if (t[i][0] - i != t[0][0]):
            return False
    return True

def czy_trojka(talia):
    t = zamiana_na_liczby(talia)
    t.sort()
    if (t[0][0] == t[2][0] or t[1][0] == t[3][0] or t[2][0] == t[4][0]):
        return True
    return False

def czy_dwie_pary(talia):
    t = zamiana_na_liczby(talia)
    t.sort()
    wynik = 0
    i = 0
    while (i < 4):
        if (t[i][0] == t[i+1][0]):
            wynik = wynik + 1
            i = i + 1
        i = i + 1
    if (wynik == 2):
        return True
    return False

def czy_para(talia):
    t = zamiana_na_liczby(talia)
    t.sort()
    for i in range(0, 4):
        if (t[i][0] == t[i+1][0]):
            return True
    return False

def moc_talia_F(talia_F):
    moc = 10
    if czy_kareta(talia_F):
        moc = 3
    elif czy_full(talia_F):
        moc = 4
    elif czy_trojka(talia_F):
        moc = 7
    elif czy_dwie_pary(talia_F):
        moc = 8
    elif czy_para(talia_F):
        moc = 9
    return moc

    

def moc_talia_B(talia_B):
    moc = 10
    if czy_poker(talia_B):
        moc = 2
    elif czy_kareta(talia_B):
        moc = 3
    elif czy_full(talia_B):
        moc = 4
    elif czy_kolor(talia_B):
        moc = 5
    elif czy_strit(talia_B):
        moc = 6
    elif czy_trojka(talia_B):
        moc = 7
    elif czy_dwie_pary(talia_B):
        moc = 8
    elif czy_para(talia_B):
        moc = 9
    return moc

def wygrana_F(talia_F, talia_B):
    moc_B = moc_talia_B(talia_B)
    moc_F = moc_talia_F(talia_F)

    if (moc_F <= moc_B):
        return True
    else:
        return False


def prawdopodobienstwo(ile, zbio_F, zbio_B):
    ile_F = 0
    for i in range(0, ile):
        b = losowanie_talia_B(zbio_B)
        f = losowanie_talia_F(zbio_F)
        if wygrana_F(f, b):
            ile_F = ile_F + 1

    return 1.0 - (ile_F / ile)
 
def najlepsza_talia(ile):
    najlepsze = 0
    z =[]
    while (najlepsze < 0.6):
        zbior_B2 = random.sample(zbior_B, ile)
        p = prawdopodobienstwo(1000, zbior_F, zbior_B2)
        if p > najlepsze:
            najlepsze = p
            z = zbior_B2
            print([p, z])
            if p >= 0.47:
                p = prawdopodobienstwo(1000, zbior_F, z)
                if p >= 0.5:
                    return [p, z]
        
    return [p, z]
