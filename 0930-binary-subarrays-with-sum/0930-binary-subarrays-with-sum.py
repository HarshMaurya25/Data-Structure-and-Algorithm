class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap = defaultdict(int)
        ans = 0
        prefix = 0
        hashmap[0] = 1
        for num in nums:
            prefix += num
            ans += hashmap[prefix - goal]
            hashmap[prefix] += 1
        return ans