class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res=[]
        row=len(board)
        col=len(board[0])
        def help(r,c,remain,ds):    
            if remain==0:
                res.append(ds[:])
                return True

            if r < 0 or r >= row or c < 0 or c >= col:
                return False
            if board[r][c] != word[len(word) - remain]:
                return False

            # Mark visited
            temp = board[r][c]
            board[r][c] = '#'
            found = False

            if help(r, c+1, remain-1, ds):
                found = True
            if help(r, c-1, remain-1, ds):
                found = True
            if help(r+1, c, remain-1, ds):
                found = True
            if help(r-1, c, remain-1, ds):
                found = True

            # Backtrack
            board[r][c] = temp
            return found

        for r in range(row):
                for c in range(col):
                    if board[r][c] == word[0]:  # First letter match
                        if help(r, c, len(word), []):
                            return True
            
        return False
