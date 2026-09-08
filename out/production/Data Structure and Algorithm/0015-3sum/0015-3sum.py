class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        ans = []
        print(nums)
        for i in range(0 , len(nums) - 1):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                add = nums[i] + nums[j] + nums[k]
                # print(f"i : {i}({nums[i]}) , j : {j}({nums[j]}) , k : {k}({nums[k]}) Add : {add} {[nums[i] , nums[j] , nums[k]]}")

                if add == 0:
                    ans.append([nums[i] , nums[j] , nums[k]])
                    if nums[j] == nums[j + 1]:
                        while j < k and nums[j] == nums[j+1]:
                            j += 1
                        j += 1
                    else:
                        j += 1
                    if nums[k] == nums[k - 1]:
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1
                        k -= 1
                    else:
                        k -= 1

                elif add < 0:
                    j += 1
                else:
                    k -= 1
        
        return ans