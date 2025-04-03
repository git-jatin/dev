
def arr(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i]==a[j]:
                count=count+1

            else:
                print("no duplicate")
    return count

a=[3,4,5,6,7,7,7]
print(arr(a))

