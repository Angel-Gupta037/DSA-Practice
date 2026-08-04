class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        used=[False]*len(nums)
        def backtrack(perm):
            if len(perm)==len(nums):
                res.append(perm[:])
                return 

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i]=True
                perm.append(nums[i])
                backtrack(perm)
                perm.pop()
                used[i]=False
        backtrack([])
        return res

        