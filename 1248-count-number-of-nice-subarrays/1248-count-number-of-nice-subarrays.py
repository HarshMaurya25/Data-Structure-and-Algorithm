class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        odd_count = 0
        ans = 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1

            if odd_count - k in hashmap:
                ans += hashmap[odd_count - k]

            hashmap[odd_count] = hashmap.get(odd_count, 0) + 1

        return ans
