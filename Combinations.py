from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        m=[]
        for i in range(1,n+1):
            m.append(i)
        comb= combinations(m,k)
        return(comb)
        
