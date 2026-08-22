class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        s,p=0,1
        while n>0:
            digit=n%10
            s+=digit
            p*=digit
            n=n//10
        if temp%(s+p)==0:
            return True
        else:
            return False
        