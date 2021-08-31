
def countdown(num):
    num_list = []
    for i in range(num, -1, -1):
        print(i)
        num_list.append(i)
    return num_list

print(countdown(7))

def print_and_return(list):
    # print(list)
    print(list[0])
    print(list[1])

print (print_and_return([3,5]))

def first_plus_length(list):
    return list[0] + len(list)

print (first_plus_length([3,5,6,2,9]))

def values_bigger_than_second(list):
    new_list = []
    for i in range(0, len(list)):
        if list[i] > list[1]:
            # print(i)
            new_list.append(list[i])
    return new_list

print (values_bigger_than_second([5,2,6,7,1,9]))

def size_and_value(size, value):
    new_list = []
    for i in range (size, 0, -1):
        new_list.append(value)
    return new_list

print (size_and_value(6,"D"))