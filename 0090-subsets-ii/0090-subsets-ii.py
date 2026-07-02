class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        n=len(nums)
        res=[]
        def helper(i,ds):
            if i==n:
                res.append(ds[:])
                return
            #include
            ds.append(nums[i])
            helper(i+1,ds)
            ds.pop()
            idx=i+1
            while idx<n and nums[idx-1]==nums[idx]:
                idx+=1
            helper(idx,ds)
        helper(0,[])
        return res

         
        