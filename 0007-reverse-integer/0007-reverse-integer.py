class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        digits = list(str(abs(x)))  # convert to array of digits
        
        # now do your two pointer swap!
        i, j = 0, len(digits)-1
        while i < j:
            digits[i],digits[j]=digits[j],digits[i]
            i += 1
            j -= 1
        
        result = sign * int("".join(digits))  # convert back
        
        if result < -2**31 or result > 2**31-1:
            return 0
        return result
