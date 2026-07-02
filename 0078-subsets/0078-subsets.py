class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        def helper(i,ds):
            if i==n:
                res.append(ds[:]) # whatever in ds copies to resultant
                return 
            #incude
            ds.append(nums[i])
            helper(i+1,ds)
            ds.pop() #back-tracking
            #exclude
            helper(i+1,ds)
        helper(0,[])
        return res