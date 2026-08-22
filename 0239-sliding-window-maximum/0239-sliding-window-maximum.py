class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        st=[]
        
        n=len(nums)
        arr=[0]*(n-k+1)
        l,r=0,k-1
        for i in range(n):
            while st and nums[st[-1]]<=nums[i]:
                st.pop()
            st.append(i)
            if st[0] <= i - k: #remove ele not in the sliing window
                st.pop(0)
            if i >= k - 1:#adds vals to the max-list
                arr[i - k + 1] = nums[st[0]]
        return arr
        