class Solution(object):
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        result = []
        for i in range(n):
            result.append('0' if nums[i][i] == '1' else '1')
        return "".join(result)
        