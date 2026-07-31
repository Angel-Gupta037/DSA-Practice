class Solution:
    def minimumPushes(self, word: str) -> int:
        freq={}
        s=0
        for char in word:
            freq[char]= freq.get(char,0)+1
        sorted_freq = sorted(freq.values(), reverse=True)
        totalp=0
        p=1
        for i, count in enumerate(sorted_freq):
            if i > 0 and i % 8 == 0:
                p += 1

            totalp+=count*p
        return totalp
