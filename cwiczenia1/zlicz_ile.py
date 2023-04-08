plik = open('tadek3.txt', 'r')
zawartosc = plik.readlines()
pan_tadeusz_O = []
for x in zawartosc:
    pan_tadeusz_O.append(x.replace("\n", ""))
plik.close()

plik = open('pan_tadeusz_losowy.txt', 'r')
zawartosc = plik.readlines()
pan_tadeusz_L = []
for x in zawartosc:
    pan_tadeusz_L.append(x.replace("\n", ""))
plik.close()

plik = open('pan_tadeusz_maksymalny.txt', 'r')
zawartosc = plik.readlines()
pan_tadeusz_M = []
for x in zawartosc:
    pan_tadeusz_M.append(x.replace("\n", ""))
plik.close()

wynik_M = 0
wynik_L = 0
ile_wersow = 0
for i in range(len(pan_tadeusz_O)):
    czy_M = True
    czy_L = True
    wers_O = pan_tadeusz_O[i].split()
    wers_L = pan_tadeusz_L[i].split()
    wers_M = pan_tadeusz_M[i].split()

    if (len(wers_O) == len(wers_L)):
        for x in range(len(wers_O)):
            if (wers_O[x] != wers_L[x]):
                czy_L = False
        if (czy_L == True):
            wynik_L += 1

    if (len(wers_O) == len(wers_M)):
        for x in range(len(wers_O)):
            if (wers_O[x] != wers_M[x]):
                czy_M = False
        if (czy_M == True):
            wynik_M += 1
    
    ile_wersow += 1

print(wynik_L)
print(wynik_L/ile_wersow)
print(wynik_M)
print(wynik_M/ile_wersow)


