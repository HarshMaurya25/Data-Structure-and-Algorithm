class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1

        prefix = 0
        ans = 0

        for i , num in enumerate(nums):
            prefix += num
            rem = prefix % k

            if rem in mp:
                ans += mp[rem]
            
            mp[rem] += 1

        return ans