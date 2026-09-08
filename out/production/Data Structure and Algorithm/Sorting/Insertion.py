def sorting(nums):
    n = len(nums)

    for i in range(n):
        max = 0
        for j in range(1,n-i):
            if nums[j] > nums[max]:
                max = j

        nums[n-i-1], nums[max] = nums[max], nums[n-i-1]

arr = [2,5,1,78,65,43]
sorting(arr)
print(arr)