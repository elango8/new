from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = 0
        exist = 0
        fre = defaultdict(int)
        for ch in s:
            fre[ch] += 1
        for key,value in fre.items():
            if value == 1:
                res = s.index(key)
                exist = 1
                break
        if exist == 0:
            return -1
        return res
    
my = Solution()
print(my.firstUniqChar("leetcode"))