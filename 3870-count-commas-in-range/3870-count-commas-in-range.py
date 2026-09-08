class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        
        # Power of 1000: 1000, 1000000, 1000000000, ...
        power = 1000
        commas = 1
        
        while power <= n:
            # Count numbers from 'power' to min(n, power*1000 - 1)
            end = min(n, power * 1000 - 1)
            total += (end - power + 1) * commas
            
            # Move to next range
            power *= 1000
            commas += 1
        
        return total 