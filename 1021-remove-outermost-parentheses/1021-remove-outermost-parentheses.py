class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st=[]
        res=[]
        for char in s:
            if char=='(':
                if st:
                    res.append(char)
                st.append(char)
            else:
                st.pop()
                if st:
                    res.append(char)
        return ''.join(res)

        