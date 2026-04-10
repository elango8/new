class Solution:
    def findPairs(self, nums, k: int) -> int:
        usa = []
        for num in nums:
            if num not in usa:
                usa.append(num)
        count = 0
        for i in range(len(usa)):
            for j in range(len(usa)):
                if (usa[i]-usa[j]) == k:
                    count +=1
        return count


my = Solution()
print(my.findPairs([3,1,4,1,5], 2))     

        