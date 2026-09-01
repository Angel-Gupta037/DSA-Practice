class Solution:
    def minDays(self, bd: List[int], m: int, k: int) -> int:
        low=1
        high=max(bd)
        ans=-1
        if len(bd)<(m*k):
            return -1
        while low<=high:
            mid=(low+high)//2
            bouquet=0
            consecutive=0
            
            for day in bd:
                if day<=mid:
                    consecutive+=1

                    if consecutive==k:
                        bouquet+=1
                        consecutive=0
                else:
                    consecutive=0

            if bouquet>=m:
                high=mid-1
                ans=mid
            else:
                low=mid+1
        return ans


