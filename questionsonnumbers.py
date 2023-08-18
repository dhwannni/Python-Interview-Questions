#Python Coding Questions
#https://quescol.com/interview-preparations/python-coding-question

#Python Coding Questions on Numbers

#1- Reverse an integer 
#using [::-1] & array is given
nums = [1, 2, 3, 4]
rev = nums[::-1]
print(rev)
#input type 
num = int(input("Enter a number:"))
print("This is the number before reversing: ", num)
rev = int(str(num)[::-1])
print("This is the number after reversing: " , rev)

#2- Armstrong number
def is_armstrong(num):
    # Convert the number to a string and get its length
    num_str = str(num)
    num_len = len(num_str)

    # Calculate the sum of the digits raised to the power of the number of digits
    sum_of_powers = sum([int(digit) ** num_len for digit in num_str])

    # If the sum is equal to the original number, it's an Armstrong number
    return sum_of_powers == num

#3-Prime number
num = int(input("Enter a number: "))
if num == 2:
    print("This number is prime: ", num)
elif num % 2 == 0:
    print("The number is not prime: ", num)
else:
    print("The number is prime: ", num)

#8- Greatest among integers
#input type 
a = int(input("Enter 1 number: "))
b = int(input("Enter 1 number: "))
c = int(input("Enter 1 number: "))
if a>b and a>c:
    print("The max is:", a)
elif a<b and b>c:
    print("The max is:", b)
elif c>a and c>b: 
    print("The max is:", c)
#array type 
array = [1,3,5]
max = max(array)
print(max)

#19- Given number is even or odd
#input type 
num = int(input("Enter a number: "))
if num %2 == 0:
    print("This number is even: ", num)
else: 
    print("This number is odd: ",  num)
#number given 
num = 2
if num %2 == 0:
    print("This number is even: ", num)
else: 
    print("This number is odd: ",  num)

