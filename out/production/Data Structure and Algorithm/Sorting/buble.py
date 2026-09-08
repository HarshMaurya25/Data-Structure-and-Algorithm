def sorting(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1, n - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

arr = [2,5,1,78,65,43]
sorting(arr)
print(arr)