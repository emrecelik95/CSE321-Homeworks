
perm = []
def findOptimalAssistantship(inputTable):
    n = len(inputTable[0])
    r = len(inputTable)
     
    vect = []
    minT = 999999
    temp = 0

    helper(inputTable,n,r,0)

    n = len(inputTable[0])
    r = len(inputTable)
    lenPerm = len(perm)
    vect = [-1]*r
    imin = 0

    for i in range(lenPerm):
        temp = 0
        for k in range(n):
            temp += perm[i][k][k]

        if(temp < minT):
            minT = temp
            imin = i


    for m in range(n):
        vect[inputTable.index(perm[imin][m])] = perm[imin][m].index(perm[imin][m][m])
    for k in range(r-n):
        vect[inputTable.index(perm[imin][n+k])] = -1
        minT += 6
        
    return vect,minT
    
# Permutation Backtracking algorithm reference
# http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string
def helper(inputTable,n,r,i):
    if(i == r-1):
        perm.append(list(inputTable))
    
    for j in range(i,r):
        inputTable[i], inputTable[j] = inputTable[j], inputTable[i]
        helper(inputTable,n,r,i+1)
        inputTable[i], inputTable[j] = inputTable[j], inputTable[i]
        

inputTable = [
    [5, 8,  7],  # R.A. 0
    [8, 12, 7],  # R.A. 1
    [4, 8,  5],  # R.A. 3
    [1,2,3]      # R.A. 3  
            ]    



asst, time = findOptimalAssistantship(inputTable)
print(asst)
print(time)


    
