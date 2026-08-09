class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start = 0
        max_len = 1
        def expand_around_center(left: int, right: int) -> None:
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    start = left
                left -= 1
                right += 1
        
        for i in range(len(s)):
            expand_around_center(i, i)
            expand_around_center(i, i + 1)
        
        return s[start:start + max_len]