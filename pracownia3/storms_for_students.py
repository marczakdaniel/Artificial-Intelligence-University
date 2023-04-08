
def B(i,j):
    return 'B_%d_%d' % (i,j)



def print_domains(R, C):
    for i in range(R):
        for j in range(C):
            s = "    " + B(i, j) + " in 0..1,"
            writeln(s)


def suma_R(R, C, rows):
    for i in range(R):
        row = "    "
        for j in range(C):
            row = row + (B(i, j))
            if (j != C - 1):
                row = row + ' + '
            else:
                row = row + ' #= '
        row = row + str(rows[i]) + ","
        writeln(row)

def suma_C(R, C, cols):
    for j in range(C):
        col = "    "
        for i in range(R):
            col = col + (B(i, j))
            if (i != R - 1):
                col = col + ' + '
            else:
                col = col + ' #= '
        col = col + str(cols[j]) + ","
        writeln(col)

def znane(triples):
    for t in triples:
        row = "    " + B(t[0], t[1]) + ' #= ' + str(t[2]) + ","
        writeln(row)

def prostokaty(R, C):
    for i in range(R):
        for j in range(C - 2):
            row = "    " + B(i, j+1) + "#= 1 #==> " + B(i, j) + " + " + B(i, j+2) + " #> 0,"
            writeln(row)
    for j in range(C):
        for i in range(R - 2):
            col = "    " + B(i+1, j) + "#= 1 #==> " + B(i, j) + " + " + B(i+2, j) + " #> 0,"
            writeln(col)

def rogi(R, C):
    for i in range(R-1):
        for j in range(C-1):
            row = "    " + B(i, j) + " + " + B(i + 1, j + 1) + " #= 2 #<==> " + B(i+1, j) + " + " + B(i, j + 1) + " #= 2,"
            writeln(row)

def storms(rows, cols, triples):
    writeln(':- use_module(library(clpfd)).')

    R = len(rows)
    C = len(cols)
    
    bs = [ B(i,j) for i in range(R) for j in range(C)]
    
    writeln('solve([' + ', '.join(bs) + ']) :- ')
    
    #TODO: add some constraints
    print_domains(R, C)
    suma_R(R, C, rows)
    suma_C(R, C, cols)
    znane(triples)
    prostokaty(R, C)
    rogi(R, C)

    #writeln('    [%s] = [1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0],' % (', '.join(bs),)) #only for test 1

    writeln('    labeling([ff], [' +  ', '.join(bs) + ']).' )
    writeln('')
    writeln(":- tell('prolog_result.txt'), solve(X), write(X), nl, told.")

def writeln(s):
    output.write(s + '\n')

txt = open('zad_input.txt').readlines()
output = open('zad_output.txt', 'w')

rows = list(map(int, txt[0].split()))
cols = list(map(int, txt[1].split()))
triples = []

for i in range(2, len(txt)):
    if txt[i].strip():
        triples.append(list(map(int, txt[i].split())))
storms(rows, cols, triples)            
        

