#plik = open('words_for_ai1.txt', 'r')
#zawartosc = plik.readlines()
#dictionary = []
#for x in zawartosc:
#    dictionary.append(x.replace("\n", ""))
#plik.close()
#
slownik = set(open('words_for_ai1.txt', 'r').read().split("\n"))
max_l = len(max(slownik, key=len))

def podzial_wiersza(linia):
    dp = [[['', 0] for x in range(len(linia) + 1)] for y in range(len(linia) + 1)] 


    for rozmiar in range(1, len(linia) + 1):
        for poc in range(len(linia) - rozmiar):
            if (linia[poc:(poc+rozmiar)] in slownik):
                dp[poc][poc+rozmiar - 1] = [linia[poc:(poc+rozmiar)], len(linia[poc:(poc+rozmiar)]) ** 2]
            else:
                for i in range(0, rozmiar-1):
                    if (dp[poc][poc+i][1] > 0 and dp[poc+i+1][poc+rozmiar-1][1] > 0 and dp[poc][poc+i][1]+dp[poc+i+1][poc+rozmiar-1][1] > dp[poc][poc+rozmiar-1][1]):
                        dp[poc][poc+rozmiar-1][1] = dp[poc][poc+i][1]+dp[poc+i+1][poc+rozmiar-1][1]
                        dp[poc][poc+rozmiar-1][0] = dp[poc][poc+i][0] + ' ' + dp[poc+i+1][poc+rozmiar-1][0]
    return dp


print(podzial_wiersza('ksiegapierwsza'))    



