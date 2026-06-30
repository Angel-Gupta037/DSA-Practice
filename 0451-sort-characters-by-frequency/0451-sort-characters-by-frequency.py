from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)

        sort=sorted(freq.keys(), key=lambda x: (-freq[x], x))

        res=""
        for char in sort:
            res+=char*freq[char]
    
        return res
        