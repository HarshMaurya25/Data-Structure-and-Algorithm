class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        even = 0
        odd = 0 
        ans = [0 for _ in range(len(nums))]

        for i in nums:
            # print(f"{i} is the Even number : {i % 2 == 0} so even : {even * 2} or odd : {odd * 2 + 1}")
            if i >= 0:
                ans[even * 2] = i
                even += 1
            else:
                ans[odd * 2 + 1] = i
                odd += 1

        return ans