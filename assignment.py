x=10;
print(x)

for x1 in range(1 , 11):
    print(x1)

x2=[ 8,45,25,6, 11, 29, 42, 25, 14,42,25]
for list1 in x2:
    print(list1)

arr = {2, 5, 1, 3, 0};
print(max(arr))

# Define the two strings
string1 = "aman"
string2 = "abhi"

# Convert the strings to sets to get unique characters
set1 = set(string1)
set2 = set(string2)

# Find the intersection of the two sets to get common letters
common_letters = set1.intersection(set2)

# Print the output
print(common_letters)
# Define the list
question = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]

# Create an empty dictionary to store the counts
occurrences = {}

# Iterate through the list and count occurrences
for element in question:
    if element in occurrences:
        occurrences[element] += 1
    else:
        occurrences[element] = 1

# Print the occurrences
print(occurrences)
arr= {0, -1, 2, -3, 1}
x=-2
if x in arr:
    print("yes")
else:
    print("no")






