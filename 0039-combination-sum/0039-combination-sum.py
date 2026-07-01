class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def recurse(ind, t, ds):
            # Base case
            if ind == len(candidates):
                if t == 0:
                    ans.append(ds[:])  
                return
            
            # DON'T 
            recurse(ind + 1, t, ds)
            
            #PICK (if it fits)
            if candidates[ind] <= t:  
                ds.append(candidates[ind]) 
                recurse(ind, t - candidates[ind], ds)
                ds.pop() 
        
        recurse(0, target, [])  #Call the function
        return ans