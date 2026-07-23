class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)

        def checking(mid):
            ans = 0
            for i in nums:
                ans += -(-i // mid)

                #print(f"Mid = {mid} , i : {i} and answer : {-(-i // mid)} and ANS : {ans}")
            return ans

        answer = high
        while(low <= high):
            mid = low + (high - low) // 2
            checks = checking(mid)

            print(f"Mid : {mid} and Checks : {checks}")
            if(checks <= threshold and answer > mid):
                answer = mid

            if(checks > threshold):
                low = mid + 1
                
            else:
                high = mid - 1
    

        return answer

