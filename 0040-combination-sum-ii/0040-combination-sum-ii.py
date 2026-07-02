class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def recurse(ind, t, ds):
            # Base case
            if ind == len(candidates):
                if t == 0:
                    ans.append(ds[:])  
                return

            # DON'T 
            next=ind+1
            while len(candidates)>next and candidates[next]==candidates[ind]:
                next+=1
            recurse(next, t, ds)
            
            #PICK 
            if candidates[ind] <= t:  
                ds.append(candidates[ind]) 
                recurse(ind+1, t - candidates[ind], ds)
                ds.pop() #backtracking
        
        recurse(0, target, [])  #Call the function
        return ans
        