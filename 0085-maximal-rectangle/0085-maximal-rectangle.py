class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestmsxarea(height):
            height.append(0) #sentinel
            st=[]
            maxarea=0
            for i in range (len(height)):
                while st and height[i]<height[st[-1]]:
                    h=height[st.pop()]
                    width=i if not st else i-st[-1]-1
                    maxarea=max(maxarea,h*width)

                st.append(i)
            height.pop()
            return maxarea
        if not matrix:return 0
        m=len(matrix[0])
        height=[0]*m
        maxarea=0
        for r in matrix:
            for i in range(m):
                if r[i]=='1':
                    height[i]+=1
                else:
                    height[i]=0
            maxarea=max(maxarea,largestmsxarea(height))
        return maxarea
        