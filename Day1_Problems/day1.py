# # Python Practice Problems

# ## Variables and Data Types

# 1. **Basic Variable Assignment**
#    - Create three variables: one containing your name, one with your age, and one with whether you're a student (True/False)
#    - Print each variable with a descriptive message

name="Jasjeet"
age=22
is_student=True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Student status: {is_student}")


# 2. **Type Conversion**
#    - Create a variable with a decimal number (e.g., 7.8)
#    - Convert it to an integer and store in a new variable
#    - Convert it to a string and store in another variable
#    - Print all three and their types using type()

number=7.8
second_number=int(number)
string_var=str(second_number)
 
print(number,type(number)) 
print(second_number,type(second_number)) 
print(string_var,type(string_var)) 



# 3. **String Operations**
#    - Create a variable containing a sentence with at least 5 words
#    - Find and print its length
#    - Convert it to uppercase
#    - Replace one word with another

sentence= "Hi my name is jasjeet"
print(len(sentence))
print(f" uppercase",{sentence.upper()})
print(f"replace the word (jasjeet), {sentence.replace('jasjeet','palvi')}")


# ## Conditional Statements

# 1. **Age Classifier**
#    - Write a program that:
#    - Takes an age as input
#    - Prints "Child" if age < 13
#    - Prints "Teenager" if age is between 13 and 19
#    - Prints "Adult" if age is 20 or more

age=int(input("give an age  : "))
if age<13:
    print("child")
elif 13<=age<=19:
    print("teenager")   
elif age>=20:
    print("adult")




# 2. **Grade Calculator**
#    - Create a program that:
#    - Takes a numerical score (0-100)
#    - Prints "A" for 90-100
#    - Prints "B" for 80-89
#    - Prints "C" for 70-79
#    - Prints "D" for 60-69
#    - Prints "F" for below 60
#    - Add input validation to check if the score is valid

def calculate_score(score):
    if not isinstance(score,(int,float)) or score<0 or score>100:
        return "invalid score"
    
    elif score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    elif score<60:
        return "F"

print(calculate_score(91))
print(calculate_score(85))
print(calculate_score(76))
print(calculate_score(65))
print(calculate_score(60))
print(calculate_score(55))




# 3. **Number Properties**
#    - Write a program that takes a number and checks if it's:
#    - Positive, negative, or zero
#    - Even or odd
#    - A multiple of 5
#    - Print all these properties

def check_number(number):
    # check positive/negative/zero
    if number>0:
        status= "Positive"
    elif number<0:
        status= "Negative"
    else:
        status= "Zero"

    # check odd even
    parity="even" if number % 2==0 else "odd"

    # check multiple of 5
    multiple="is" if number % 5==0 else "is not"

    return f"Number {number} is {status}, {parity}, and {multiple} a multiple of 5"

print(check_number(15))
print(check_number(-4))




# ## Loops

# 1. **Number Pattern**
#    - Print this pattern using loops:
#    ```
#    1
#    1 2
#    1 2 3
#    1 2 3 4
#    1 2 3 4 5
#    ```

def pattern():
    for i in range(1,6):
        for j in range(1,i+1):
            print(j,end="")
        print()
pattern()    




# 2. **Sum Calculator**
#    - Write a program that:
#    - Keeps asking for numbers until the user enters 0
#    - Prints the sum of all numbers entered
#    - Also prints how many numbers were entered

def calculate_sum():
    numbers=[]
    while True:
        num=float(input("Enter a number (0 to stop) :"))
        if num==0:
            break
        numbers.append(num)
    print( f"sum of numbers {sum(numbers)}, and count of the numbers is {len(numbers)}")

calculate_sum()

# 3. **Multiplication Table**
#    - Create a program that:
#    - Takes a number as input
#    - Prints its multiplication table up to 10
#    - Format it neatly with proper spacing

number=int(input("enter a number for table : "))
for i in range(0,11):
    result=i*number
    print(f"The multipication table of {number} is {number} * {i} = {result}")


# 4. **Factor Finder**
#    - Write a program that:
#    - Takes a number as input
#    - Prints all its factors
#    - Also prints whether it's a prime number

# ## Functions

# 1. **Temperature Converter**
#    - Create two functions:
#    - celsius_to_fahrenheit(celsius)
#    - fahrenheit_to_celsius(fahrenheit)
#    - Each should return the converted temperature
#    - Add input validation

def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        return "Invalid input"
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        return "Invalid input"
    return (fahrenheit - 32) * 5/9


print(celsius_to_fahrenheit(25))  
print(fahrenheit_to_celsius(77))


# 2. **Password Validator**
#    - Write a function that checks if a password is valid
#    - Requirements:
#      - At least 8 characters long
#      - Contains at least one uppercase letter
#      - Contains at least one number
#      - Contains at least one special character
#    - Return True if valid, False if not

def pass_valid(password):
    if len(password)<8:
        return False 
    
    has_upper = False
    has_number = False
    has_special = False
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.isdigit():
            has_number = True
        elif char in special_chars:
            has_special = True
            
    return has_upper and has_number and has_special


print(pass_valid("Pass123!"))  
print(pass_valid("password"))  


# 3. **List Operations**
#    - Create functions for:
#      - Finding the average of a list of numbers
#      - Finding the largest and smallest numbers
#      - Removing duplicates from a list
#      - Reversing a list without using reverse()
def list_operations(numbers):
    # Average
    average = sum(numbers) / len(numbers) if numbers else 0
    
    # Min and Max without built-in functions
    min_num = max_num = numbers[0] if numbers else None
    for num in numbers[1:]:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
            
    # Remove duplicates
    unique = list(dict.fromkeys(numbers))
    
    # Reverse without reverse()
    reversed_list = numbers[::-1]
    
    return {
        "average": average,
        "min": min_num,
        "max": max_num,
        "unique": unique,
        "reversed": reversed_list
    }


numbers = [1, 2, 2, 3, 4, 4, 5]
print(list_operations(numbers)) 


# ## Challenge Problems

# 1. **Calculator Function**
#    - Create a function that:
#    - Takes two numbers and an operator (+, -, *, /, %) as input
#    - Performs the calculation
#    - Handles division by zero
#    - Returns the result and any error messages
#    - Add support for exponents and square roots

def calculator(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        elif operator == '%':
            return num1 % num2
        elif operator == '^':
            return num1 ** num2
        elif operator == 'sqrt':
            if num1 < 0:
                return "Error: Cannot calculate square root of negative number"
            return num1 ** 0.5
        else:
            return "Error: Invalid operator"
    except Exception as e:
        return f"Error: {str(e)}"


print(calculator(10, 5, '+'))  
print(calculator(10, 5, '-')) 
print(calculator(10, 5, '*'))  
print(calculator(10, 5, '/'))  
print(calculator(10, 0, '/'))  
print(calculator(10, 2, '^'))  
print(calculator(16, 0, 'sqrt'))  
