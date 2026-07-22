class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def firstOccurrence():
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            if low < len(nums) and nums[low] == target:
                return low
            return -1

        def lastOccurrence():
            low = 0
            high = len(nums) - 1
            ans = -1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] <= target:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1

            if ans != -1 and nums[ans] == target:
                return ans
            return -1

        return [firstOccurrence(), lastOccurrence()]