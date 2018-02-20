# Emre Celik - 141044024 , CSE 321 - HW4, Part4 #

"""
find_kth_book_2 fonksiyounda onceki parttan farkli olarak, oncekinde midlerin toplamina
bagli olarak ikisini ayri ayri olarak boluyorduk(logm + logn).Burada ikisini ayni
birlikte gibi dusunup bolme islemi yapiyoruz(log k).
"""

def find_kth_book_2(m, n, k):

    if(len(m) == 0):
        return n[k - 1]

    if (len(m) > len(n)):
        return find_kth_book_2(n, m, k);

    if(k == 1):
        return min(m[0], n[0])
    
    i = min(len(m), k//2)
    j = min(len(n), k//2)

    if(m[i - 1] > n[j - 1]):
        return find_kth_book_2(m, n[j:], k - j)

    return find_kth_book_2(m[i:], n, k - i)

m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]

book = find_kth_book_2(m,n,6)
print(book)
#Output: systemsprogramming
