class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=-1
        if len(weights)<days:
            return -1
        while low<=high:
            mid=(low+high)//2
            day=1
            total=0
            for num in weights:
                if total+num<=mid:
                    total+=num
                else:
                    day+=1
                    total=num
            if day<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        