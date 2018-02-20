# Emre Celik - 141044024 , CSE 321 - HW4, Part1 #

"""
divAndCon fonksiyonunda divide and conquer yapýp , left ve right listeyi
, arrayi ve mid indexini getMin fonksiyonuna parametre verip bunun sonucunu
return ederek devam ettim.getMin fonksiyonu left, right ve (eger birlesiyorsa)
left + right listesinden elemanlarýnýn toplamý en kücük olan listeyi return ediyor.
Bunu yaparken de birlestirme kontrolu yapmak icin left in son eleman indexi,
right'ýn ilk eleman indexi ve mid indexini karsilastirip birlesme olup olmadigi
anlasiliyor.Duruma göre left , right veya left + right listesi return edilerek
recursive devam ediliyor.

Worst Case Analysis:
Divide and Conquer'da sagdan ve soldan yariya bolerek gidildiginden
recursion O(logn), getMid fonksiyonunda index ve sum fonksiyonlari kullanildigindan
n, bu her durumda boyle oldugundan ;
Worst Case : O(n log(n))

"""


import sys

def getMin(left, right, arr, m):	
	lEnd = left[len(left) - 1]
	rEnd = right[len(right) - 1]
	
	useMid = (arr.index(lEnd) == m - 1 and arr.index(rEnd) == m + 1)
	combine = ( (lEnd == arr[m] and arr.index(rEnd) == m + 1) or 
				(rEnd == arr[m] and arr.index(lEnd) == m - 1) or useMid)

	lSum = sum(left)
	rSum = sum(right)

	if(combine):
		if(useMid):
			left.append(arr[m])
		smallest = min(lSum, rSum, lSum + rSum)
	else:
		smallest = min(lSum, rSum)

	if(smallest == lSum):
		return left
	elif(smallest == rSum):
		return right
	elif(smallest == lSum + rSum):
		return (left + right)

def divAndCon(arr, l, r):
	if(l == r):
		return [arr[l]]                                    

	if(l < r):
		m = (r-l)//2 + l

		l1 = divAndCon(arr, l, m)
		l2 = divAndCon(arr, m + 1, r)

		return getMin(l1, l2, arr, m)

def min_subarray_finder(arr):
	return divAndCon(arr, 0, len(arr) - 1)

inpArr = [1, -4, -7, 5, -13, 9, 23, -1]
msa = min_subarray_finder(inpArr)
print(msa)
print(sum(msa))
