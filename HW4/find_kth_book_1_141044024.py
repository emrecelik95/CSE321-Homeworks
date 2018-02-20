# Emre Celik - 141044024 , CSE 321 - HW4, Part3 #

"""
find_kth_book_1_helper fonksiyonunda iki arrayin midlerinin toplamina bakarak eger
k dan kucukse , midi kucuk olan arrayi midden itibaren sag tarafini recursion kol
ile gonderiyoruz.Ayný zamanda size azaldiginden k da o arrayin midi + 1 kadar azalýyor.
Eger midlerinin toplami k dan buyuk veya esit ise bu sefer midi dahil ederek
sag taraftan arrayi bolup o arrayin end degiskeni olarak recursion kola veriliyor.
Arraylerden biri, kendi end arrayine esit oldugunda, sonuc diger arrayin k ninci
indisindeki eleman oluyor.

"""

    
def find_kth_book_1_helper(m, n, mEnd, nEnd,k):

    if(m == mEnd):
        return n[k]
    if(n == nEnd):
        return m[k]
    
    mMid = (len(m) - len(mEnd)) // 2
    nMid = (len(n) - len(nEnd)) // 2

    if(mMid + nMid < k):
        if(m[mMid] > n[nMid]):
            return find_kth_book_1_helper(m, n[nMid + 1:], mEnd, nEnd, k - nMid - 1)
        else:
            return find_kth_book_1_helper(m[mMid + 1:],n, mEnd, nEnd, k - mMid - 1)
    else:
        if(m[mMid] > n[nMid]):
            return find_kth_book_1_helper(m, n, m[mMid:], nEnd, k)
        else:
            return find_kth_book_1_helper(m, n, mEnd, n[nMid:], k)


def find_kth_book_1(m, n, k):
    return find_kth_book_1_helper(m, n, m[len(m):], n[len(n):], k - 1)


m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]

book = find_kth_book_1(m,n,6)
print(book)
#Output: systemsprogramming
