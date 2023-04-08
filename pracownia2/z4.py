import itertools
from queue import Queue
plik = open('zad_input.txt', 'r')
zapytanie = plik.readlines()
linie = []
for x in zapytanie:
    linie.append(x.replace("\n", ""))

kolumny = len(linie[0])
wiersze = len(linie)

plansza = []
punkty_startowe = set()
punkty_koncowe = set()
sciany = set()

for i in range(wiersze):
    for j in range(kolumny):
        if (linie[i][j] == '#'):
            sciany.add((i, j))
        elif (linie[i][j] == "G"):
            punkty_koncowe.add((i, j))
        elif (linie[i][j] == "S"):
            punkty_startowe.add((i, j))
        elif (linie[i][j] == "B"):
            punkty_startowe.add((i, j))
            punkty_koncowe.add((i, j))

# kierunki:
#    1
#   2 3
#    4

def przesuniecie(pozycje, kierunek):
    nowe_pozycje = set()
    for poz in pozycje:
        n_poz_x = poz[0]
        n_poz_y = poz[1]
        if (kierunek == 1):
            n_poz_x = n_poz_x - 1
        elif (kierunek == 2):
            n_poz_y = n_poz_y - 1
        elif (kierunek == 3):
            n_poz_y = n_poz_y + 1
        elif (kierunek == 4):
            n_poz_x = n_poz_x + 1
        if ((n_poz_x, n_poz_y) not in sciany):
            nowe_pozycje.add((n_poz_x, n_poz_y))
        else:
            nowe_pozycje.add(poz)
    return nowe_pozycje

def czy_mamy_wynik(pozycje):
    for poz in pozycje:
        if (poz not in punkty_koncowe):
            return False
    return True

def zamiana_ruchow(ruchy):
    wynik = ""
    for i in ruchy:
        if (i == 1):
            wynik = wynik + "U"
        elif (i == 2):
            wynik = wynik + "L"
        elif (i == 3):
            wynik = wynik + "R"
        elif (i == 4):
            wynik = wynik + "D"
    return wynik

def zachlanne():
    najlepszy_start = []
    najlepsze_ruchy = []
    kolejnosc = list(itertools.permutations([1, 2, 3, 4]))
    ile = 10
    ile_ruchow = len(punkty_startowe)
    for k in range(len(kolejnosc)):
        t_ruchy = []
        for i in range(4):
            for j in range(ile):
                t_ruchy.append(kolejnosc[k][i])
        t_start = punkty_startowe.copy()
        for i in t_ruchy:
            t_start = przesuniecie(t_start, i)
        if (len(t_start) < ile_ruchow):
            ile_ruchow = len(t_start)
            najlepszy_start = t_start
            najlepsze_ruchy = t_ruchy
    return najlepszy_start, najlepsze_ruchy

def BFS(pozycja, ruchy):
    odwiedzone = set()
    Kolejka = Queue(maxsize=0)
    Kolejka.put((pozycja, ruchy))
    odwiedzone.add(str(pozycja))
    dlugosc = len(pozycja)

    while Kolejka.empty() == False:
        tym = Kolejka.get()
        t_pozycja = tym[0]
        t_ruchy = tym[1]
        if czy_mamy_wynik(t_pozycja):
            wyjscie = open("zad_output.txt", "w")
            wyjscie.write(zamiana_ruchow(t_ruchy))
            wyjscie.close()
            break
        for r in range(1, 5):
            nowe_pozycje = przesuniecie(t_pozycja, r)
            if (str(nowe_pozycje) not in odwiedzone):
                if (len(nowe_pozycje) < dlugosc):
                    dlugosc = len(nowe_pozycje)
                    Kolejka = Queue(maxsize=0)
                    odwiedzone = set()
                odwiedzone.add(str(nowe_pozycje))
                Kolejka.put((nowe_pozycje, t_ruchy + [r]))

pozycje, ruchy = zachlanne()
BFS(pozycje, ruchy)
        
plik.close()

