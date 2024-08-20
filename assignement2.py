array = [10, 5, 8, 20, 3, 9, 6, 32, 26]
maxelement = max(array)
square = maxelement ** 2
print(square)


list1 = [8, 45, 25, 6, 11, 29, 42, 25, 14, 42, 25]
counts = {}
for num in list1:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

for num, count in sorted_counts:
    print( num,count)
def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))



# Define the input array
array = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
uniquearray = []
for item in array:
    if item not in uniquearray:
        uniquearray.append(item)
print(uniquearray)

numbers = [21, 45, -21, -45, 600, 100, 50, 70]
print(numbers.sort())
print(numbers[-2])

numbers1 = [21, 45, -21, -45, 600, 100, 50, 70]
numbers1.sort()
print(numbers1[-3])

# Define the list of numbers
numbers = [3, -5, -28, 7, -81, 4, -16]

negative_numbers = []
for num in numbers:

    if num < 0:
        negative_numbers.append(num)

print(negative_numbers)
negative_numbers.sort(reverse=True)
print(negative_numbers)
print(negative_numbers[1])
input_sentence = "Hi welcome to the world of python programming"
words = input_sentence.split()
print(words)
reversed_words = words[::-1]
print(reversed_words)
print(' '.join(reversed_words))

# Define the input text
input_txt = "Hi Welcome to the Wrold of Python programming"

# Initialize counters for lowercase and uppercase characters
lowercase_count = 0
uppercase_count = 0

# Iterate through each character in the text
for char in input_txt:
    # Check if the character is a lowercase letter
    if char.islower():
        lowercase_count += 1
    # Check if the character is an uppercase letter
    elif char.isupper():
        uppercase_count += 1

# Print the counts of lowercase and uppercase characters
print(f"Number of lowercase characters: {lowercase_count}")
print(f"Number of uppercase characters: {uppercase_count}")

# Define the input string
# Define the list with various types of elements
elements = ['gfg', 1, True, 'is', 2, 'best']

# Initialize a counter for the number of strings
string_count = 0

# Iterate through each element in the list
for element in elements:
    # Check if the type of the element is 'str'
    if type(element) == str:
        # Increment the counter
        string_count += 1

# Print the count of string elements
print(f"Number of string elements in the list: {string_count}")

