import random

plik = open('words_for_ai1.txt', 'r')
zawartosc = plik.readlines()
slownik = {''}
for x in zawartosc:
    slownik.add(x.replace("\n", ""))
plik.close()
max_l = len(max(slownik, key=len))

def podzial_wiersza(wiersz):
    czy_w_slowniku = [0 for x in range(len(wiersz) + 1)]
    
    poczatek_slowa = [ [] for x in range(len(wiersz) + 1)]

    for i in range(0, len(wiersz)):
        if wiersz[:i+1] in slownik:
            czy_w_slowniku[i] = 1
            poczatek_slowa[i].append(0)

    
    for rozmiar in range(1, len(wiersz)):
        for i in range(0, rozmiar):
            if (czy_w_slowniku[i] == 1) and (wiersz[i+1:rozmiar+1] in slownik):
                czy_w_slowniku[rozmiar] = 1
                poczatek_slowa[rozmiar].append(i+1)

    moc_slowa = [ [0, ''] for x in range(len(wiersz))]
    for i in range(0, len(wiersz)):
        for p in poczatek_slowa[i]:
            moc = random.randint(0,10000)
            if (moc > moc_slowa[i][0]):
                moc_slowa[i][0] = moc
                slowo = ''
                if (p != 0):
                    slowo = moc_slowa[p-1][1] + ' ' + wiersz[p:i+1]
                else:
                    slowo = wiersz[p:i+1]
                moc_slowa[i][1] = slowo
    return moc_slowa[len(wiersz) -1][1]


plik = open('pan_tadeusz_bez_spacji.txt', 'r')
wypis = open('pan_tadeusz_losowy.txt', 'w')
zapytanie = plik.readlines()
linie = []
for x in zapytanie:
    linie.append("".join(x.split()))


for x in linie:
    wypis.write(podzial_wiersza(x))
    wypis.write("\n")