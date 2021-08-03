# Minimum Score Triangulation of Polygon

from typing import List, Tuple

from itertools import combinations

def order_by_score(e):
    return e[0] * e[1] * e[2]

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values) - 2
        c = [i for i in (set(tuple(j) for j in [i for i in combinations(values, 3)]))]
        for i in c:
            for j in c:
                if self.calcScore(i) == self.calcScore(j) and i != j:
                    c.remove(j)
        s = 0
        while n != 0:
            m = min(c, key = order_by_score)
            s += self.calcScore(m)
            c.remove(m)
            n -= 1
        return s
    def calcScore(self, t: Tuple) -> int:
        return t[0] * t[1] * t[2]
        
print(Solution().minScoreTriangulation([1,2,3]))

print(Solution().minScoreTriangulation([3,7,4,5]))

print(Solution().minScoreTriangulation([1,3,1,4,1,5]))
