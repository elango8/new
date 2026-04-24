class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count = 0
        for i in range(len(moves)):
            if moves[i] == '_':
                count +=1
        return count

my = Solution()
print(my.furthestDistanceFromOrigin("_R__LL_"))