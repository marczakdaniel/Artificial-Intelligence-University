
from queue import Queue

def zamiana(poz):
    kolumna = ord(poz[0]) - ord('a') + 1
    wiersz = int(poz[1])
    return [kolumna, wiersz]

# plansza:
#   1 2 3 4 5 6 7 8
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1


# ruchy:
# 1 2 3
# 4 P 5
# 6 7 8



def czy_legalny_ck(BK, BW, CK):
    w_CK = CK[1]
    k_CK = CK[0]
    if (w_CK < 1 or w_CK > 8 or k_CK <  1 or k_CK > 8):
        return False
    if (CK == BK or CK == BW):
        return False
    w_BK = BK[1]
    k_BK = BK[0]
    w_BW = BW[1]
    k_BW = BW[0] 
    if (w_CK == w_BW or k_CK == k_BW):
        return False
    if ((w_CK <= w_BK + 1 and w_CK >= w_BK - 1) and (k_CK <= k_BK + 1 and k_CK >= k_BK - 1)):
        return False
    
    return True

def czy_legalny_bk(BK, BW, CK):
    w_BK = BK[1]
    k_BK = BK[0]
    if (w_BK < 1 or w_BK > 8 or k_BK <  1 or k_BK > 8):
        return False
    if (BK == CK or BK == BW):
        return False
    w_CK = CK[1]
    k_CK = CK[0]
    if ((w_BK <= w_CK + 1 and w_BK >= w_CK - 1) and (k_BK <= k_CK + 1 and k_BK >= k_CK - 1)):
        return False
    
    return True

def czy_legalny_bw(BK, BW, CK):
    w_BW = BW[1]
    k_BW = BW[0]
    if (w_BW < 1 or w_BW > 8 or k_BW <  1 or k_BW > 8):
        return False
    if (BW == BK or BW == CK):
        return False
    w_CK = CK[1]
    k_CK = CK[0]
    if ((w_BW <= w_CK + 1 and w_BW >= w_CK - 1) and (k_BW <= k_CK + 1 and k_BW >= k_CK - 1)):
        return False
    return True

def czy_mat(BK, BW, CK):
    w_CK = CK[1]
    k_CK = CK[0]
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if (i != 0 or j != 0):
                new_CK = [k_CK + i, w_CK + j]
                if czy_legalny_ck(BK, BW, new_CK) == True:
                    return False
    return True


# ruch:
# 0 - białe
# 1 - czarne

def BFS(ruch, BK, BW, CK):
    Q = Queue(maxsize=0)
    Q.put([ruch, BK, BW, CK])
    odwiedzone = []
    odwiedzone.append([ruch, BK, BW, CK])
    ile = 0
    kolor = ruch
    while Q.empty() == False:
        stan = Q.get()
        a_ruch = stan[0]
        a_BK = stan[1]
        a_BW = stan[2]
        a_CK = stan[3]
        if (a_ruch != kolor):
            kolor = a_ruch
            ile += 1
        if (a_ruch == 1):
            if (czy_mat(a_BK, a_BW, a_CK) == True):
                return ile
            else:
                for i in range(-1, 2, 1):
                    for j in range(-1, 2, 1):
                        if (i != 0 or j != 0):
                            new_CK = [a_CK[0] + i, a_CK[1] + j]
                            new_stan = [0, a_BK, a_BW, new_CK]
                            if (new_stan in odwiedzone) == False:
                                if (czy_legalny_ck(a_BK, a_BW, new_CK)):
                                    odwiedzone.append(new_stan)
                                    Q.put(new_stan)
        elif (a_ruch == 0):
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if (i != 0 or j != 0):
                        new_BK = [a_BK[0] + i, a_BK[1] + j]
                        new_stan = [1, new_BK, a_BW, a_CK]
                        if (new_stan in odwiedzone) == False:
                            if (czy_legalny_bk(new_BK, a_BW, a_CK)):
                                odwiedzone.append(new_stan)
                                Q.put(new_stan)
            new1_BW = [a_CK[0], a_BW[1]]
            if ([1, a_BK, new1_BW, a_CK] in odwiedzone) == False:
                if (czy_legalny_bw(a_BK, new1_BW, a_CK)):
                    odwiedzone.append([1, a_BK, new1_BW, a_CK])
                    Q.put([1, a_BK, new1_BW, a_CK])
            new2_BW = [a_BW[0], a_CK[1]]
            if ([1, a_BK, new2_BW, a_CK] in odwiedzone) == False:
                if (czy_legalny_bw(a_BK, new2_BW, a_CK)):
                    odwiedzone.append([1, a_BK, new2_BW, a_CK])
                    Q.put([1, a_BK, new2_BW, a_CK])

#black b4 f3 e8
#print(BFS(1, zamiana('b4'), zamiana('f3'), zamiana('e8')))            

#inp: white a1 e3 b7 out: 9
print(BFS(0, zamiana('a1'), zamiana('e3'), zamiana('b7')))  
#inp: black h7 a2 f2 out: 6
#print(BFS(1, zamiana('h7'), zamiana('a2'), zamiana('f2')))  
#inp: black a2 e4 a4 out: 8
#print(BFS(1, zamiana('a2'), zamiana('e4'), zamiana('a4')))  



            

            
        
         




