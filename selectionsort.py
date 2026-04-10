class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums)):
            ini = i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[ini]:
                    ini = j
            nums[i] , nums[ini]= nums[ini],nums[i]
        return nums

my = Solution()
print(my.selectionSort([7, 4, 1, 5, 3]))