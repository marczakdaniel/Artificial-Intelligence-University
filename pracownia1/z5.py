import random


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

def opt_dist(wiersz, D):
    liczba_jedynek = 0
    for i in wiersz:
        if i == 1:
            liczba_jedynek = liczba_jedynek + 1
    wynik = len(wiersz)
    ile = 0
    for i in range(0, D):
        if wiersz[i] == 1:
            ile = ile + 1
    wynik = min(wynik, liczba_jedynek - 2 * ile + D)
    for i in range(D, len(wiersz)):
        if wiersz[i] == 1:
            ile = ile + 1
        if wiersz[i - D] == 1:
            ile = ile - 1
        wynik = min(wynik, liczba_jedynek - 2 * ile + D)
    return wynik

def zly_wiersz(wiersz, D):
    if (opt_dist(wiersz, D) != 0):
        return True
    return False


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
        przed_dop = opt_dist(w, D_wiersze[i]) + opt_dist(k, D_kolumny[j])
        if (w[j] == 0):
            w[j] = 1
        else:
            w[j] = 0
        if (k[i] == 0):
            k[i] = 1
        else:
            k[i] = 0
        dop = opt_dist(w, D_wiersze[i]) + opt_dist(k, D_kolumny[j])
        if (min_dop < przed_dop - dop):
            min_dop = dop
            j_dop = j
        if (w[j] == 0):
            w[j] = 1
        else:
            w[j] = 0
    return j_dop


def rozwiazywanie():
    for i in range(wiersze*kolumny*10):
        w = losowy_zly_wiersz()
        if (w == -1):
            return True
        if random.randint(1, 100) <= 20:
            zamiana(random.randint(0, wiersze-1), random.randint(0,kolumny-1))
        else:
            k = najlepsze_dopasowanie(w)
            zamiana(w, k)
    return False

def sprawdzanie_kolumn():
    for j in range(kolumny):
        k = kolumna_na_wiersz(j)
        if (opt_dist(k, D_kolumny[j]) != 0):
            return False
    return True

def sprawdzanie_wierszy():
    for i in range(wiersze):
        if (opt_dist(obrazek[i], D_wiersze[i]) != 0):
            return False
    return True




plik = open("zad5_input.txt", "r").read().split("\n")
wk = plik[0].split(" ")
global wiersze, kolumny 
wiersze = eval(wk[0])
kolumny = eval(wk[1])
global D_wiersze 
D_wiersze = []
for x in plik[1:wiersze+1]:
    D_wiersze.append(eval(x))
global D_kolumny 
D_kolumny = []
for x in plik[wiersze+1:(wiersze+kolumny+1)]:
    D_kolumny.append(eval(x))

global obrazek

obrazek = tworz_losowy_obrazek()
wynik = rozwiazywanie()
while (wynik != True) or (sprawdzanie_kolumn() != True):
    obrazek = tworz_losowy_obrazek()
    wynik = rozwiazywanie()

wypis = open("zad5_output.txt", "w")
for i in obrazek:
    for x in i:
        if x == 1:
            wypis.write("#")
        else:
            wypis.write(".")
    wypis.write("\n")

wypis.close()

