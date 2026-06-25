class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        cnt1=0
        cnt2=0
        el1,el2=0,0
        for i in range(n):
            if cnt1==0 and nums[i]!=el2:
                cnt1=1
                el1=nums[i]
            elif cnt2==0 and nums[i]!=el1:
                cnt2=1
                el2=nums[i]
            elif el1==nums[i]:
                cnt1+=1
            elif el2==nums[i]:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        result = []
        if nums.count(el1) > n//3:
            result.append(el1)
        if nums.count(el2) > n//3 and el2 != el1:
            result.append(el2)
        
        return result
                
                
        