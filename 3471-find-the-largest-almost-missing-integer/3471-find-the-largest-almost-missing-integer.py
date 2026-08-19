class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        #all subarray
        #track frequency of all sunarray
        #find largest in len-1 subarray
        n=len(nums)
        freq={}
        for i in range(n-k+1):
            seen=set()#this avoids duplicates
            for j in range(i,i+k):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    freq[nums[j]]=freq.get(nums[j],0)+1
        maxx=-1
        for num,cnt in freq.items():
            if cnt==1:
                maxx=max(maxx,num)
        return maxx
        