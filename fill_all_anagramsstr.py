from collections import defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        req_s = len(p)
        indexes = []
        occ = defaultdict(int)
     
        for ch in p:
            occ[ch] += 1

        sl_win = defaultdict(int)
        l = 0
        
        for r in range(len(s)):
            sl_win[s[r]] += 1

            if r - l + 1 > req_s:
                sl_win[s[l]] -= 1
                if sl_win[s[l]] == 0:
                    del sl_win[s[l]]
                l += 1

            if sl_win == occ:
                indexes.append(l)
        
        return indexes

my = Solution()
print(my.findAnagrams("cbaebabacd", "abc")) 