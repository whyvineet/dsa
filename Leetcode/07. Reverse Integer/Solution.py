# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            result = -int(str(x)[:0:-1])
        else:
            result = int(str(x)[::-1])
            
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result