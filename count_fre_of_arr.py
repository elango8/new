# ans needed [5,5,5,5] --> [[5,4]]
class Solution:
    def countFrequencies(self, nums):
        dic = {}
        res = []
        for num in nums:
            dic[num] = dic.get(num,0)+1
        for i,j in dic.items():
            res.append([i,j])
        return res

my = Solution()
print(my.countFrequencies([1, 2, 2, 1, 3]))
