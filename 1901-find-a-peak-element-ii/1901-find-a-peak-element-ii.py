class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        l = 0
        r = col - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            max_row = 0
            for i in range(row):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
            
            left_val = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
            right_val = mat[max_row][mid + 1] if mid + 1 < col else -1
            
            if mat[max_row][mid] > left_val and mat[max_row][mid] > right_val:
                return [max_row, mid]
            
            if left_val > mat[max_row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return [-1, -1]