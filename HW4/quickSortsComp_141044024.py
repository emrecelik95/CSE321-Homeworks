# Emre Celik - 141044024 , CSE 321 - HW4, Part5 #

"""
Referans : http://www.cs.bilkent.edu.tr/~atat/473/lecture05.pdf

Hoare's ve Lomuto's Partition' da eger array sirali gelir ise quicksortun O(n^2)
calismasina neden olur. Hoare genel olarak swap etme olasiligi daha az oldugundan
Lomuto Partition'dan daha hizlidir. Tum elemanlar esit olsa bile düzenli ayirma
islemi yapar.

"""


def lomutoPartition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if(arr[j] <= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return (i + 1)

def hoarePartition(arr, lo, hi):
    pivot = arr[lo]
    i = lo - 1
    j = hi + 1
    while(True):

        j -= 1
        while(arr[j] > pivot):
            j -= 1

        i += 1
        while(arr[i] < pivot):
            i += 1
        
        if(i < j):
            arr[i], arr[j] = arr[j], arr[i]
        else:
            return j
        
        
def quickSort(arr, lo, hi, part):

    if(lo < hi):
        i = 0
        if(part == "lomuto"):
            i = lomutoPartition(arr, lo, hi);
            quickSort(arr, lo, i - 1, part)
            quickSort(arr, i + 1, hi, part)
            
        elif(part == "hoare"):
            i = hoarePartition(arr, lo, hi)
            quickSort(arr, lo, i, part)
            quickSort(arr, i + 1, hi, part)

        

            
def quickSortLomuto(arr):
    low = 0
    hi = len(arr) - 1
    temp = list(arr)
    quickSort(temp, 0, len(arr) - 1, "lomuto")
    return temp


def quickSortHoare(arr):
    low = 0
    hi = len(arr) - 1
    temp = list(arr)
    quickSort(temp, 0, len(arr) - 1, "hoare")
    return temp
                               

arr = [15,4,68,24,75,16,42]
qsh = quickSortHoare(arr)
print(qsh)
qsl = quickSortLomuto(arr)
print(qsl)
