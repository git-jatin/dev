from fontTools.misc.cython import returns


def sub(a,n):
 n=len(a)
 big_sub=""
 for i in range(n):
    s=""
    s+=a[i]

    for j in range(i+1,n):
        if a[j] not in s:
            s+=a[j]
        else:
            break
    if len(s)>len(big_sub):
            big_sub=s

 return big_sub

arr = "aaa"
n=len(arr)
big_sub=sub(arr,n)

print(big_sub)