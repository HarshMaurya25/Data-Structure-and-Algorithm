class Solution:
    def findMin(self, nums: List[int]) -> int:
        def solution(l , h):
            m = l + (h - l)//2

            if(nums[l] <= nums[h]):
                return nums[l]
            elif(nums[l] <= nums[m]):
                return solution(m + 1 , h)
            else:
                return solution(l , m )

        return solution(0 , len(nums) - 1)