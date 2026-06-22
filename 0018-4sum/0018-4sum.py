class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        n=sorted(nums)
        for i in range(len(n)):
            if i>0 and n[i]==n[i-1]: continue
            for j in range(i+1, len(n)):
                if j>i+1 and n[j]==n[j-1]: continue
                k = j+1        # ← reset here!
                l = len(n)-1   # ← reset here!
                while k<l:
                    sum=0
                    sum+=n[i]+n[j]+n[k]+n[l]
                    if sum==target:
                        res.append([n[i],n[j],n[k],n[l]])
                        k+=1
                        l-=1
                        while k<l and n[k]==n[k-1]:
                            k+=1
                        while k<l and n[l]==n[l+1]:
                            l-=1
                    elif sum<target:
                            k+=1
                    else: l-=1
        return res
