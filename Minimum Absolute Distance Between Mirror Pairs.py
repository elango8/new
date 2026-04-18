from typing import List
from collections import defaultdict

class Solution:
    @staticmethod
    def rev(num: int) -> int:
        rev = 0
        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit 
            num = num // 10 
        return rev

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        result = float("inf")

        for i, num in enumerate(nums):
            dic[num].append(i)

        for i, num in enumerate(nums):
            check = Solution.rev(num)
            if check in dic:
                for j in dic[check]:
                    if i < j:  
                        result = min(result, abs(i - j))

        return -1 if result == float("inf") else result


my = Solution()
print(my.minMirrorPairDistance([12,21]))