a=[-12,-3,-6,-10]
a.sort()
result=1
for i in range(len(a)):
    s=a[::-1]
print(s)
for j in range(3):
    print(s[j])
    result *=s[j]
print(result)



