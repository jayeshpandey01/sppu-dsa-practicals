'''
Write a python program to store second year percentage of students in array. Write 
function for sorting array of floating point numbers in ascending order using 
a) Insertion sort 
b) Shell Sort and display top five scores
'''

  # Function to perform Insertion Sort on the given array.

Parameters:
    arr (list): List of floating point numbers.

Returns:
    list: Sorted list of floating point numbers in ascending order.
'''
n = len(arr)

for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

return arr

 # Function to perform Shell Sort on the given array.

Parameters:
    arr (list): List of floating point numbers.

Returns:
    list: Sorted list of floating point numbers in ascending order.
'''
n = len(arr)
gap = n // 2

while gap > 0:
    for i in range(gap, n):
        temp = arr[i]
        j = i

        while j >= gap and arr[j - gap] > temp:
            arr[j] = arr[j - gap]
            j -= gap

        arr[j] = temp

    gap //= 2

return arr

# if name == "main": # Taking input of number of students n = int(input("Enter the number of students: "))

# Taking input of percentages of students
percentages = []

for i in range(n):
    percentage = float(input(f"Enter percentage of student {i + 1}: "))
    percentages.append(percentage)

# Sorting the array using Insertion Sort
sorted_insertion = insertionSort(percentages)

# Sorting the array using Shell Sort
sorted_shell = shellSort(percentages)

# Displaying top five scores
print("\nTop five scores (sorted using Insertion Sort):")
for i in range(n - 1, n - 6, -1):
    print(sorted_insertion[i])

print("\nTop five scores (sorted using Shell Sort):")
for i in range(n - 1, n - 6, -1):
    print(sorted_shell[i])
