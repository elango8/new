class Solution:
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        ans = float("inf")

        for i in range(n):
            index = (startIndex + i) % n
            if words[index] == target:
                ans = min(ans, i)

        for i in range(n):
            index = (startIndex - i + n) % n
            if words[index] == target:
                ans = min(ans, i)

        return -1 if ans == float("inf") else ans