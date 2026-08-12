class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            #get frequency
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1 #shrink if more
                if freq[nums[left]] == 0:
                    del freq[nums[left]] 
                left += 1
            max_len = max(max_len, right - left + 1)#find length
        
        return max_len