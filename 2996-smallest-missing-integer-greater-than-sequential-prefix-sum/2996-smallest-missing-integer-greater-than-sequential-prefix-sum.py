class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = set(nums)

        prefix_sum = nums[0]
        i = 1

        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
            i += 1

        while prefix_sum in s:
            prefix_sum += 1

        return prefix_sum