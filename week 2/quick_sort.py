def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        povit = arr[-1]
        l_arr=[]
        r_arr=[]
        for i in range(len(arr)-1):
            if arr[i]<povit:
                l_arr.append(arr[i])
            else:
                r_arr.append(arr[i])
        return quick_sort(l_arr)+[povit]+quick_sort(r_arr)
arr=[1,5,3,2,9,7,5,4,0,9,8,7,5,4,3]
arr2 =[5,5,5,5,5,5,5]
print(quick_sort(arr))
print(quick_sort(arr2))
