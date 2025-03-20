A=[1,2,3,4,5,6,7,8,9]
item=9
low=0
high=len(A)-1
if low<=high:
    mid=int((low+high)/2)
    if A[mid]==item:
        print("item found",item)
    elif A[mid]>item:
        high=mid-1
        print("item found",high)
    elif A[mid]<item:
        low=mid+1
        print("item found ",low)

else:
    print ("does not print")