a=[4, 3, 6, 2, 1, 1]
a.sort()
n=len(a)
st=0
miss=0
for i in range(n-1):
    s=a[i]+1
    if s!=a[i+1] and a[i+1]!=a[i]:
         miss=s


    for j in range(i+1,n):
        if a[i]==a[j]:
            st=a[i]

print(st,miss)