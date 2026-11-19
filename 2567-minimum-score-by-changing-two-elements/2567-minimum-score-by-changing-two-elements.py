class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        # Three ways to spend 2 changes on extremes
        return min(
            nums[-1] - nums[2],      # change two smallest
            nums[-3] - nums[0],      # change two largest
            nums[-2] - nums[1],      # change one smallest + one largest
        )