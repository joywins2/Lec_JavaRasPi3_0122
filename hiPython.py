print("Hi,Python! I am JoyWins!")

def average(num_list):
    avg = 0
    for n in num_list:
        avg = avg + n
    avg = avg / len(num_list)
    return avg

# Should print 5.0
list_1 = [4, 7, 9, 0]
print(average(list_1))

# Should print 4.406333333333
list_2 = [-3.2, 6.419, 10]
print(average(list_2))

# Should print 42.0
list_3 = [42]
print(average(list_3))
