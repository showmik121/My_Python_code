# List
num = [1, 2, 3, 4, 3]

# Dictionary
person = {'name': 'kala', 'address': 'kaliPUR', 'AGE': 23}

# Print the entire dictionary
print(person)

# Access and print a specific key's value
print(person['address'])

# Delete a key-value pair from the dictionary
del person['address']
print(person)

# Iterate through the dictionary's key-value pairs
for key, value in person.items():
    print(key, value)

# Iterate through the list with index and value using enumerate
for i, n in enumerate(num):
    print(i, n)
