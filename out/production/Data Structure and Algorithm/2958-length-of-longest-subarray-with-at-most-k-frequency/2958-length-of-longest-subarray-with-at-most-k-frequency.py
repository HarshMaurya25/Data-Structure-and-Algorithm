class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)

        i = 0
        ans = 0

        for j in range(len(nums)):
            freq[nums[j]] += 1

            while freq[nums[j]] > k:
                freq[nums[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)

        return ans