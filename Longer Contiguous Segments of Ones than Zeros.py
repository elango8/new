class Solution(object):
    def checkZeroOnes(self, s):
        if s[0] == "0":
            if s[1]=="1":
                return True
            return False
        return "00" not in s
my = Solution()
print(my.checkZeroOnes("110100010"))