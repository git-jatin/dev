from fontTools.merge.util import first


def rotate(arr,d):
    n=len(arr)

    for i in range (d):
        first=arr[0]
        for j in range(n-1):
            arr[j]=arr[j+1]
        arr[n-1]=first


    for i in range (n):
        print(arr[i])
arr=[1,2,4,5]
d=3
rotate(arr,d)