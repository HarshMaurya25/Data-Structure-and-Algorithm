def quick(num, start , end):
    if (start >= end):
        return 

    l = start
    h = end
    mid = (l + h)//2

    pivot = num[mid]

    while(l <= h):
        while num[l] < pivot:
            l += 1
        while num[h] > pivot:
            h -= 1

        if (l <= h):
            num[l], num[h] = num[h] , num[l]
            l+=1
            h -=1

    quick(num , start , h)
    quick(num , l , end)

arr = [2,5,1,78,65,43]
quick(arr , 0 , len(arr)-1)
print(arr)