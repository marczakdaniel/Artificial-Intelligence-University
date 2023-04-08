import random

def gen_row(w, s):
    def gen_seg(o, sp):
        if not o:
            return [[0] * sp]
        return [[0] * x + o[0] + tail
                for x in range(1, sp - len(o) + 2)
                for tail in gen_seg(o[1:], sp - x)]
 
    return [x[1:] for x in gen_seg([[1] * i for i in s], w + 1 - sum(s))]

def tworz_losowy_obrazek():
    o = []
    for i in range(wiersze):
        o.append([])
        for j in range(kolumny):
            o[i].append(random.randint(0, 1))
    return o


def zamiana(i, j):
    global obrazek
    if (obrazek[i][j] == 0):
        obrazek[i][j] = 1
    else:
        obrazek[i][j] = 0

def opt_dist(wiersz, D, j):
    wynik1 = len(wiersz)

    poprawne = gen_row(len(wiersz), D)
    for p in poprawne:
        ile = 0
        for i in range(len(p)):
            if (p[i] != wiersz[i]):
                ile += 1
        if (ile < wynik1):
            wynik1 = ile
        if (wynik1 == 0):
            break
    
    wynik2 = len(wiersz)
    if (wiersz[j] == 0):
        wiersz[j] = 1
    else:
        wiersz[j] = 0

    for p in poprawne:
        ile = 0
        for i in range(len(p)):
            if (p[i] != wiersz[i]):
                ile += 1
        if (ile < wynik2):
            wynik2 = ile
        if (wynik2 == 0):
            break
    return wynik1, wynik2

def zly_wiersz(wiersz, D):
    i = 0
    O = []
    while i < len(wiersz):
        if (wiersz[i] == 1):
            dod = 1
            i += 1
            while (i < len(wiersz) and wiersz[i] == 1):
                dod += 1
                i += 1
            O.append(dod)
        i += 1
    if (O == D):
        return False
    #if (opt_dist(wiersz, D) != 0):
    #    return True
    return True


def losowy_zly_wiersz():
    global obrazek
    zle_w = []
    for i in range(wiersze):
        if zly_wiersz(obrazek[i], D_wiersze[i]):
            zle_w.append(i)
    if len(zle_w) == 0:
        return -1
    return random.choice(zle_w)

def kolumna_na_wiersz(j):
    odp = []
    for i in range(wiersze):
        odp.append(obrazek[i][j])
    return odp

def najlepsze_dopasowanie(i):
    w = obrazek[i]
    k = []
    min_dop = 0
    j_dop = -1
    for j in range(kolumny):
        k = kolumna_na_wiersz(j)

        wier1, wier2 = opt_dist(w, D_wiersze[i], j)
        kol1, kol2 = opt_dist(k, D_kolumny[j], i)
        przed_dop = wier1 + kol1
        
        dop = wier2 + kol2
        if (min_dop < przed_dop - dop):
            min_dop = dop
            j_dop = j
        if (w[j] == 0):
            w[j] = 1
        else:
            w[j] = 0
    return j_dop


def rozwiazywanie():
    for i in range(wiersze*kolumny*100):
        w = losowy_zly_wiersz()
        if (w == -1):
            return True
        if random.randint(1, 100) <= 25:
            zamiana(random.randint(0, wiersze-1), random.randint(0,kolumny-1))
        else:
            k = najlepsze_dopasowanie(w)
            zamiana(w, k)
    return False

def sprawdzanie_kolumn():
    for j in range(kolumny):
        k = kolumna_na_wiersz(j)
        if (zly_wiersz(k, D_kolumny[j]) == True):
            return False
    return True

def sprawdzanie_wierszy():
    for i in range(wiersze):
        if (zly_wiersz(obrazek[i], D_wiersze[i]) == True):
            return False
    return True




plik = open("zad_input.txt", "r").read().split("\n")
wk = plik[0].split(" ")
global wiersze, kolumny 
wiersze = eval(wk[0])
kolumny = eval(wk[1])
global D_wiersze 
D_wiersze = []
for x in plik[1:wiersze+1]:
    i = x.split(" ")
    nowy = []
    for a in i:
        nowy.append(eval(a))
    D_wiersze.append(nowy)

global D_kolumny 
D_kolumny = []
for x in plik[wiersze+1:(wiersze+kolumny+1)]:
    i = x.split(" ")
    nowy = []
    for a in i:
        nowy.append(eval(a))
    D_kolumny.append(nowy)

global obrazek

obrazek = tworz_losowy_obrazek()
wynik = rozwiazywanie()
while (wynik != True) or (sprawdzanie_kolumn() != True):
    obrazek = tworz_losowy_obrazek()
    wynik = rozwiazywanie()

wypis = open("zad_output.txt", "w")
for i in obrazek:
    for x in i:
        if x == 1:
            wypis.write("#")
        else:
            wypis.write(".")
    wypis.write("\n")

wypis.close()