#Two Sum – Pair with given Sum
a=[1,2,3,4]
sum=5
n=len(a)
def add(a,sum):
    for i in range(n):
        for j in range(i+1,n):
            if a[i]+a[j]==sum:
                print("found ")
            else:
                print("not found")

print(add(a,sum))

