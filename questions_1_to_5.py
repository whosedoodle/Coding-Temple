#Question 1: Write a function to print "hello_USERNAME!" 
#USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print(f"Hello {user_name}")
hello_name(user_name=input("What is your username?: "))

#Question 2: Write a python function, first_odds that 
#prints the odd numbers from 1-100 and returns nothing

def first_odds():
    numbers = list(range(1,101,2))
    print(numbers)

(first_odds())

#Question 3: Please write a Python function, max_num_in_list to return the
#max number of a given list. The first line of the code has been defined 
#as below.

def max_num_in_list(a_list):
    a_list = [1,6,4,23,54,3,6,9]
    return print(max(a_list))

max_num_in_list(list)

#Question 4: Write a function to return if the given year is a leap year. 
#A leap year is divisible by 4, but not divisible by 100, unless it is 
#also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    return True if a_year%4 == 0 else False

print(is_leap_year(a_year=int(input("What year would you like to check?: "))))

#Question 5: Write a function to check to see if all numbers in list 
#are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, 
#but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    a_list = [1,3,5,6,3]
    return a_list == sorted(a_list)

print(is_consecutive(list))