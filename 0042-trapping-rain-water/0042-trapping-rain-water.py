class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 1
        ans = 0
        temp = 0 

        size = len(height)
        if size <= 2:
            return 0
        
        while right < size:
            if height[left] == 0:
                left += 1
            if left == right:
                right += 1
            else:
                if height[left] <= height[right]:
                    ans += temp
                    left = right
                    temp = 0
                else:
                    temp += height[left] - height[right]
                    right += 1
            print(f"{left} {right} {temp} {ans}")

        if left >= size - 2:
            return ans

        x , y = size - 2 , size - 1
        temp = 0

        while x >= left:
            if height[y] == 0:
                y -= 1
            if y == x:
                x -= 1
            else:
                if height[y] <= height[x]:
                    ans += temp 
                    y = x
                    temp = 0
                else:
                    temp += height[y] - height[x]
                    x -= 1
        
        return ans