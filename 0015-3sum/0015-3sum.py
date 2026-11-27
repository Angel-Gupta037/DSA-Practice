class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            # early exit: smallest remaining value is positive → no zero sum possible
            if nums[i] > 0:
                break
            # skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            target = -nums[i]

            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicate l values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # skip duplicate r values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return res