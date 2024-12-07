###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140
car_speed = int( input('Enter car speed (km/h): ') )

if car_speed > 140:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')

###
# Credit card payment 
#
account_balance = float(500)
total_payment = float(input('Enter the total value of purchases: '))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')

###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = int(input('Enter the number of properly performed tasks: '))
test_passed = False

if tasks_ok >= total_tasks / 2:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')

###
# Checking whether the number
# entered from the keyboard is even or odd 
#
number = int(input('Enter number: '))

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')


###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.15 # 15%
is_bonus = input('Does the employee receive a bonus? (Y/N):').upper() == 'Y'

if is_bonus:
    total_salary = basic_salary + (basic_salary * bonus)
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {"Yes" if is_bonus else "No"}')
print(f'Total salary: {total_salary}')

###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
size = input('Enter size symbol: ').upper()

if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('M: Medium size')
elif size == 'L':
    print('L: Large size')
elif size == 'XL':
    print('XL: Extra large size')
else:
    print('Incorrect symbol')


###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#
driving_mode = input('Enter driving mode (A/M/E): ').upper()
distance = int(input('Enter distance in km: '))

if driving_mode == 'A':
    fuel_consumption = 7 # liters per 100km
elif driving_mode == 'M':
    fuel_consumption = 9
elif driving_mode == 'E':
    fuel_consumption = 6


total_consumption = (fuel_consumption / 100) * distance
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption:.2f} liters')

###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input('Enter number 1: '))
number2 = int(input('Enter number 2: '))
operator = input('Enter an operator: ')

if operator == "+":
    result = number1 + number2
elif operator == "-":
   result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2

# print result
print(f'{number1} {operator} {number2} = {result}')

#### a program that calculates and prints the quarter of the year for a given month number
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month >= 7:
    quarter = 3
elif month >= 4:
    quarter = 2
else:
    quarter = 1

print(f'Month {month} is in quarter {quarter}')


#### a program that checks what number was entered from the keyboard
###  and prints the appropriate message

number = float(input('Enter your number: '))

if number > 0:
    print(f'Number {number} is positive')
elif number < 0:
    print(f'Number {number} is negative')
else:
    print(f'Number is 0')


###
# Checking login and password
#
login = 'joe'
password = 'abcd'
entered_login = input('Login: ')
entered_password = input('Password: ')
if login == entered_login and password == entered_password:
    print('You are logged in')
else:
    print('Incorrect login or password!!')


###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#
age = int(input('Enter your age: '))

if age < 18 or age >= 65 :
    print("You're eligible for a discount")
else:
    print("You're not eligible for a discount")


###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if not x < 0 or not y < 0 :
    print(f'At least one of the numbers {x} and {y} is not negative')


month = int(input('Enter month number (1..12): '))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31  
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30  
else:  
    days = 28

print(f'Month {month} has {days} days')

###
# Checks if the given day number of the month is correct
#
month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
day_ok = False

if month ==1 or month==3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day >=1 and day <= 31:
        day_ok = True
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day >=1 and day <= 30:
        day_ok = True
elif month == 2:
    if day >=1 and day <= 28:
        day_ok = True

message = f'Day {day} for the month {month}'
if day_ok:
    print(f'{message} is correct')
else:
    print(f'{message} is incorrect')


###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#
university = 'Krakow University of Economics'
university_expanded = ""

for char in university:
    university_expanded = university_expanded + char + ' '

print(university) 
print(university_expanded) 


###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    char_code = ord(char)
    char_code += 1
    encrypted_char = chr(char_code)
    encrypted_text += encrypted_char


print(plain_text)
print(encrypted_text)

###
# Calculates the sum of integer numbers in the range <5,5>
#
sum = 0

for i in range(5,11):
    sum += i

print(f'Sum is {sum}')


###
# Calculates the sum of even numbers in the range <1,10>
#
sum = 0

for i in range(1, 11):
    if not i % 2 == 0:
        continue
    sum += i

print(f'Sum of even numbers in the range <1,10> is {sum}')


###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#
for i in range(2,11):
    print(f'1/{i} = {1/i}')


###
# A simple number guessing game
#
import random

# Randomly chosen number to be guessed from 1 to 100
number_to_guess = random.randint(1, 100)
user_guess = 0

print("Guess the number between 1 and 100!")

while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")


###
# Sums numbers entered by user
#
total_sum = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count += 1  # Increment the counter for each entered number

if count > 0:
    mean = total_sum / count  # Calculate the arithmetic mean
    print(f"The total sum of the numbers is: {total_sum}")
    print(f"The arithmetic mean of the numbers is: {mean}")
