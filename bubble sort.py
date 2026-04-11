class Solution:
    def selectionSort(self, nums):
        
        for i in range(len(nums)):
            flag = False
            for j in range(0,len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]
                    flag = True
            if not flag:
                break
        return nums


my = Solution()
print(my.selectionSort([7, 4, 1, 5, 3]))