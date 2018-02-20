# -*- coding: cp1254 -*-
# CSE 321 – Introduction to Algorithm Design Homework 05
# EMRE CELIK - 141044024

# Algoritma : x sayisinin 3'un katina kadar 5 kooyuyorum.Geri kalanini 3 ile dolduruyorum.
# Sonrasinda 3 un sayisi 5 in kati olana kadar geriye dogru 3 ekliyorum(5 lerin yerlerine).
# En son elimdeki sayida 5 ler 3 un kati veya 3 ler 5 in kati degil ise -1 donduruyorum.
# Worst Case Analysis : En sondan basa kadar 3 yerlestirmek.
# O(n) ' dir.

def decentNumber(x):
    result = ""
    bound = x - x % 3
    count3 = 0
    
    if(x < 3):
        return -1;

    for i in range(0, bound):
        result += "5"

    for i in range(bound, x):
        result += "3"
    
    while(bound > 0 and (x - bound) % 5 != 0):
        count3 += 1
        bound -= 1
        result = result[:bound] + "3" + result[bound+1:]

    if(bound % 3 != 0 or (x - bound) % 5 != 0):
        return -1
    
            
    return result



dn =  decentNumber(11)
print(dn)
#Output: 55555533333
