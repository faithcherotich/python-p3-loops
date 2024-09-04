#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")    
    

def square_integers(int_list):
    # code goes here!
    return [x ** 2 for x in int_list]
numbers = [1,2,3,4,5]
squared_numbers = square_integers(numbers) 
print(squared_numbers)  

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 ==0:
            print('Fizz')  
        elif i % 5 == 0:
            print('Buzz')  
        else:
            print(i)  
