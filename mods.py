

#{k+m} for x=y(mod n)
def eqIsCorrect(k, m, y, n, max_ = 1000):
    for i in range(max_):
        if not ((k*i+m-y)/n).is_integer():
            return False

    return True

def systemIsCorrect(k,m,y,n, max_=1000):
    for i in range(len(y)):
        if not eqIsCorrect(k,m,y[i],n[i],max_):
            return False

    return True

def calcBruteForceSol(y,n,max_=1000,max_2=1000):
    for i in range(1,max_):
        for j in range(1,max_):
            if systemIsCorrect(i,j,y,n,max_2): 
                return (i,j)

    return -1

aux_par = calcBruteForceSol([8,4,0],[11,10,27],3000,100)
print(aux_par)

#print(eqIsCorrect(2970,1944,8,11))
#print(eqIsCorrect(2970,1944,4,10))
#print(eqIsCorrect(2970,1944,0,27))
#print(eqIsCorrect(aux_par[0],aux_par[1],5,7))




