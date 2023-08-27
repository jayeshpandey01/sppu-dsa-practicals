'''
Experiment Number 14: Write a python program to store first year percentage of students in an array.
                      Write function for sorting array of floating point numbers in ascending order using:
                      a) Selection Sort
                      b) Bubble Sort and display top five scores
'''
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    num_students = int(input("Enter the number of students: "))
    percentages = []

    for i in range(num_students):
        percentage = float(input(f"Enter the percentage for student {i + 1}: "))
        percentages.append(percentage)

    sorted_percentages_selection = percentages.copy()
    selection_sort(sorted_percentages_selection)

    sorted_percentages_bubble = percentages.copy()
    bubble_sort(sorted_percentages_bubble)

    print("\nTop Five Scores (Selection Sort):")
    for i in range(1, 6):
        print(f"{i}. {sorted_percentages_selection[-i]:.2f}%")

    print("\nTop Five Scores (Bubble Sort):")
    for i in range(1, 6):
        print(f"{i}. {sorted_percentages_bubble[-i]:.2f}%")

if __name__ == "__main__":
    main()