else:
    print("No numbers were entered.")


# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0
i = 1 


while i <= N:
    if i % 2 == 0:
        sum_even += i
    i += 1 

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")


import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    if countdown >= 1 and countdown <= 5:
        if countdown == 5:
            print("five")
        elif countdown == 4:
            print("four")
        elif countdown == 3:
            print("three")
        elif countdown == 2:
            print("two")
        elif countdown == 1:
            print("one")
    else:
        print(countdown)

    countdown -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")


###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-4): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        entered_pin = input("Enter your PIN to check: ")
        if entered_pin == pin:
            print("PIN is correct.")
        else:
            print("Incorrect PIN.")
    elif choice == '5':
        entered_pin = input("Enter your current PIN to change it: ")
        if entered_pin == pin:
            new_pin = input("Enter your new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print("Your PIN has been successfully changed.")
            else:
                print("Invalid PIN. The PIN must consist of exactly 4 digits.")
        else:
            print("Incorrect PIN. Unable to change.")
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")


# Counts vowels in the text using a while loop
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
index = 0  # Initialize the index for the while loop

# Count vowels in the text
while index < len(text):
    if text[index] in vowels:
        vowel_count += 1
    index += 1  # Move to the next character

print(f"The number of vowels in the text is: {vowel_count}")


###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2

print(f'{bulbs_on} are lit')


###
# Password validator
# New password is at least 12 characters long
#
new_password = input('Enter new password: ')
if len(new_password) < 12:
   print('Password too short (min. 12 chars)') 
else:
   print('Password is strong.')


###
# Program that simulates the operation of an electronic thermometer.
#
temperature = -2
if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print("It is hot")
elif temperature >= 15:
    print("It is warm")
elif temperature >= 0:
    print("It is cold")
elif temperature < 0:
    print("Warning, frost")

### Parking meter
hours = input('Enter the number of hours: ')

if hours <= 2:
    fee = 5
elif hours <= 6:
    fee = 15
else:
    fee = 20

print(f"The parking fee for {hours} hours is {fee} PLN.")

###
# Age group checker
# Categorizes age into Child, Teen, Adult, or Senior
#

age = int(input("Enter your age: "))

if age < 13:
    print("You are a Child.")
elif 13 <= age <= 19:
    print("You are a Teen.")
elif 20 <= age <= 64:
    print("You are an Adult.")
else:
    print("You are a Senior.")


###
# Checking if both people are adults
#
person1_name = input('Enter first person name: ')
person1_age = int(input('Enter first person age: '))
person2_name = input('Enter second person name: ')
person2_age = int(input('Enter second person age: '))
if person1_age >= 18 and person2_age >= 18:
    print(f'Both {person1_name} and {person2_name} are adults')
else:
    print(f'Either {person1_name} or {person2_name} is not an adult')


###
# Checking if both people are adults
#
name = input('Enter first person name: ')

if name[-1].lower() == 'a':
    print(f'{name} - Polish female name')
else:
    print('Not a female name')


###
# Dog's age calculator
# 

dog_age_human_years = float(input("Enter the dog's age in human years: "))

if dog_age_human_years <= 2:
    dog_age_dog_years = dog_age_human_years * 10.5
else:
    dog_age_dog_years = (2 * 10.5) + (dog_age_human_years - 2) * 4


print(f"The dog's age in dog's years is {dog_age_dog_years:.0f} years.")


### Price drop program
current_price = float(input("Enter the current product price: "))
previous_price = float(input("Enter the previous product price: "))


price_decrease = ((previous_price - current_price) / previous_price) * 100


if price_decrease >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_decrease:.0f}%")
else:
    print("No significant price drop. Wait for a better deal.")


### Discount based on amount of products purchased
num_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))


if num_products <= 2:
    total_cost = num_products * product_price
else:
    full_price_cost = 2 * product_price
    discounted_cost = (num_products - 2) * product_price * 0.75
    total_cost = full_price_cost + discounted_cost


print(f"Amount to pay: {total_cost:.2f}")


### Speed limits on highways in Poland
speed_limit_min = 40
speed_limit_max = 140

car_speed = int(input("Enter car speed: "))

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")
else:
    print("Car speed is within the valid range.")


### Good or bad influencer
facebook = True
twitter = False
instagram = True


active_accounts = sum([facebook, twitter, instagram])

if active_accounts >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")


### EAN-13 number
ean_number = input("Enter EAN-13 article number: ")

if len(ean_number) == 13 and ean_number.isdigit():
    print("Article number is correct")
    
    if ean_number[0:3] == "590":
        print("Article manufactured in Poland")
