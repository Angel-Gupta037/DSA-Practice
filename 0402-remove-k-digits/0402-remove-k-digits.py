class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in range(len(num)):
            while st and k>0 and st[-1]>num[i]:#if right element is smaller then pop
                st.pop()
                k-=1
            st.append(num[i])   #push
        while k>0:          #if still smthng left in k to remove
            st.pop()
            k-=1
        while st and st[0]=='0': 
            st.pop(0)
        return ''.join(st)if st else "0" #for triling zeros
        
        