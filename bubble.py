def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)

arr=[9,8,7,6,5,4,70,2,1]
bubble(arr)
print(arr)

