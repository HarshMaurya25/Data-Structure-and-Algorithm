class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_index = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            rem = prefix % k

            if rem in rem_index:
                if i - rem_index[rem] >= 2:
                    return True
            else:
                rem_index[rem] = i

        return False