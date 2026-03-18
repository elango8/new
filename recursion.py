# def rec(a=0,cut = 0):
#     if a == 10:
#         return cut 
#     else:
#         cut += a
#         a+=2
#         return rec(a,cut)
    
# print(rec())

# def num(i=1,n=5):
#     if i > n:
#         return 
#     print(i)
#     return num(i+1,n)
# num()

# def num(n=5):
#     if n <= 0:
#         return 
#     print(n)
#     return num(n-1)
# num()


# def summ(n=3,sum=0):
#     if n < 1:
#         print(sum)
#         return
#     else:return summ(n-1,sum+n)
# summ()  

def facti(n):
    if n == 0:
        return 1
    else:
        return n*(facti(n-1))
print(facti(5))

