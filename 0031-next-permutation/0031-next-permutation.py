class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        ind=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break

        if ind == -1:
            nums.reverse()
            return
        
        for i in range(len(nums)-1,ind,-1):
            if nums[i]>nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
                break
        nums[ind+1: ]=sorted(nums[ind+1:])
        