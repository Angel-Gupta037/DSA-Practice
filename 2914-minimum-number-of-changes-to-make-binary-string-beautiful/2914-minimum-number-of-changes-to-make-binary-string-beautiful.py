class Solution:
    def minChanges(self, s: str) -> int:
        cnt = 0
        i = 0
        while i < len(s):
            if s[i] != s[i + 1]:
                cnt += 1
            i += 2
        return cnt
        