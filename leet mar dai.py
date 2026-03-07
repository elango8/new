class Solution(object):
    def minFlips(self, s):
        n = len(s)
        alt1 = "".join("01"[i % 2] for i in range(n))
        alt2 = "".join("10"[i % 2] for i in range(n))
        doubled = s + s
        res = n
        for i in range(n):
            w = doubled[i:i+n]
            res = min(res, sum(w[j] != alt1[j] for j in range(n)), sum(w[j] != alt2[j] for j in range(n)))
        return res

        