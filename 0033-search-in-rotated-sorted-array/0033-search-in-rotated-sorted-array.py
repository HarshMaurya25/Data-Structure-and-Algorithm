class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def middle():
            return (low + high)//2

        low = 0
        high = len(nums) - 1
        mid = middle()

        while low <= high:
            mid = middle()

            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:

                if nums[mid] >= target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        
        return -1