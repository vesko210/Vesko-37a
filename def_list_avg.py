def list_avg(lst, multiplier = 1):
    count = 0 
    average = 0

    for i in lst:
        if type(i) == int or type(i) == float:
           average += i * multiplier
           count += 1
        elif type(i) == str:
            average += (int(i) * multiplier)
            count += 1
    if count == 0:
        print("Error: Division by zero")
    return average/count


print(list_avg(['4', 1.5, "@7$", 3.5, (1, "hi")]))
print(list_avg(['6', 3, 3.0], 2))
print(list_avg(['%$', {}]))
print(list_avg([]))

