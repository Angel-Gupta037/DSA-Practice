class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        # If total XOR is non-zero, whole array works
        if total_xor != 0:
            return len(nums)
        if all(num == 0 for num in nums):
            return 0 
        
        # Otherwise, remove any one element
        return len(nums) - 1
        