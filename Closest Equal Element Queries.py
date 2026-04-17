from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        
        for index in queries:
            check = nums[index]
            found = False
            min_dist = n 
           
            for j in range(1, n):
                next_index = (index + j) % n
                if nums[next_index] == check:
                    min_dist = min(min_dist, j)
                    found = True
                    break 
            
            for j in range(1, n):
                prev_index = (index - j + n) % n
                if nums[prev_index] == check:
                    min_dist = min(min_dist, j)
                    found = True
                    break  
            
            if found:
                ans.append(min_dist)
            else:
                ans.append(-1)
        
        return ans
