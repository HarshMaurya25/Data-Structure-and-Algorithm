class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def solution(l , h):
            m = l + (h - l)//2

            if(l - h == 0):
                return l
            
            if(l - h == 1):
                return l if(l > h) else h

            if(nums[m + 1] < nums[m] > nums[m - 1]):
                return m

            elif(nums[m + 1] > nums[m]):
                return solution(m + 1 , h)
            else:
                return solution(l , m - 1)
        
        return solution(0 , len(nums) - 1)