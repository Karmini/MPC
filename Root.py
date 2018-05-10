#Approximation numérique d'une racine avec la méthode de Heron

c = float(input("Racine à calculer : "))
while c <= 0:
   c = float(input("Racine à calculer : "))
   
x0 = c
epsilon = 10**(-10)
Nitermax = 100


def racine(x0, epsilon, Nitermax):
    for m in (1,8):
        n = Nitermax
        e = epsilon
        x = float(x0)
        print("n:",0,"| x:",x)
        for i in range(1,n+1):
            a = x
            try :
                x = 0.5*(x + c/x)
            except :
                print("\nIl y a une erreur de calcul\n")
                return
            print("n:",i,"| x:",x)
            
            if (abs(a - x)) <= e:
                print("\nLa racine de",c,"est",x,"\navec une précision de après la virgule")
                return
            if i == n:
                print("Le nombre d'itérations est atteint à",n,"avec une précision de :",e,"\n")

racine(c, epsilon, Nitermax)


