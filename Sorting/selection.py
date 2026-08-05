def sorting(nums):
    n = len(nums)

    for i in range(n - 1):
        print(f"Index is : {i}")
        for j in range(i + 1, 0 , -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break

arr = [2,5,1,78,65,43]
sorting(arr)
print(arr)