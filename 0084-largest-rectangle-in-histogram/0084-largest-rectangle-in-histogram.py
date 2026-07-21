class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        n = len(heights)
        ls = [0] * n  
        rs = [0] * n  
        
        # NSL 
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            ls[i] = st[-1] + 1 if st else 0 
            st.append(i)
        
        # Clear stack for NSR
        st = []  
        
        # NSR 
        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            rs[i] = st[-1] - 1 if st else n - 1  
            st.append(i)
        
        #max area
        maxA = 0
        for i in range(n):
            width = rs[i] - ls[i] + 1
            maxA = max(maxA, heights[i] * width)
        
        return maxA