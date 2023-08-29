'''
Write python program to store 10th class percentage of students in array. Write function 
for sorting array of floating point numbers in ascending order using radix sort and display 
top five scores
'''

def countingSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = int(arr[i] / exp)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = int(arr[i] / exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radixSort(arr):
    max_value = max(arr)
    exp = 1

    while max_value // exp > 0:
        countingSort(arr, exp)
        exp *= 10


def topFiveScores(arr):
    sorted_arr = sorted(arr, reverse=True)
    top_five = sorted_arr[:5]
    print("Top five scores:")
    for score in top_five:
        print(score)


# Main program
students_percentage = []
n = 10

# Taking input
for i in range(n):
    percentage = float(input("Enter percentage of student {}: ".format(i+1)))
    students_percentage.append(percentage)

# Sorting the array using radix sort
radixSort(students_percentage)

# Displaying top five scores
topFiveScores(students_percentage)
