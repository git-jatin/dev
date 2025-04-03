da=input("input the  the string :")
def pall(a):

    if a == a[::-1]:
       return "Pallindrome string:",a
    else:
        return "not pallindrome :",a
print(pall(a))

