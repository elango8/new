# n1= 52
# n2 = 10
# out = 0
# while n1>0 and n2 > 0:
#     if n1>n2:
#         n1 = n1%n2
#     else:
#         n2 = n2%n1
# if (n1==0):print(n2)
# else:print(n1)

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = 0
        co1 = 0
        co2 = 0
        odd = 0
        for i in range(1,n*n):
            if i%2 == 0:
                co1 +=1
                if co1 <= n:
                    even +=i
                
            else:
                co2+=1
                if co2 <= n:
                    odd +=i
                  
        while even >0 and odd>0:
            if even > odd:
                even = even%odd
            else:
                odd = odd%even
        if even == 0:
            return odd
        else:return even
        
my = Solution()
print(my.gcdOfOddEvenSums(7))
