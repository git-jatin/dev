a=[
    [1,2,3,4],
    [1,9,9,9],
    [1,2,9,4],
    [1,9,9,9],
    ]
n=len(a)
m=len(a[0])
print(n,m)
maxsum = -1
for i in range(n-2):
    for j in range(m-2):

        sum1 = (a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] +a[i+2][j] +a[i+2][j+1] +a[i+2][j+2])
        # i=0 j=1
        # 01 02 03 12 21 22 23
        maxsum = max(sum1,maxsum)

print(maxsum)


