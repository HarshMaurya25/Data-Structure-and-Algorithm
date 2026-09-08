class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}

        for idx , i in enumerate(nums):
            if hasmap.get(target - i) != None:
                return [idx , hasmap[target - i]]
            else:
                hasmap[i] = idx