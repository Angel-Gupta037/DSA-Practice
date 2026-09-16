class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0 
        for i in range(len(nums)):
            if i > farthest:
                return False  # Yahan tak pahunch hi nahi sakte
            
            farthest = max(farthest, i + nums[i])  # Yahan se kitna aage ja sakte hain
        return True