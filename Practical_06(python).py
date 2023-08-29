# It is decided that weekly greetings are to be furnished to wish the students having their 
# birthdays in that week. The consolidated sorted list with desired categorical information 
# is to be provided to the authority. Write a python program to store students PRNs with 
# date and month of birth. Let List_A and List_B be the two list for two SE Computer 
# divisions. Lists are sorted on date and month. Merge these two lists into third list 
# “List_SE_Comp_DOB” resulting in sorted information about Date of Birth of SE Computer 
# students


def merge_and_sort_lists(list_a, list_b):
    merged_list = list_a + list_b
    merged_list.sort(key=lambda x: (x[1], x[2]))  # Sorting by month and date
    return merged_list

def main():
    list_a = []
    list_b = []
    
    num_students_a = int(input("Enter the number of students in List A: "))
    for i in range(num_students_a):
        prn = input(f"Enter PRN for student {i+1}: ")
        date, month = map(int, input(f"Enter birth date and month (DD MM) for student {i+1}: ").split())
        list_a.append((prn, date, month))
    
    num_students_b = int(input("Enter the number of students in List B: "))
    for i in range(num_students_b):
        prn = input(f"Enter PRN for student {i+1}: ")
        date, month = map(int, input(f"Enter birth date and month (DD MM) for student {i+1}: ").split())
        list_b.append((prn, date, month))
    
    list_se_comp_dob = merge_and_sort_lists(list_a, list_b)
    
    print("\nMerged and sorted List_SE_Comp_DOB:")
    for student in list_se_comp_dob:
        prn, date, month = student
        print(f"PRN: {prn}, DOB: {date:02d}-{month:02d}")

if __name__ == "__main__":
    main()
