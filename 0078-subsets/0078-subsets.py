class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        def subsets(i):
            if i == len(nums):
                return [[]]

            result = subsets(i + 1)

            return result + [[nums[i]] + subset for subset in result]

        return subsets(0)