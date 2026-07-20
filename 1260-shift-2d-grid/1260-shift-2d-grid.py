class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        k %= rows * cols
        flat=[]
        # Flatten and rotate 
        for i in range(rows):
            for j in range(cols):
                flat.append(grid[i][j])
        rotated = flat[-k:] + flat[:-k] if k else flat
       
        return [rotated[i*cols:(i+1)*cols] for i in range(rows)]