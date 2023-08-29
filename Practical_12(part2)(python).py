'''
Write a python program to store names and mobile numbers of your friends in sorted 
order on names. Search your friend from list using Fibonacci search. Insert friend if not 
present in phonebook.

'''

def fibonacci_search(arr, x):
    fib2, fib1 = 0, 1

    while fib1 < len(arr):
        fib2, fib1 = fib1, fib2 + fib1

    offset = -1

    while fib1 > 1:
        i = min(offset + fib2, len(arr) - 1)

        if arr[i] < x:
            fib1, fib2 = fib2, fib1 - fib2
            offset = i
        elif arr[i] > x:
            fib1, fib2 = fib2 - fib1, fib1 - fib2
        else:
            return i

    if fib2 and offset < len(arr) - 1 and arr[offset + 1] == x:
        return offset + 1

    return -1

def insert_friend(phonebook, name, number):
    i = 0
    while i < len(phonebook) and phonebook[i][0] < name:
        i += 1

    if i < len(phonebook) and phonebook[i][0] == name:
        print("Friend already exists in phonebook.")
    else:
        phonebook.insert(i, (name, number))
        print("Friend successfully added to phonebook.")

def display_phonebook(phonebook):
    print("Phonebook:")
    for friend in phonebook:
        print(friend[0], "-", friend[1])

# Initialize phonebook
phonebook = [("Alice", "123456789"), ("Bob", "987654321"), ("Charlie", "567891234")]

# Sort the phonebook based on names
phonebook.sort(key=lambda x: x[0])

# Display initial phonebook
display_phonebook(phonebook)

# Search for a friend
friend_name = input("Enter the name of the friend you want to search: ")
index = fibonacci_search([friend[0] for friend in phonebook], friend_name)

if index != -1:
    print("Friend found in phonebook!")
    print(phonebook[index][0], "-", phonebook[index][1])
else:
    print("Friend not found in phonebook.")

# Insert a friend
friend_name = input("Enter the name of the friend you want to insert: ")
friend_number = input("Enter the mobile number of the friend you want to insert: ")
insert_friend(phonebook, friend_name, friend_number)

# Display updated phonebook
display_phonebook(phonebook)
