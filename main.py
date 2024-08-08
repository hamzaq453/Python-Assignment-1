# Python Programming Assignment 1

#Question 1
anton_age = 21
beth_age = anton_age + 6
chen_age = beth_age + 20
drew_age = chen_age + anton_age
ethan_age = chen_age


ages = {
    "Anton": anton_age,
    "Beth": beth_age,
    "Chen": chen_age,
    "Drew": drew_age,
    "Ethan": ethan_age
}

for name, age in ages.items():
    print(f"{name} is {age} years old.")

#Question 2

name = "Alice"
age = 30
city = "New York"

sentence = f"{name} is {age} years old and lives in {city}."

print(sentence)

#Question 3

s = "hElLo WoRlD"

capitalized = s.capitalize()

uppercase = s.upper()

lowercase = s.lower()

print(capitalized) 
print(uppercase)   
print(lowercase)   

#Question 4

s = "the quick brown fox jumps over the lazy dog"
index_fox = s.find("fox") if "fox" in s else -1
count_the = s.count("the")

print(f"index of 'fox' is {index_fox}")  
print(f"'the' appears {count_the} times") 

# Question 5
s = "I love programming in Python"
replaced_string = s.replace("Python", "Java")

print(replaced_string) 

# Question 6
s = "apple,banana,cherry,dates"
split_list = s.split(",")
joined_string = " ".join(split_list)

print(split_list) 
print(joined_string)  

# Question 7

s = "   Python is fun!   "
stripped = s.strip()
left_justified = stripped.ljust(20, '*')
right_justified = stripped.rjust(20, '*')

print(stripped)  
print(left_justified) 
print(right_justified)  

# Question 8

num = 45
binary_representation = bin(num)

print(f"Binary representation : {binary_representation}")  # Expected Output: Binary representation : 0b101101

# Question 9
base = 3
exponent = 4
power_result = base ** exponent

print(f"Power result: {power_result}")  # Expected Output: Power result: 81

# Questio 10

value = 12.34567
rounded_integer = round(value)
rounded_two_decimals = round(value, 2)

print(f"Rounded to nearest integer: {rounded_integer}")  # Expected Output: Rounded to nearest integer: 12
print(f"Rounded to two decimal places: {rounded_two_decimals}")  # Expected Output: Rounded to two decimal places: 12.35


