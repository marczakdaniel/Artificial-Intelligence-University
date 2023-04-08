import heapq
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

def odl(i):
    minimum = 0
    for j in punkty_koncowe:
        odle = abs(j[0] - i[0]) + abs(j[1] - i[0])
        if odle < minimum:
            minimum = odle
    return minimum


zapamietywanie = []
for i in range(wiersze):
    tym = []
    for j in range(kolumny):
        tym.append(odl((i, j)))
    zapamietywanie.append(tym)

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

def h(pozycja):
    suma_minimum = 0
    for i in pozycja:
        x = i[0]
        y = i[1]
        #suma_minimum += zapamietywanie[x][y]
        if (suma_minimum < zapamietywanie[x][y]):
            suma_minimum = zapamietywanie[x][y]
    return suma_minimum

def ASTAR(pozycja):
    odwiedzone = set()
    Kopiec = []
    heapq.heappush(Kopiec, (h(pozycja), (pozycja, [])))
    odwiedzone.add(tuple(pozycja))
    while True:
        tym = heapq.heappop(Kopiec)
        t_pozycja = tym[1][0]
        t_ruchy = tym[1][1]
        if (czy_mamy_wynik(t_pozycja)):
            wyjscie = open("zad_output.txt", "w")
            wyjscie.write(zamiana_ruchow(t_ruchy))
            wyjscie.close()
            break
        for r in range(1, 5):
            nowe_pozycje = przesuniecie(t_pozycja, r)
            if (tuple(nowe_pozycje) not in odwiedzone):
                odwiedzone.add(tuple(nowe_pozycje))
                heapq.heappush(Kopiec, (h(nowe_pozycje) + len(t_ruchy),(nowe_pozycje, t_ruchy + [r])))


ASTAR(punkty_startowe)        
plik.close()