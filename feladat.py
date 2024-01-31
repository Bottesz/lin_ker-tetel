import math

def osztok(szam):
    i = 2
    osztoik = []
    for i in range(2,round(math.sqrt(szam) + 1)):
        if szam % i == 0:
            osztoik.append(i)
    return osztoik

print(osztok(100))

"""
def osztok2(szam):
    lista = []
    oszto = 2 
    while oszto
"""




