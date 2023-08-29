'''
 Write a python program to store roll numbers of student array who attended training 
program in sorted order. Write function for searching whether particular student 
attended training program or not, using Binary search and Fibonacci search
'''

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return False


def fibonacci_search(arr, x):
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2

    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
        i = min(offset + fib2, len(arr) - 1)

        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return True

    if fib1 and arr[offset + 1] == x:
        return True

    return False


def main():
    roll_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    roll_numbers.sort()

    search_num = 50

    if binary_search(roll_numbers, search_num):
        print(f"{search_num} attended the training program (Binary Search)")
    else:
        print(f"{search_num} did not attend the training program (Binary Search)")

    if fibonacci_search(roll_numbers, search_num):
        print(f"{search_num} attended the training program (Fibonacci Search)")
    else:
        print(f"{search_num} did not attend the training program (Fibonacci Search)")


if __name__ == '__main__':
    main()
