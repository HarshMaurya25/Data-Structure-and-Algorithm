class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]

        for i in range(1 , len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        # print(prefix)
        ans = -1

        for i in range(0 , len(nums)):
            beforei = 0
            afteri = prefix[-1]
            if i != 0:
                beforei = prefix[i - 1]

            if i + 1 != len(nums):
                afteri = prefix[i]

            # print(f"{i}  {prefix[-1] - afteri} {beforei} {prefix[i - 1]} {i != 0}")
            if prefix[-1] - afteri == beforei:
                ans = i
                break

        return ans