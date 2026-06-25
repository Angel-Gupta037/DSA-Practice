class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m-1      # last real element of nums1
        p2 = n-1      # last element of nums2
        p3 = m+n-1    # last index of nums1

        while p1>=0 and p2>=0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1     # ← p3 always moves regardless!

        while p2>=0:   # remaining nums2 elements
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1