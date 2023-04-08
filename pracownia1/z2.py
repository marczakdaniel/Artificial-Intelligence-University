plik = open('words_for_ai1.txt', 'r')
zawartosc = plik.readlines()
slownik = {''}
for x in zawartosc:
    slownik.add(x.replace("\n", ""))
plik.close()
max_l = len(max(slownik, key=len))



#def podzial_wiersza(wiersz, wyjscie='')
#    if wiersz is '':
#        print(wyjscie)
#    
#    for rozmiar in range(1, len(wiersz) + 1):
#        if slowo_w_wlowniku(wiersz[:i]):
#            podzial_wiersza(wiersz[i:], wyjscie + ' ' + wiersz[:i])




#def podzial_wiersza(wiersz):
#    dp = [[0] * len(wiersz)] * len(wiersz)
#    wartosc = [[0] * len(wiersz)] * len(wiersz)
#    for rozmiar in range(1, len(wiersz) + 1):
#        for poc in range(0, len(wiersz) - rozmiar):
#            if slowo_w_slowniku(wiersz[poc:poc+rozmiar]):
#                dp[poc][poc+rozmiar-1] = 1
#            else:
#                for i in range(1, rozmiar):

def najwiekszy(zbior):
    wynik = ''
    wartosc = 0
    for i in zbior:
        wartosc_i = 0
        slowa = i.split()
        for j in slowa:
            wartosc_i += (len(j) * len(j))
        if wartosc_i > wartosc:
            wynik = i
            wartosc = wartosc_i
    return wynik

def podzial_wiersza(wiersz):
    pamiec = {}

    def podciagi(sub):
        if sub in pamiec:
            return pamiec[sub]
        result = []
        if sub in slownik:
            pamiec[sub] = [sub]
            return pamiec[sub]
        for i in range(max_l, 0, -1):
            if sub[:i] in slownik:
                    reszta_slowa = podciagi(sub[i:])
                    for j in reszta_slowa:
                        result.append(sub[:i] + ' ' + j)
                    result = [najwiekszy(result)]
        pamiec[sub] = [najwiekszy(result)]
        return pamiec[sub]

    return podciagi(wiersz)





plik = open('zad2_input.txt', 'r')
wypis = open('zad2_output.txt', 'w')
zapytanie = plik.readlines()
linie = []
for x in zapytanie:
    linie.append("".join(x.split()))


for x in linie:
    a = podzial_wiersza(x)
    wypis.write(a[0])
    wypis.write("\n")
plik.close()
wypis.close()