class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        left = 0
        ones = 0
        for right in range(n): #cnt 1s
            if s[right] == '1':
                ones += 1
            # Shrink window from left while enough 1s
            while ones == k:
                curr = s[left:right+1] #len of curr str
                if ans == "" or len(curr) < len(ans) or (len(curr) == len(ans) and curr < ans):
                    ans = curr
                
                # Remove left character
                if s[left] == '1':
                    ones -= 1
                left += 1
        
        return ans



            