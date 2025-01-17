# Lists

# List Basics

# Create a list of 5 favorite foods
# Add a new food to the end
# Insert a food at position 2
# Remove the last food
# Print the list before and after each operation

food=['Rice','tortila','dosa','noodles','salad']
food.append('sushi')
print(food)
food.insert(1,'tacos')
food.pop()
print(food)

# List Operations

# Create a list of numbers 1-10
# Create a new list with only even numbers
# Create another list with only numbers greater than 5
# Find the sum and average of the original list

def list_oper():
    orginal=list(range(1,11))
    even_num=[n for n in orginal if n%2==0]
    great_5= [n for n in orginal if n>5 ]

    print(f"original: {orginal}, even: {even_num}, greater_than_five: {great_5}, sum: {sum(orginal)}, average: {sum(orginal)/len(orginal)}")

list_oper()

# List Manipulation

# Given: numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
# Remove all duplicates while maintaining order
# Count how many times each number appears
# Find the second largest number
numbers=[1,2,2,3,3,3,4,4,5]

# Remove duplicates while maintaining order
unique_numbers = list(dict.fromkeys(numbers))

# Count occurrences of each number
count_dict = {}
for num in numbers:
    count_dict[num] = numbers.count(num)

# Find second largest number
second_largest = sorted(set(numbers))[-2]

print("Original list:", numbers)
print("Remove duplicates:", unique_numbers)
print("Count of each number:", count_dict)
print("Second largest number:", second_largest)




# Tuples

# Tuple Basics

# Create a tuple with your name, age, and city
# Try to modify an element (notice it's not possible)
# Create a new tuple with updated age
# Concatenate both tuples

def tuple_basics():
    person = ("John", 25, "New York")
    # This will raise an error: person[1] = 26
    updated_person = person[:1] + (26,) + person[2:]
    combined = person + updated_person
    print( combined)
tuple_basics()
# Tuple Operations

# Create a tuple of numbers
# Count how many times a specific number appears
# Convert tuple to list, modify it, convert back to tuple
# Find the index of a specific element


# Tuple Packing/Unpacking

# Create a tuple with 5 student names and their scores
# Unpack the tuple into variables
# Create a function that returns multiple values and unpack them


# Sets

# Set Basics

# Create two sets of numbers
# Find their union, intersection, and difference
# Add elements to both sets
# Remove elements from both sets


# Set Operations

# Create three sets with some common elements
# Find elements that are in all three sets
# Find elements that are in at least two sets
# Find elements that are unique to each set


# Set Manipulation

# Given two strings, find:

# All unique characters in both strings
# Common characters between them
# Characters in first string but not in second




# Set Applications

# Create a program to store and check unique visitor IDs
# Add new visitors
# Check if a visitor is new or returning
# Remove inactive visitors



# Dictionaries

# Dictionary Basics

# Create a dictionary of student names and their scores
# Add new students
# Update existing scores
# Remove students
# Print all names and scores


# Dictionary Operations

# Create a dictionary of items and their prices
# Apply a 10% discount to all items
# Find the most expensive and least expensive items
# Calculate the total cost of all items


# Nested Dictionaries

# Create a nested dictionary of:
# pythonCopy{
#     'class_a': {'student1': {'math': 90, 'english': 85},
#                'student2': {'math': 95, 'english': 90}},
#     'class_b': {...}
# }

# Calculate average score per subject per class
# Find the top student in each class
# Find the overall top student


# Dictionary Applications

# Create a word frequency counter that:

# Takes a string of text
# Counts how many times each word appears
# Ignores case and punctuation
# Returns the top 3 most common words