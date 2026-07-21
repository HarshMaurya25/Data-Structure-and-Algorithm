class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def solution(l , h):
            m = l + (h - l)//2

            if(l > h ):
                return False
            elif(nums[m] == target):
                return True
            if nums[l] == nums[m] == nums[h]:
                l += 1
                h -= 1
                return solution(l, h)
            if(nums[l] <= nums[m]):
                if(nums[m] > target and target >= nums[l]):
                    return solution(l , m - 1)
                else:
                    return solution(m + 1 , h)
            else:
                if(nums[m] < target and target <= nums[h]):
                    return solution(m + 1 , h)
                else:
                    return solution(l , m - 1)
        
        return solution(0 , len(nums) - 1)

                
        