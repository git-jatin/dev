def con(a):
 n=len(a)

 m=0
 for i in range(n):
    count = 0
    for j in range(n):
        if a[i]==a[j]:

            count+=1

    if count > m:
        m=count
        value=a[i]
 print(f"{value}:{m}")
a=[1,0,1,1,0,0,0,0,1]
con(a)





