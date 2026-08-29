class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def backtrack(start: int, curr: List[int]):
            res.append(curr[:]) #whole set as a subset is obvious
            
            for i in range(start, len(nums)): #we iterate
                if i > start and nums[i] == nums[i - 1]: #if prev is same as curr- leave it
                    continue
                curr.append(nums[i])#append whatever bypasses the above cond.
                backtrack(i + 1, curr) #imoves ahead,checks for next number
                curr.pop()
        
        backtrack(0, [])
        return res