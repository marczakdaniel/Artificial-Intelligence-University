def opt_dist(lista, D):
    if len(lista) < D:
        return -1
    liczba_jedynek = 0
    for i in lista:
        if i == 1:
            liczba_jedynek = liczba_jedynek + 1
    wynik = len(lista)
    ile = 0
    for i in range(0, D):
        if lista[i] == 1:
            ile = ile + 1
    wynik = min(wynik, liczba_jedynek - 2 * ile + D)
    for i in range(D, len(lista)):
        if lista[i] == 1:
            ile = ile + 1
        if lista[i - D] == 1:
            ile = ile - 1
        wynik = min(wynik, liczba_jedynek - 2 * ile + D)
    return wynik

    
plik = open('zad4_input.txt', 'r')
wypis = open('zad4_output.txt', 'w')
for linia in plik:
    ciag, D = linia.split()
    lista = []
    for i in ciag:
        lista.append(int(i))
    wypis.write(str(opt_dist(lista, int(D))))
    wypis.write("\n")

plik.close()
wypis.close()



