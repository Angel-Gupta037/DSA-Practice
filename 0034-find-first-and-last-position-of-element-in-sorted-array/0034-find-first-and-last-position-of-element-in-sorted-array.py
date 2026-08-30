class Solution:
    def searchRange(self, n: List[int], target: int) -> List[int]:
        low=0
        high=len(n)-1
        first=-1
        while low<=high:
            mid=(low+high)//2
            if n[mid]==target:
                first=mid
                high=mid-1 
            elif n[mid]<target:
                low=mid+1
            else:
                high=mid-1
        low=0
        high=len(n)-1
        last=-1
        while low<=high:
            mid=(low+high)//2
            if n[mid]==target:
                last=mid
                low=mid+1 
            elif n[mid]<target:
                low=mid+1
            else:
                high=mid-1 
        return [first,last]  


        