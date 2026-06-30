class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        i=0
        # Check for spaces.
        while i<n and (s[i]==' ' or s[i]==0):
            i+=1

        
        #Check for sign of negative or positive.
        sign=1
        if i<n and (s[i]=='-'or s[i]=='+'):
            sign=-1 if s[i]=='-'else 1
            i+=1

        # Check for non digit value.
        res=0
        while i<n and s[i].isdigit():
            res=res*10+int(s[i])
            i+=1
        #The digit value
        res *= sign
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        
        return res
        