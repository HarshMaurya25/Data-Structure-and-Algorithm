class Solution:

    def splitSum(self , nums , mid , p ):
        nSum = 0

        maximum = 0
        count = 1
        for i in nums:
            if(nSum + i <= mid):
                nSum += i
            else:
                maximum = max(maximum , nSum)
                nSum = i
                count += 1

        maximum = max(maximum , nSum)
        return [count, maximum]

    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        ans = high
        while low <= high:
            mid = (low + high) // 2

            splitSum = self.splitSum(nums , mid , k)

            print(f"Low : {low} , high : {high} and mid : {mid} ---> {splitSum}")
            if(splitSum[0] <= k):
                ans = splitSum[1]
                high = mid - 1
            else:
                low = mid + 1
        
        return ans


