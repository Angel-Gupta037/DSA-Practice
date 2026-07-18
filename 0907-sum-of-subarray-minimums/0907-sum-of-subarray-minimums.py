class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def findnse(arr):
            n=len(arr)
            ans=[0]*n
            st=[]
            for i in range(n-1,-1,-1):
                curr=arr[i]
                while st and arr[st[-1]]>=curr: #if stack is not empty and top ele is not smaller
                    st.pop() #pop them
                if st:          #update ans since st is not empty
                    ans[i]=st[-1]
                else:
                    ans[i]=n
                st.append(i)
            return ans
        
        def findpse(arr):
            n=len(arr)
            ans=[0]*n
            st=[]
            for i in range(n):
                curr=arr[i]
                while st and arr[st[-1]]>curr: #if stack is not empty and top ele is not smaller
                    st.pop() #pop them
                if st:          #update ans since st is not empty
                    ans[i]=st[-1]
                else:
                    ans[i]=-1
                st.append(i)
            return ans
        
        mod = 10**9 + 7
        n=len(arr)
        nse=findnse(arr)
        pse=findpse(arr)
        total=0
        for i in range(n):
            # Count of first type of subarrays
            left = i - pse[i]
            # Count of second type of subarrays
            right = nse[i] - i
            # Count of subarrays where current element is minimum
            freq = left * right * 1
            val=(freq*arr[i])%mod
            total= (total+val)%mod
        return total




        