
def getCost(X,Y):
    if(X == "AUX" or Y == "AUX"):
        return 1

    return 2

def TOH(A,B,C,n,liste):

    if(n == 1):
        print("disk", n, A, "to", C)
        liste[n - 1] = liste[n - 1] + n * getCost(A,C)
    else:
        TOH(A,C,B,n-1,liste)
        liste[n - 1] = liste[n - 1] + n * getCost(A,C)
        print("disk", n, A, "to", C)
        TOH(B,A,C,n-1,liste)

def TOHtime(A,B,C,n):
    liste = []
    for i in range(n):
        liste.append(0)

    print("Input size is", n)
    TOH(A,B,C,n,liste)
    for i in range(n):
        	print("Elapsed time for disk",i + 1,":", liste[i]) 

TOHtime("SRC","AUX","DST",3)
