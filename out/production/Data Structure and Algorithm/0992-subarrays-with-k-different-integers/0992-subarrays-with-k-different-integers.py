class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMost(k):
            freq = {}
            left = 0
            ans = 0

            for right in range(len(nums)):
                freq[nums[right]] = freq.get(nums[right], 0) + 1

                while len(freq) > k:
                    freq[nums[left]] -= 1

                    if freq[nums[left]] == 0:
                        del freq[nums[left]]

                    left += 1

                ans += right - left + 1

            return ans

        return atMost(k) - atMost(k - 1)
