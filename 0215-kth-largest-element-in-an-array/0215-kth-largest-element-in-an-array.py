class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)

    def quickSelect(self, nums, start, end, target):
        if start == end:
            return nums[start]

        pivot = nums[random.randint(start, end)]

        low = start
        high = end

        while low <= high:
            while nums[low] > pivot:
                low += 1

            while nums[high] < pivot:
                high -= 1

            if low <= high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1

        if target <= high:
            return self.quickSelect(nums, start, high, target)

        if target >= low:
            return self.quickSelect(nums, low, end, target)

        return nums[target]
