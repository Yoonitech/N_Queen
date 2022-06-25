
import numpy as np
import random
from timeit import default_timer as timer



def Check_Row(AR, Row, Column):
    for i in range(Column):
        if AR[i] == Row:
            return False
    return True

def Check_X(AR, Row, Column, N_Queen):
    R = Row
    C = Column
    for i in range(N_Queen):
        R += 1
        C -= 1
        if R == AR[C] and C >= 0:
            return False
    R = Row      
    C = Column  
    for i in range(N_Queen):
        R -= 1
        C -= 1
        if R == AR[C] and R != -1 and C >= 0:
            return False
    return True   


def Reman_Var_Finder (AR, Column, N_Queen):
    R_List = []
    for i in range(N_Queen):
        if Check_Row(AR, i, Column) and Check_X(AR, i, Column, N_Queen):
            R_List.append(i)
    return R_List

def Run_Alg(N_Queen):
    AR = []
    for i in range(N_Queen):
        AR.append(-1)
    t1 = timer()
    while(-1 in AR):
        AR = []
        for i in range(N_Queen):
            AR.append(-1)
        for i in range(N_Queen) :
            Var_List = Reman_Var_Finder (AR, i, N_Queen)
            if len(Var_List) == 0:
                break
            Random = random.randint(0,len(Var_List)-1)
            AR[i] = Var_List[Random]
    return (AR,round(timer() - t1, 4))

