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

poker_F = 0
kareta_F = 0
full_F = 0
kolor_F = 0
strit_F = 0
trojka_F = 0
dwie_pary_F = 0
para_F = 0

poker_B = 0
kareta_B = 0
full_B = 0
kolor_B = 0
strit_B = 0
trojka_B = 0
dwie_pary_B = 0
para_B = 0

for k1 in range(len(zbior_B) - 4):
    for k2 in range(k1 + 1, len(zbior_B) - 3):
        for k3 in range(k2 + 1, len(zbior_B) - 2):
            for k4 in range(k3 + 1, len(zbior_B) - 1):
                for k5 in range(k4 + 1, len(zbior_B)):
                    talia = [zbior_B[k1], zbior_B[k2], zbior_B[k3], zbior_B[k4], zbior_B[k5]]
                    if czy_poker(talia):
                        poker_B += 1
                    elif czy_kareta(talia):
                        kareta_B += 1
                    elif czy_full(talia):
                        full_B += 1
                    elif czy_kolor(talia):
                        kolor_B += 1
                    elif czy_strit(talia):
                        strit_B += 1
                    elif czy_trojka(talia):
                        trojka_B += 1
                    elif czy_dwie_pary(talia):
                        dwie_pary_B += 1
                    elif czy_para(talia):
                        para_B += 1

for k1 in range(len(zbior_F) - 4):
    for k2 in range(k1 + 1, len(zbior_F) - 3):
        for k3 in range(k2 + 1, len(zbior_F) - 2):
            for k4 in range(k3 + 1, len(zbior_F) - 1):
                for k5 in range(k4 + 1, len(zbior_F)):
                    talia = [zbior_F[k1], zbior_F[k2], zbior_F[k3], zbior_F[k4], zbior_F[k5]]
                    if czy_poker(talia):
                        poker_F += 1
                    elif czy_kareta(talia):
                        kareta_F += 1
                    elif czy_full(talia):
                        full_F += 1
                    elif czy_kolor(talia):
                        kolor_F += 1
                    elif czy_strit(talia):
                        strit_F += 1
                    elif czy_trojka(talia):
                        trojka_F += 1
                    elif czy_dwie_pary(talia):
                        dwie_pary_F += 1
                    elif czy_para(talia):
                        para_F += 1

ile_F = [poker_F, kareta_F, full_F, kolor_F, strit_F, trojka_F, dwie_pary_F, para_F]
ile_B = [poker_B, kareta_B, full_B, kolor_B, strit_B, trojka_B, dwie_pary_B, para_B]

print(ile_F)
print(ile_B)

mianownik = 1646701056
licznik = 0
for i in range(len(ile_B)):
    for j in range(i + 1, len(ile_F)):
        licznik += ile_B[i] * ile_F[j]

print(licznik)
print(licznik/mianownik)
