class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low = 2
        high = x // 2
        ans = 1

        while low <= high:
            mid = low + (high - low) // 2

            if mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans