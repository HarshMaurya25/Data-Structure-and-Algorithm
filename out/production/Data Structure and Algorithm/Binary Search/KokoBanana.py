class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxs = max(piles)
        print(h ,len(piles))
        if(h == len(piles)):
            
            print("Enter maxs")    
            return maxs

        ans = -1

        low = 1
        high = maxs

        def checking(i):
            answer = 0
            for j in piles:
                # print(i , answer , -(-j // i))
                answer += -(-j // i)

            return answer

        print("Enter WHile")
        while(low <= high):
            mid = low + (high - low)//2

            checks = checking(mid)
            print("Solution of the ",mid , checks , low , high)

            if(checks <= h):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans