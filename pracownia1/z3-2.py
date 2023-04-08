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



def sort_po_num(karta):
    return karta[0]

def losowanie_F(zbio_F):
    random_card = random.choice(zbio_F)
    return random_card

def losowanie_B(zbio_B):
    random_card = random.choice(zbio_B)
    return random_card

def losowanie_talia_F(zbio_F):
    talia = random.sample(zbio_F, 5)
    return talia

def losowanie_talia_B(zbio_B):
    talia = random.sample(zbio_B, 5)
    return talia

def czy_poker(t):
    t.sort(key=sort_po_num)
    if t[0][1] == t[1][1] == t[2][1] == t[3][1] == t[4][1]:
        if t[0][0] == (t[1][0] - 1) == (t[2][0] - 2) == (t[3][0] - 3) == (t[4][0] - 4):
            return True
    return False
        

def czy_kareta(t):
    t.sort(key=sort_po_num)
    if (t[0][0] == t[1][0] == t[2][0] == t[3][0]) or (t[1][0] == t[2][0] == t[3][0] == t[4][0]):
        return True
    return False

def czy_full(t):
    t.sort(key=sort_po_num)
    if ((t[0][0] == t[1][0] == t[2][0]) and (t[3][0] == t[4][0])) or ((t[2][0] == t[3][0] == t[4][0]) and (t[0][0] == t[1][0])):
        return True
    return False

def czy_kolor(t):
    if t[0][1] == t[1][1] == t[2][1] == t[3][1] == t[4][1]:
        return True
    return False

def czy_strit(t):
    t.sort(key=sort_po_num)
    if t[0][0] == (t[1][0] - 1) == (t[2][0] - 2) == (t[3][0] - 3) == (t[4][0] - 4):
        return True
    return False

def czy_trojka(t):
    t.sort(key=sort_po_num)
    if ((t[0][0] == t[1][0] == t[2][0]) or (t[1][0] == t[2][0] == t[3][0]) or (t[2][0] == t[3][0] == t[4][0])):
        return True
    return False

def czy_dwie_pary(t):
    t.sort(key=sort_po_num)
    i = 0
    par = 0
    while i < 4:
        if (t[i][0] == t[i+1][0]):
            par += 1
            i += 1
        i += 1
    if (par == 2):
        return True
    return False


def czy_para(t):
    t.sort(key=sort_po_num)
    i = 0
    par = 0
    while i < 4:
        if (t[i][0] == t[i+1][0]):
            par += 1
            i += 1
        i += 1
    if (par == 1):
        return True
    return False

def moc_talia(t):
    moc = 10
    if czy_poker(t):
        moc = 2
    elif czy_kareta(t):
        moc = 3
    elif czy_full(t):
        moc = 4
    elif czy_kolor(t):
        moc = 5
    elif czy_strit(t):
        moc = 6
    elif czy_trojka(t):
        moc = 7
    elif czy_dwie_pary(t):
        moc = 8
    elif czy_para(t):
        moc = 9
    return moc

def wygrana_B(talia_F, talia_B):
    moc_F = moc_talia(talia_F)
    moc_B = moc_talia(talia_B)

    if (moc_F > moc_B):
        return True
    else:
        return False


def prawdopodobienstwo(ile, zbio_F, zbio_B):
    ile_B = 0
    for i in range(0, ile):
        b = losowanie_talia_B(zbio_B)
        f = losowanie_talia_F(zbio_F)
        if wygrana_B(f, b):
            ile_B = ile_B + 1

    return ile_B / ile
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
                p = prawdopodobienstwo(100000, zbior_F, z)
                if p >= 0.5:
                    return [p, z]
        
    return [p, z]

#print(najlepsza_talia(12))
# a = [['3', 'PIK'], ['3', 'KIER'], ['8', 'KIER'], ['9', 'PIK'], ['9', 'KIER'], ['3', 'KARO'], ['8', 'TREFL'], ['8', 'PIK'], ['9', 'KARO']] 56%
a = [['2', 'PIK'], ['2', 'KIER'], ['10', 'TREFL'], ['3', 'KIER'], ['5', 'KIER'], ['3', 'TREFL'], ['2', 'TREFL'], ['3', 'PIK'], ['3', 'KARO'], ['2', 'KARO']] #56%
b = [['3', 'TREFL'], ['6', 'TREFL'], ['8', 'TREFL'], ['10', 'PIK'], ['6', 'KIER'], ['10', 'KIER'], ['10', 'TREFL'], ['8', 'PIK'], ['10', 'KARO'], ['8', 'KIER'], ['8', 'KARO']] #49.37
#c = [['10', 'TREFL'], ['10', 'KARO'], ['10', 'KIER'], ['10', 'PIK'], ['9', 'TREFL'], ['9', 'KARO'], ['9', 'KIER'], ['9', 'PIK'], ['8', 'TREFL'], ['8', 'KARO'], ['8', 'KIER'], ['8', 'PIK']] # 56.36
c = [[10, 1], [10, 2], [10, 3], [10, 4], [9, 1], [9, 2], [9, 3], [9, 4], [8, 1], [8, 2], [8, 3], [8, 4]] # 56.36

#c = [['8', 'TREFL'], ['9', 'KARO'], ['10', 'TREFL'], ['10', 'KARO'], ['9', 'KIER'], ['8', 'KARO'], ['8', 'PIK'], ['10', 'KIER'], ['7', 'PIK'], ['10', 'PIK'], ['8', 'KIER']]
#d = [['8', 'TREFL'], ['9', 'KARO'], ['10', 'TREFL'], ['10', 'KARO'], ['9', 'KIER'], ['8', 'KARO'], ['8', 'PIK'], ['10', 'KIER'], ['7', 'PIK'], ['10', 'PIK'], ['8', 'KIER']]
print(prawdopodobienstwo(100000, zbior_F, zbior_B))
#print(prawdopodobienstwo(100000, zbior_F, c))
