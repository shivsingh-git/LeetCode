class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""                                                      #declaring the string
        for i in digits:
            s += str(i)                                             #adding the numbers in the string
        return [x for x in str(int(s) + 1)]                         # returning the value adding 1 to last digit
