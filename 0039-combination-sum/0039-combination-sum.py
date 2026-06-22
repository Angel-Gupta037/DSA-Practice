class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def helper(i,ds,target):
            if target==0:
                res.append(ds[:])
                return
            if i==len(candidates) or target<0:
                return
            ds.append(candidates[i])
            helper(i,ds,target-candidates[i])
            ds.pop()
            helper(i+1,ds,target)
        helper(0,[],target)
        return res