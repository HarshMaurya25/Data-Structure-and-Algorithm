class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        for i in range(k):
            temp = nums[len(nums) - 1]
            for idx in range(len(nums) - 2 , -1, - 1):
                nums[idx + 1] = nums[idx]
            nums[0] = temp

# Time : O(n * k)
# Space: O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        arr = []
        length = len(nums)
        for idx, i in enumerate(nums):
            x = (length - k + idx) % length
            arr.append(nums[x])
            # print(arr , x , nums[x])
        
        nums[:] = arr

# Time : O(n)
# Space: O(n)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k %= l
        count = 0
        for i in range(k):
            # print(l - k + i)
            nums.insert(count , nums[l - k + i + count])
            count +=1
        for i in range(k):
            nums.pop()

# Time : O(n*k)
# Space : O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k %= l
        for i in range(l - k ):
            nums.append(nums[0])
            nums.pop(0)

# Time : O(n - k)
# Space : O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
# Time : O(n)
# Space : O(1)