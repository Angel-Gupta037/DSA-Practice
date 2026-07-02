class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        arr = list(range(1, 10)) 
        
        def recurse(ind, remaining, ds):
            # Base case
            if len(ds) == k:
                if remaining == 0:
                    res.append(ds[:])
                return
            
            if ind == len(arr) or remaining < 0:
                return
            
            # DON'T PICK 
            recurse(ind + 1, remaining, ds)
            
            # PICK 
            if arr[ind] <= remaining:
                ds.append(arr[ind]) 
                recurse(ind + 1, remaining - arr[ind], ds)
                ds.pop()
        
        recurse(0, n, []) 
        return res