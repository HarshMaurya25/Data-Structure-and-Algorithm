class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insertPos = 0

        for num in nums:
            if num != 0:
                nums[insertPos] = num
                insertPos += 1

        while insertPos < len(nums):
            nums[insertPos] = 0
            insertPos += 1