class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multi = 1
        count = 0
        for num in nums:
            if num == 0:
                count += 1
                continue
            multi *= num
        
        if count > 1:
            for i,num in enumerate(nums):
                nums[i] = 0
            return nums

        for i,num in enumerate(nums):
            if num == 0:
                nums[i] = multi
            else:
                if count == 1:
                    nums[i] = 0
                else:
                    nums[i] = multi//nums[i]
        
        return nums