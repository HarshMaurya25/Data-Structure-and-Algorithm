class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        wmax = 0
        wsum = 0 

        for i in weights:
            wmax = max(wmax , i)
            wsum += i
        
        def checks(capcity):
            loaded = 0
            day = 1
            for i in weights:
                # print(loaded , i , day)
                if loaded + i <= capcity:
                    loaded += i
                else:
                    day += 1
                    loaded = i
            
            return day

        low = wmax
        high = wsum
        ans = -1
        while(low <= high):
            mid = low + (high - low)//2

            possible = checks(mid)
            # print(mid , possible)
            if possible <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans