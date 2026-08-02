from math import gcd
from typing import List
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:

        maxx=float('-inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                g=gcd(nums[i], nums[j])
                m=(nums[i] * nums[j]) // (g**2)
                maxx=max(maxx,m)
        return maxx
    
        