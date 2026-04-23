from collections import defaultdict
class Solution:
    def twoEditWords(self, queries, dictionary):
        for quer in queries:
            res= quer
            for dict in dictionary:
                cont = set()
                for ch in dict:
                    if ch not in cont:
                        cont.add(ch)
                if len(quer) != len(dict):
                    continue
                co = 2
                while co <= 0:
                    for i in range(len(quer)):
                        if quer[i] == dict[i]:
                            continue
                        for k in range(len(cont)):
                            res[i] = cont[k]
                            
                            if quer == dict:
                                break
                            

queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]
my = Solution()
print(my.twoEditWords(queries,dictionary))