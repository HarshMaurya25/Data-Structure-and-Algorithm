class Solution:
    def maxArea(self, height: List[int]) -> int:
        i , j = 0 , len(height) - 1

        maxi = 0
        while i < j:
            num1= height[i]
            num2 = height[j]

            maxi = max(maxi , min(num1 , num2) * (j - i))
            if num1 < num2:
                i += 1
            else:
                j -= 1
        
        return maxi