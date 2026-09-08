class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        low, high = 0, m

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX

            L1 = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            R1 = float('inf') if partitionX == m else nums1[partitionX]

            L2 = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            R2 = float('inf') if partitionY == n else nums2[partitionY]

            if L1 <= R2 and L2 <= R1:
                if (m + n) % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                else:
                    return max(L1, L2)

            elif L1 > R2:
                high = partitionX - 1
            else:
                low = partitionX + 1