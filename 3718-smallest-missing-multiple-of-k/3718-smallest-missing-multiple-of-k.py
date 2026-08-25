class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen=set()
        multiple=k
        while multiple in nums:
            multiple+=k
        return multiple
        