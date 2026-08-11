class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix=nums[0]
        i=1
        while i< len(nums) and nums[i]==nums[i-1]+1:
            prefix+=nums[i]
            i+=1
        missing=prefix
        while missing in nums:
            missing+=1
        return missing

        