class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums.sort()
        
        # Case 1: Three largest numbers
        case1 = nums[-1] * nums[-2] * nums[-3]
        
        # Case 2: Two smallest (most negative) × largest
        case2 = nums[0] * nums[1] * nums[-1]
        
        return max(case1, case2)