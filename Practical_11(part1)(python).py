'''
Write a python program to store roll numbers of student in array who attended
training program in random order. Write function for searching whether particular
student attended training program or not, using Linear search and Sentinel search.
'''

def linear_search(roll_numbers, target):
    for roll_number in roll_numbers:
        if roll_number == target:
            return True
    return False

def sentinel_search(roll_numbers, target):
    n = len(roll_numbers)
    roll_numbers.append(target)  # Add target as a sentinel at the end
    i = 0
    while roll_numbers[i] != target:
        i += 1
    roll_numbers.pop()  # Remove the sentinel
    return i != n

# Example usage
roll_numbers = [10, 20, 30, 40, 50]
student_roll_number = 30

if linear_search(roll_numbers, student_roll_number):
    print("Linear search: Student attended the training program")
else:
    print("Linear search: Student did not attend the training program")

if sentinel_search(roll_numbers, student_roll_number):
    print("Sentinel search: Student attended the training program")
else:
    print("Sentinel search: Student did not attend the training program")
