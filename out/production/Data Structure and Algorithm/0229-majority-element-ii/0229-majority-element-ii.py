class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}

        for num in nums:
            if hashmap.get(num):
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        ans = []
        for h, s in hashmap.items():
            if s > len(nums)/3:
                ans.append(h)

        return ans