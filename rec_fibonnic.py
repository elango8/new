class Solution:
    def fib(self, n: int) -> int:
        if n <=1:
            return n
        fi = self.fib(n-1)
        se = self.fib(n-2)
        return fi+se
        