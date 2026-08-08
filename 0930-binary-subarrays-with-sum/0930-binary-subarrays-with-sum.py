class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(k):
            if k<0:
                return 0
            l=0
            s=0
            cnt=0
            for r in range(len(nums)):
                s=s+nums[r]
                while s>k:
                    s-=nums[l]
                    l+=1
                cnt+=r-l+1
            return cnt
        return atmost(goal) - atmost(goal - 1)
            
            