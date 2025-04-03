


def ar(buy):
    l = len(buy)
    profit = 0
    for i in range(l):
        for j in range(i+1,l):
            profit= max(profit,buy[j]-buy[i])
    return profit
buy=[2,3,5,6,8,9]
print(ar(buy))



#Iteration 1: profit = max(0, 3 - 2)  → profit = 1
#Iteration 2: profit = max(1, 5 - 2)  → profit = 3
#Iteration 3: profit = max(3, 6 - 2)  → profit = 4
#Iteration 4: profit = max(4, 8 - 2)  → profit = 6
#Iteration 5: profit = max(6, 9 - 2)  → profit = 7