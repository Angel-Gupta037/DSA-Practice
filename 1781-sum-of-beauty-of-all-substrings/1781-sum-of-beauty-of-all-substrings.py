class Solution:
    def beautySum(self, s: str) -> int:
        count = 0
        l = len(s)
        for i in range(l):
            freq = {}
            for j in range(i, l):
                freq[s[j]] = freq.get(s[j], 0) + 1
                values = freq.values()
                count += max(values) - min(values)
        return count
                
                