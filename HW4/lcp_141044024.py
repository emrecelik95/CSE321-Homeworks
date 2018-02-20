# Emre Celik - 141044024 , CSE 321 - HW4, Part2

"""
divAndCon fonksiyonunda Divide and Conquer yaparak sol ve sag yarim listeyi
s1 ve s2 ye atadim.Bu iki listeyi findCommona verip, ortak olanlari liste olarak
return ettim.Bunu yaparken son indisten baslayip geri dogru eleman eleman baktim.


Worst Case Analysis :
Listedeki elemanlar tamamen ayný olsun.
divAndCon fonksiyonunun complexity si O(log (n)) dir. 
findCommon' da bütün elemanlara bakilacagindan O(n) dir.

Worst Case : O(n log(n))
"""


def findCommon(s1, s2):
	common = ""
	n1 = len(s1)
	n2 = len(s2)
	i, j = n1 - 1, n2 - 1
    
	while(i >= 0 and j >= 0):
		if(s1[i] == s2[j]):
			common = s1[i] + common
		else:
			break
		i, j = i - 1, j - 1

	return common

def divAndCon(st, l, r):
	if(l == r):
		return st[l]

	if(l < r):
		m = (r-l)//2 + l
		s1 = divAndCon(st, l, m)
		s2 = divAndCon(st, m + 1, r)

		return findCommon(s1, s2)

        

def longest_common_postfix(st):
	return divAndCon(st, 0, len(st) - 1)

inpStrings = ["absorptivity", "circularity", "electricity", "importunity", "humanity"]
lcp = longest_common_postfix(inpStrings)
print(lcp)
