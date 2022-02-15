import numpy as np
import pandas as pd

def ParcoursLargeur(matrice, s):
    elm = s
    k = 0
    Q = []
    print(len(matrice[0]))
    for i in range(len(matrice[0])):
        mydect[i] = -1
    while k < len(matrice[0]):
        for i in range(len(matrice[0])):
            if matrice[elm, i] != 0:
                if mydect[i] == -1:
                    Q.insert(0, i)
                mydect[elm] = 1
                mydect[i] = 1

        print("----------------------------------------------------------------------------------------------------------")
        print(pd.Series(mydect))
        if(sum(mydect.values()) == len(matrice)):
            break
        print(Q)
        print("----------------------------------------------------------------------------------------------------------")

        elm = Q[-1]
        print("elem = ", elm)
        if (len(Q)>1):
            del Q[-1]

        print(Q)
        k += 1




mydect = {}
connection = {}
matrice = np.array([
    [0,1,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,0],
    [0,0,0,1,0,1,0,1,0],
    [1,0,1,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,0,1],
    [0,0,1,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,1,1,0,0,0,0,0,0],
    [1,0,0,0,1,0,0,0,0]
])
long = len(matrice[0])

ParcoursLargeur(matrice, 0)