from itertools import permutations

#def zbiory(D, dl):
#    suma = 0;
#    for i in D:
#        suma += i
#    ile_puste = dl - suma - len(D) + 1
#    zbior = []
#    for i in range(1, ile_puste+1):
#        for x in range(len(D) - 1):
#            zbior.append(i)
#    perm = list(permutations(zbior, len(D) - 1))#
#    ile_puste = dl - suma - len(D)

#    print(perm)

def gen_row(w, s):
    """Create all patterns of a row or col that match given runs."""
    def gen_seg(o, sp):
        if not o:
            return [[0] * sp]
        return [[0] * x + o[0] + tail
                for x in range(1, sp - len(o) + 2)
                for tail in gen_seg(o[1:], sp - x)]
 
    return [x[1:] for x in gen_seg([[1] * i for i in s], w + 1 - sum(s))]

#print(gen_row(10, [1, 3, 2]))

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

print(zly_wiersz([0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1], [3, 1, 2, 2]))