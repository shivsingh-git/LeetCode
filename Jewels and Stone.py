class Solution:                                                         
        def numJewelsInStones(self, J: str, S: str) -> int:                  
            x , y =[] , []                                                      #creating two lists
            for i in J :
                x.append( i )                                                   #adding the correspondins element in the lists
            for i in S :
                y.append( i )
            c = 0
            for i in x :
                c = c + y.count(i)                                              #counting the values and storing in the counter
            return c
        
