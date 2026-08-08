class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            if k < 0:
                return 0
            left = 0
            count = 0
            odd_count = 0
            for right in range(len(nums)):
                odd_count += nums[right] % 2
                while odd_count > k:
                    odd_count -= nums[left] % 2
                    left += 1
                count += right - left + 1
            return count
        return atMost(k) - atMost(k - 1)
        