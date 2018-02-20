# -*- coding: cp1254 -*-
# CSE 321 – Introduction to Algorithm Design Homework 05
# EMRE CELIK - 141044024
# Algoritma : Yeni bir cost matrisi yapiyorum. Ilk sutunu aynen alip(birinden baslandigi icin)
# sonraki sutunları yerlestirirken gelebilecegi noktalardan max olani(cost matrisinden)
# alip kendiyle toplayip yaziyorum. Son sutun, cikis yeri olup, o sutunun max'ini aliyorum.
# Worst Case Analysis : Her durumda n*m lik yeni bir cost matris olustururken iterate edeceginden
# O(n*m)' dir.


def theft(x):
    cost = list(x)
    maxCost = 0

    for i in range(1,len(x[0])):
        for j in range(0, len(x)):
            
            if(j == 0):
                cost[j][i] = cost[j][i] + max(cost[j][i - 1], cost[j + 1][i - 1])
            elif(j == len(x[0]) - 1):
                cost[j][i] = cost[j][i] + max(cost[j - 1][i - 1], cost[j][i - 1])
            else:
                cost[j][i] = cost[j][i] + max(cost[j - 1][i - 1], cost[j][i - 1], cost[j + 1][i - 1])
            
            maxCost = cost[j][i] if (cost[j][i] > maxCost) else maxCost
            
            
    return maxCost

amountOfMoneyInLand= [[10,33,13,15], [22,21,4,1], [5,0,2,3], [0,6,14,2]]
res = theft(amountOfMoneyInLand)
print(res)
#Output: 83
