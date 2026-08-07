class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i , num in enumerate(nums):
            if i == 0:
                continue
            self.nums[i] = self.nums[i] + self.nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        num = 0 
        if left >= 1:
            num = self.nums[left - 1]
        print(num , self.nums[right])
        return self.nums[right] - num


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)