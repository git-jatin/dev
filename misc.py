from numpy.ma.core import maximum

s=["geeks","for","geeks" ,"for" ,"geeks" , "aaa"]
n=len(s)
max=0
sec=0

for i in range(n):
    count = 0
    for j in range(n):
        if s[i]==s[j]:
            count += 1
    print(f"{s[i]}:{count}")
    if count > max:
        print(count)
    elif count >sec:
        print (sec)

