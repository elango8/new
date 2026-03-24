class Solution:
    def maximumTripletValue(self, nums) -> int:
        l = 0
        r = len(nums)-1
        max_t = 0
        mid = r//2
        while l < mid:
                max_t = max(max_t,(nums[l]-nums[mid])*nums[r])
                l+=1
        if max_t < 0:
             return -1
        return max_t
maxi = Solution()
print(maxi.maximumTripletValue([3,2,1]))