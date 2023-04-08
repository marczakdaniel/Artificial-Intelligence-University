import heapq
from queue import Queue
plik = open('zad_input.txt', 'r')
zapytanie = plik.readlines()
linie = []
for x in zapytanie:
    linie.append(x.replace("\n", ""))

kolumny = len(linie[0])
wiersze = len(linie)

punkty_startowe = set()
punkty_koncowe = set()
sciany = set()




ODLEGLOSC = {}
for i in range(wiersze):
    for j in range(kolumny):
        ODLEGLOSC[(i, j)] = 10000000

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

def BFS(pozycja):
    odwiedzone = set()
    Kolejka = Queue(maxsize=0)
    Kolejka.put((pozycja, 0))
    odwiedzone.add(pozycja)
    while Kolejka.empty() == False:
        tym = Kolejka.get()
        poz_t = tym[0]
        odl_t = tym[1]
        if (poz_t in punkty_koncowe):
            ODLEGLOSC[pozycja] = min(ODLEGLOSC[pozycja], odl_t)
        for i in range(2):  
            for j in range(-1, 2, 2):
                if (i == 1):
                    nowa_pozycja = (poz_t[0] + j, poz_t[1])
                else:
                    nowa_pozycja = (poz_t[0], poz_t[1] + j)
                if (nowa_pozycja not in odwiedzone and nowa_pozycja not in sciany):
                    odwiedzone.add(nowa_pozycja)
                    Kolejka.put((nowa_pozycja, odl_t + 1))

        #odl += 1
        #for i in range(-1, 2, 1):
        #    for j in range(-1, 2, 1):
        #        if (i != j and (i == 0 or j == 0)):
        #            x = tym[0] + i
        #            y = tym[1] + j
        #            if (str((x, y)) not in odwiedzone and (x, y) not in sciany):
        #                odwiedzone.add(str((x, y)))
        #                Kolejka.put((x, y))
        #                if (ODLEGLOSC[(x, y)] > odl):
        #                    ODLEGLOSC[(x, y)] = odl
    #print(odl)
                

def wylicz_ODLEGLOSC():
    for i in range(wiersze):
        for j in range(kolumny):
            if (i, j) not in sciany:
                BFS((i, j))

def h(pozycja):
    maks = 0
    for i in pozycja:
        x = i[0]
        y = i[1]
        maks = max(maks, ODLEGLOSC[(x, y)])

    return maks

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
            #print(len(t_ruchy))
            #print(zamiana_ruchow(t_ruchy))
            wyjscie = open("zad_output.txt", "w")
            wyjscie.write(zamiana_ruchow(t_ruchy))
            wyjscie.close()
            break
        #for r in range(1, 5):
        #    nowe_pozycje = przesuniecie(t_pozycja, r)
        #    if (tuple(nowe_pozycje) not in odwiedzone):
        #        odwiedzone.add(tuple(nowe_pozycje))
        #        heapq.heappush(Kopiec, (h(nowe_pozycje) + len(t_ruchy) + 1,(nowe_pozycje, t_ruchy + [r])))
        t = [2, 1, 3, 4]
        for r in t:
            nowe_pozycje = przesuniecie(t_pozycja, r)
            if (tuple(nowe_pozycje) not in odwiedzone):
                odwiedzone.add(tuple(nowe_pozycje))
                heapq.heappush(Kopiec, (h(nowe_pozycje) + len(t_ruchy) + 1,(nowe_pozycje, t_ruchy + [r])))
        

wylicz_ODLEGLOSC()
ASTAR(punkty_startowe)        
plik.close()

#RRUUULDDRR
#DLULUUULU

#LLLLLURURRRRRRRRDDRLLLLL
#LLLLLUURRRRRRRRRDDLLLLL

#DRDLDLLLULULLLLLLLLLLLLUUUULURUUUUURRRRRRDDURRURRRRRRRRR
#DRDDLULLULLLLLLLLLLLLLURULULUUUUURRRURRRURDRRRRURRRRRRR