# Different Ways to Add Parentheses

from typing import List

class Solution:
    def diffWaysToCompute(self, n: str) -> List[int]:
        s = []
        for i in range(len(n)):
            if n[i] == "+" or n[i] == "-" or n[i] == "*":
                c = n[:i - 1] + "(" + n[i - 1] + n[i] + n[i + 1] + ")" + n[i + 2:]
                s.append(eval(c)) 
                try:
                    c = n[:i - 1] + "((" + n[i - 1] + n[i] + n[i + 1] + ")" + n[i + 2:i + 4] + ")" + n[i + 4:]
                    s.append(eval(c))
                except:
                    pass
                try:
                    c = n[:i - 3] + "(" + n[i - 3:i - 1] + "(" + n[i - 1] + n[i] + n[i + 1] + "))" + n[i + 2:]
                    s.append(eval(c))
                except:
                    pass
        return sorted(list(set(s)))

print(Solution().diffWaysToCompute("2-1-1"))

print(Solution().diffWaysToCompute("2*3-4*5"))
