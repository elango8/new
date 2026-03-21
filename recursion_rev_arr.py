def rev_ar(ar,l,r):
    if (l >= r):
        return ar
    else:
        temp = ar[r]
        ar[r] = ar[l]
        ar[l] = temp
        return rev_ar(ar,l+1,r-1)
ar = [6,2,4,9,8]
print(rev_ar(ar,0,len(ar)-1))
    
def rev_ar(ar, l, r):
    if l >= r:
        return ar
    else:
        ar[l], ar[r] = ar[r], ar[l]   
        return rev_ar(ar, l+1, r-1)

ar = [1, 2, 8, 4, 6]
print(rev_ar(ar, 0, len(ar)-1))