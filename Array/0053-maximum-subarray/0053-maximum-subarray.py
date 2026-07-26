class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')

        count = 0
        for i in nums:
            count += i
            ans = max(count , ans)
            if count < 0:
                count = 0
        
        return ans