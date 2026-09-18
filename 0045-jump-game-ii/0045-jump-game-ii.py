class Solution:
    def jump(self, nums: list[int]) -> int:
        farthest = 0
        jump=0
        curr=0
        
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])  

            if i==curr:
                jump+=1
                curr=farthest
            
        return jump
    