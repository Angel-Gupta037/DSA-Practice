class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq=Counter(s)
        half=[]
        m=""
        if len(s)==1:
            return s
        for char in sorted(freq.keys()):
            count=freq[char]
            half.append(char*(count//2))
            if count%2==1:
                m=char 

        left_half = "".join(half)
        right_half = left_half[::-1]  # Reverse the left half

        return left_half + m + right_half       