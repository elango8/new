class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic1 ={}
        dic2 ={}
        res = ""
        for ch in s:
            dic1[ch] = dic1.get(ch,0)+1
        for chr in t:
            dic2[chr] = dic2.get(chr,0)+1
        
        for key,value in dic2.items():
            if key not in dic1:
                res += key
            elif value > 1:
                res += key
        return res 

my = Solution()
print(my.findTheDifference("abcd","abcde"))