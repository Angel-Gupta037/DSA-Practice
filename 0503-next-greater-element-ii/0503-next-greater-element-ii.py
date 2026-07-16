class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[-1]*n #new array
        st=[]
        for i in range(2*n-1,-1,-1):
            ind=i%n #for initalize for circular array
            curr=nums[ind] 
            while st and st[-1]<=curr:
                st.pop()
            if i<n:
                #greater ele is not found, st is empty
                arr[i]=st[-1] if st else -1
                
            #push curr ele in the st
            st.append(curr)
        return arr


        