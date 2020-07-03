class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum1=bin(int(a,2)+int(b,2))
        return(sum1[2:])
