import random

global obrazek
global wiersze, kolumny 
global colIx

global mask
global val

def wnioskowanie_wiersze():
    for k in range(len(D_wiersze)):
        w = D_wiersze[k]
        sum = []
        sum.append(0)
        for i in range(len(w)):
            sum.append(sum[i] + w[i])
        for i in range(len(w)):
            sum_left = sum[i]
            sum_right = sum[len(w)] - sum[i + 1]
            sum_left += i
            sum_right += len(w) - i - 1
            free_space = kolumny - sum_left - sum_right
            l_granica = free_space - w[i] + 1 - 1
            p_granica = w[i] - 1
            if (p_granica >= l_granica):
                for pozycja in range(l_granica, p_granica + 1):
                    ktory = pozycja + sum_left
                    obrazek[k] = obrazek[k] | (1 << ktory)
            
def wnioskowanie_kolumny():
    for k in range(len(D_kolumny)):
        w = D_kolumny[k]
        sum = []
        sum.append(0)
        for i in range(len(w)):
            sum.append(sum[i] + w[i])
        for i in range(len(w)):
            sum_left = sum[i]
            sum_right = sum[len(w)] - sum[i + 1]
            sum_left += i
            sum_right += len(w) - i - 1
            free_space = wiersze - sum_left - sum_right
            l_granica = free_space - w[i] + 1 - 1
            p_granica = w[i] - 1
            if (p_granica >= l_granica):
                for pozycja in range(l_granica, p_granica + 1):
                    ktory = pozycja + sum_left
                    obrazek[ktory] = obrazek[ktory] | (1 << k)

def bits(b):
    return (1 << b) - 1

def calcPerms(r, cur, spaces, perm, shift, res):
    if (cur == len(D_wiersze[r])):
        if ((obrazek[r] & perm) == obrazek[r]):
            res.append(perm)
        return
    while (spaces >= 0):
        calcPerms(r, cur+1, spaces, perm | (bits(D_wiersze[r][cur]) << shift), shift + D_wiersze[r][cur]+1, res)
        shift += 1
        spaces -= 1

def updateCols(w):
    ixc = 1
    for c in range(kolumny):
        if w == 0:
            colVal[w][c] = 0
            colIx[w][c] = 0
        else:
            colVal[w][c] = colVal[w-1][c]
            colIx[w][c] = colIx[w-1][c]

        if ((obrazek[w] & ixc) == 0):
            if (w > 0 and colVal[w-1][c] > 0):
                colVal[w][c] = 0
                colIx[w][c] += 1
        else:
            colVal[w][c] += 1
        ixc = ixc << 1

def rowMask(w):
    mask[w] = 0
    val[w] = 0
    if (w == 0):
        return
    ixc = 1
    for c in range(kolumny):
        if (colVal[w-1][c] > 0):
            mask[w] = mask[w] | ixc
            if (D_kolumny[c][colIx[w-1][c]] > colVal[w-1][c]):
                val[w] |= ixc
        elif (colVal[w-1][c] == 0 and colIx[w-1][c] == len(D_kolumny[c])):
            mask[w] |= ixc
        ixc = ixc << 1

def backtrack(w):
    if (w == wiersze):
        return True
    rowMask(w)
    for i in range(len(rowPerms[w])):
        if ((rowPerms[w][i] & mask[w]) == val[w]):
            obrazek[w] = rowPerms[w][i]
            updateCols(w)
            if (backtrack(w+1)):
                return True
    return False

plik = open("zad_input.txt", "r").read().split("\n")
wk = plik[0].split(" ")
wiersze = eval(wk[0])
kolumny = eval(wk[1])
global colVal
colVal = [[0 for i in range(kolumny)] for j in range(wiersze)]

colIx = [[0 for i in range(kolumny)] for j in range(wiersze)]
mask = [0 for i in range(wiersze)]
val = [0 for i in range(wiersze)]
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

obrazek = [0 for j in range(wiersze)]

wnioskowanie_wiersze()
wnioskowanie_kolumny()

rowPerms = []
for r in range(wiersze):
    res = []
    spaces = kolumny - len(D_wiersze[r]) + 1
    for i in range(len(D_wiersze[r])):
        spaces -= D_wiersze[r][i]
    calcPerms(r, 0, spaces, 0, 0, res)
    rowPerms.append(res)


wypis = open("zad_output.txt", "w")

print(backtrack(0))

for w in obrazek:
    for i in range(kolumny):
        if (w & (1 << i)) == (1 << i):
            wypis.write("#")
        else:
            wypis.write(".")
    wypis.write("\n")

wypis.close()
