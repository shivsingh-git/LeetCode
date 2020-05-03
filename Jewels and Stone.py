class Solution:
        def numJewelsInStones(self, J: str, S: str) -> int:
            x , y =[] , []
            for i in J :
                x.append( i )
            for i in S :
                y.append( i )
            c = 0
            for i in x :
                c = c + y.count(i)
            return c
        
