class Solution:
    def findKRotation(self, nums):
        def solution(l , h):
            m = l + (h - l)//2

            if(nums[l] <= nums[h]):
                return l
            elif(nums[l] <= nums[m]):
                return solution(m + 1 , h)
            else:
                return solution(l , m )

        ans = solution(0 , len(nums) - 1) 
        return ans 

question = Solution()
a = [4, 5, 1, 2]
print(question.findKRotation(a))