# -*- coding: cp1254 -*-
# CSE 321 – Introduction to Algorithm Design Homework 05
# EMRE CELIK - 141044024

# Algoritma : Bastan baslayip, (i. eleman - i+1.eleman) + (i+1.eleman - i+2.eleman) sonucu,
# i.eleman 1 oldugunda bu sonuc, i+1.eleman 1 oldugunda bu sonuc arasından maksimum olana gore
# i. ya da (i + 1).elemani 1'e set eder. Ilk ve son eleman icin sadece yanindakiyle farkini alir.
# Worst Case Analysis : Liste her durumda iterate edildiginden O(n)' dir. 


def find_maximum_cost(x):
    x = list(x)
    size = len(x)
    maxSum = 0
    
    normal = 0
    edit = 0
    edit2 = 0
    
    normal = abs(x[0] - x[1]) + abs(x[2] - x[1])
    edit = abs(1 - x[1]) + abs(x[2] - x[1])
    edit2 = abs(1 - x[0]) + abs(x[2] - 1)
    
    x[0] = 1 if (edit > normal and edit > edit2) else x[0]
    x[1] = 1 if (edit2 > normal and edit2 > edit) else x[1]
    
    for i in range(1,size - 1):
        if(i <= size - 3): 
            normal = abs(x[i] - x[i + 1]) + abs(x[i + 2] - x[i + 1])
            edit = abs(1 - x[i + 1]) + abs(x[i + 2] - x[i + 1])
            edit2 = abs(1 - x[i]) + abs(x[i + 2] - 1)
        else:
            normal = abs(x[i] - x[i + 1])
            edit = abs(1 - x[i + 1])
            edit2 = abs(1 - x[i])
            
        x[i] = 1 if (edit > normal and edit > edit2) else x[i]
        x[i + 1] = 1 if (edit2 > normal and edit2 >= edit) else x[i + 1]

    normal = abs(x[size - 1] - x[size - 2])
    edit = abs(1 - x[size - 2])
    x[size - 1] = 1 if (edit > normal) else x[size - 1]

    for i in range(1,size):
        maxSum += abs((x[i] - x[i - 1]))

    print(x)
        
    return maxSum


Y = [ 79, 6, 40, 68, 68, 16] 
cost = find_maximum_cost(Y)
print(cost)
