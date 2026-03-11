# from collections import defaultdict
# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         dic = defaultdict(int)
#         count = 0
#         for num in nums:
#             dic[num]+=1
#         rem = 0
#         for i,j in dic.items():
#             if j > 2:
#                 dic[i] = 2
#         for k,m in dic.items():
#             count += m

class Solution:
    def removeDuplicates(self, nums) -> int:
        s_list = []
        n= len(nums)
        for i in range(n):
            if s_list.count(nums[i]) <= 2:
                s_list.append(nums[i])
            del nums[i]
        return len(s_list),s_list
 

my = Solution()
print(my.removeDuplicates([0,0,1,1,1,1,2,3,3]))