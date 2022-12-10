# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 

def hello_name(user_name):
   print("hello_" + user_name + '!')

hello_name('Jon')

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
   print(list(range(1,100,2)))

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 

def max_num_in_list(a_list):
    b_list = []
    for x in a_list:
        if isinstance(x, int):
            b_list.append(x)
    print(max(b_list))

max_num_in_list([4, 'apple', 90, 57, 18, 7])

# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    x = False
    if a_year % 100 == 0 and a_year % 400 == 0:
        x = True
    elif a_year % 4 == 0 and not a_year % 100 == 0:
        x = True
    return(x)
    
print(is_leap_year(200))
print(is_leap_year(400))
print(is_leap_year(12))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    c = True
    a_list.reverse()
    for x in range(len(a_list) - 1):
        if (a_list[x] - a_list[x + 1] != 1):
            c = False
            break
        else:
            continue
    return(c)

print(is_consecutive([1, 2, 3, 4, 5]))
print(is_consecutive([1, 4, 6, 7, 9]))