else:
    print("Invalid EAN-13 number")


# Calculates and prints the total washing time.

# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).


washing_times = {
    'jacket': 40,
    'underwear': 70,
    'shoes': 20
}


program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')

if program == 'j':
    washing_product = 'jacket'
elif program == 'u':
    washing_product = 'underwear'
elif program == 's':
    washing_product = 'shoes'
else:
    print("Invalid option. Exiting program.")
    exit()

extra_rinse = input('Extra rinse? (y/n): ').lower() == 'y'
extra_spin = input('Extra spin? (y/n): ').lower() == 'y'

total_washing_time = washing_times[washing_product]

if extra_rinse:
    total_washing_time += 15
if extra_spin:
    total_washing_time += 9

print(f"Total washing time: {total_washing_time} minutes")


# Convert time from 24-hour format to 12-hour format

time_24hr = input("Enter time (24-hour format): ")

hours, minutes = time_24hr.split(':')

hours = int(hours)
minutes = int(minutes)

if hours >= 12:
    period = "pm"
    if hours > 12:
        hours -= 12  
else:
    period = "am"
    if hours == 0:
        hours = 12  

print(f"Time in 12-hour format: {hours}:{minutes:02d}{period}")


# Read the coordinates of the point
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

# Determine the location of the point
if x == 0 and y == 0:
    print("Point P(0,0) is at the origin.")
elif x == 0:
    print(f"Point P({x},{y}) is on the y-axis.")
elif y == 0:
    print(f"Point P({x},{y}) is on the x-axis.")
elif x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system.")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system.")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system.")
else:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system.")


### Survey
computer_science = input("Are you interested in computer science? (y/n): ").lower() == 'y'
computer_games = input("Do you like playing computer games? (y/n): ").lower() == 'y'
instagram_account = input("Do you have an Instagram account? (y/n): ").lower() == 'y'

print("\nSURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if computer_science else 'No'}")
print(f"Playing computer games: {'Yes' if computer_games else 'No'}")
print(f"Has an Instagram account: {'Yes' if instagram_account else 'No'}")


# Read the decimal number from the user
decimal_number = int(input("Enter decimal number: "))

remainders = []

while decimal_number > 0:
    remainder = decimal_number % 2  
    remainders.append(str(remainder))  
    decimal_number = decimal_number // 2 

binary_number = ''.join(remainders[::-1])

print(f"Binary number: {binary_number}")


# Read the amount from the user
amount = int(input("Enter the amount in PLN: "))

five_pln_coins = amount // 5  
remaining_amount = amount % 5  

two_pln_coins = remaining_amount // 2  
remaining_amount = remaining_amount % 2  

one_pln_coins = remaining_amount  

# Display the result
print(f"The amount of PLN {amount} in coins:")
print(f"5 PLN coins: {five_pln_coins}")
print(f"2 PLN coins: {two_pln_coins}")
print(f"1 PLN coins: {one_pln_coins}")



# Loop through numbers from 1 to 30
for num in range(1, 31):

    if num % 3 == 0 and num % 5 == 0:
        print("BINGO", end=" ")

    elif num % 3 == 0:
        print("THREE", end=" ")

    elif num % 5 == 0:
        print("FIVE", end=" ")

    else:
        print(num, end=" ")


### Number multiplication
number = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


### Star pattern
for i in range(1, 6):  
    print("* " * i)


for i in range(4, 0, -1):  
    print("* " * i)


### Numbers pattern
for i in range(1, 10):  
    print(f"{i}" * i)


### PIN code 3 attempts
correct_pin = "0805"
attempts = 3

for i in range(attempts):
    entered_pin = input("Enter the PIN code: ")

    if entered_pin == correct_pin:
        print("Access granted!")
        break  
    else:
        print("Incorrect...")

else:
    print("Sorry, your payment card has been blocked.")

### 7 8 9 4 5 6 1 2 3 pattern
i = 6
while i >= 0:
    j = 1
    while j <= 3:
        print(f'{i + j}', end=' ')
        j += 1
    print()
    i -= 3


#### Fibonacci sequence
a, b = 0, 1

for _ in range(20):
    print(a, end=' ')  
    a, b = b, a + b   

####Find N leading prime numbers
def is_prime(num):
    if num <= 1:
        return False  
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            return False  
    return True

N = int(input("Enter the number of leading prime numbers to find: "))

count = 0  
current = 2 

# Loop to find N primes
while count < N:
    if is_prime(current):
        print(current, end=" ")  
        count += 1  
    current += 1  

### Coupon loop
for i in range(7):
    for j in range(i + 1, 50, 7):
        print(j, end=" ")
    print()  