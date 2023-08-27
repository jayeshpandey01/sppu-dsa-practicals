'''

Experiment Number 2 : Write a python program to store marks stored in subject "Fundamentals of Data Structure" by
                         N students in the class. Write functions to compute following:
                         1. The average score of the class.
                         2. Highest score and lowest score of the class.
                         3. Count of students who were absent for the test.
                         4. Display mark with highest frequency.
'''


def calculate_average(marks_list):
    total_marks = 0
    count = 0
    for marks in marks_list:
        if marks != -999:
            total_marks += marks
            count += 1
    average = total_marks / count
    print("Total Marks: ", total_marks)
    print("Average Marks: {:.2f}".format(average))

def find_highest_score(marks_list):
    max_score = marks_list[0]
    for marks in marks_list:
        if marks != -999 and marks > max_score:
            max_score = marks
    return max_score

def find_lowest_score(marks_list):
    min_score = marks_list[0]
    for marks in marks_list:
        if marks != -999 and marks < min_score:
            min_score = marks
    return min_score

def count_absent_students(marks_list):
    absent_count = 0
    for marks in marks_list:
        if marks == -999:
            absent_count += 1
    return absent_count

def find_max_frequency_mark(marks_list):
    max_frequency = 0
    max_frequency_mark = None
    unique_marks = set(marks_list)
    print("Marks  |  Frequency")
    for mark in unique_marks:
        frequency = marks_list.count(mark)
        print(f"{mark}    |  {frequency}")
        if frequency > max_frequency:
            max_frequency = frequency
            max_frequency_mark = mark
    return max_frequency_mark, max_frequency

def main():
    marks_in_FDS = []
    number_of_students = int(input("Enter total number of students: "))
    for i in range(number_of_students):
        marks = int(input("Enter marks of student " + str(i + 1) + ": "))
        marks_in_FDS.append(marks)

    flag = True
    while flag:
        print("\n--------------------MENU--------------------\n")
        print("1. Total and Average Marks of the Class")
        print("2. Highest and Lowest Marks in the Class")
        print("3. Number of Students absent for the test")
        print("4. Marks with Highest Frequency")
        print("5. Exit\n")
        
        choice = int(input("Enter your Choice (from 1 to 5): "))

        if choice == 1:
            calculate_average(marks_in_FDS)

        elif choice == 2:
            print("Highest Score in Class: ", find_highest_score(marks_in_FDS))
            print("Lowest Score in Class: ", find_lowest_score(marks_in_FDS))

        elif choice == 3:
            print("Number of Students absent in the test: ", count_absent_students(marks_in_FDS))

        elif choice == 4:
            mark, frequency = find_max_frequency_mark(marks_in_FDS)
            print("Highest frequency is of marks {0} that is {1}".format(mark, frequency))

        elif choice == 5:
            flag = False
            print("Thanks for using this program!")

        else:
            print("!!Wrong Choice!!")

if __name__ == "__main__":
    main()
