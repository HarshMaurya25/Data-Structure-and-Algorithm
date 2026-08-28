class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hashmap = {}
        hashmap[0] = -1
        ans = 0
        odd_count = 0

        for idx, num in enumerate(nums):
            if num%2 == 1:
                odd_count += 1

            if odd_count not in hashmap:
                hashmap[odd_count] = idx

            if odd_count < k:
                continue
            
            ans += hashmap.get(odd_count - k + 1) - hashmap.get(odd_count - k)

        return ans