class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxl=0
        zero=0
        l,r=0,0
        while r<len(nums):
            if nums[r]==0:
                zero+=1    #count of traced 0's
            if zero > k:   #increased threshold of 0's
                if nums[l]==0:   
                    zero-=1     #making the 0's  k-times
                l+=1    #shrinking the window from left side
            length =r-l+1
            maxl=max(length,maxl)
            r+=1
        return maxl
        