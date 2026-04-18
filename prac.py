from typing import List

class Solution:
    @staticmethod
    def rev(num: int) -> int:
        rev = 0
        while num > 0:
            rev = rev * 10 + (num % 10)
            num //= 10
        return rev

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_seen = {}
        result = float("inf")

        for i, num in enumerate(nums):
            rev_num = Solution.rev(num)

            if rev_num in last_seen:
                result = min(result, i - last_seen[rev_num])

            last_seen[num] = i 

        return -1 if result == float("inf") else result
    
my = Solution()
print(my.minMirrorPairDistance([12,21]))