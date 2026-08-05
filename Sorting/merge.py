def mergesort(num , start , end):
    if end - start <= 1:
        
        return 
    mid = (start + end)//2
    mergesort(num , start , mid)
    mergesort(num , mid , end)
    mergeSorting(num , start , mid , end)

def mergeSorting(num , start , mid , end):
    temp = []

    i = start
    j = mid
    k = 0

    while (i < mid and j < end):
        if num[i] > num[j]:
            temp.append(num[j])
            j+=1
        else:
            temp.append(num[i])
            i+=1

    while i < mid:
        temp.append(num[i])
        i+=1
    while j < end:
        temp.append(num[j])
        j+=1

    for i in range(end - start):
        num[start + i] = temp[i]

arr = [2,5,1,78,65,43]
mergesort(arr , 0 , len(arr))
print(arr)