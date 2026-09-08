class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, start, end):
        if start >= end:
            return

        low = start
        high = end

        pivot = nums[random.randint(start, end)]

        while low <= high:
            while nums[low] < pivot:
                low += 1

            while nums[high] > pivot:
                high -= 1

            if low <= high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1

        self.quickSort(nums, start, high)
        self.quickSort(nums, low, end)