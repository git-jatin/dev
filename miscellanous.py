
a=input("input the  the string :")
def pall(a):
    s="".join(c.lower()for c in a if c.isalnum())


    print(s)


    if s == s[::-1]:
       return "Pallindrome string:",a
    else:
        return "not pallindrome :",a
print(pall(a))


