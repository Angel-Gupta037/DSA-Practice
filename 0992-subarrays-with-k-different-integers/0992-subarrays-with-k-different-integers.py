class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmostk(K:int) -> int:
            if K==0:
                return 0
            freq={}
            l=0
            cnt=0
            for r in range(len(nums)):
                freq[nums[r]]=freq.get(nums[r],0)+1

                while len(freq)>K:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        del freq[nums[l]]
                    l+=1

                cnt+=r-l+1
            return cnt

        return atmostk(k) - atmostk(k-1)
