def Number_delitels (a):
    sum = 0
    for i in range(1, a+1):
        if a % i == 0:
            sum +=1
    return(sum)
print(Number_delitels(1))