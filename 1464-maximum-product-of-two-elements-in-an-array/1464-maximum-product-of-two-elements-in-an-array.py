class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx=0
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                n=(nums[i]-1)*(nums[j]-1)
                maxx=max(maxx,n)
        return maxx

        