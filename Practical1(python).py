'''


Experiment No. 1 : In a second year computer engineering class, group A students play cricket, group B students play
                   badminton and group C students play football.
                   Write a python program using functions to compute following:
                   a) List of students who play both cricket and badminton.
                   b) List of students who play either cricket or badminton but not both.
                   c) Number of students who play neither cricket nor badminton.
                   d) Number of students who play cricket and football but not badminton.
(NOTE : While realising the group, duplicate entries should be avoided. Do not use SET built-in functions)
'''

# Function for removing duplicate entries from the list
def removeDuplicate(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

# Function for finding intersection between two lists (A & B)
def intersection(lst1, lst2):
    common_elements = []
    for val in lst1:
        if val in lst2:
            common_elements.append(val)
    return common_elements

# Function for finding union of two lists (A | B)
def union(lst1, lst2):
    combined_list = lst1.copy()
    for val in lst2:
        if val not in combined_list:
            combined_list.append(val)
    return combined_list

# Function for finding difference between two lists (A - B)
def difference(lst1, lst2):
    unique_elements = []
    for val in lst1:
        if val not in lst2:
            unique_elements.append(val)
    return unique_elements

# Function for finding symmetric difference of two lists (A ^ B)
def symmetric_diff(lst1, lst2):
    diff1 = difference(lst1, lst2)
    diff2 = difference(lst2, lst1)
    symmetric_result = union(diff1, diff2)
    return symmetric_result

# Main function
def main():
    # Creating lists for SE COMP, Cricket, Football, and Badminton
    SEComp = input("Enter the names of students in SE COMP (comma-separated): ").split(',')
    Cricket = input("Enter the names of students who play cricket (comma-separated): ").split(',')
    Football = input("Enter the names of students who play football (comma-separated): ").split(',')
    Badminton = input("Enter the names of students who play badminton (comma-separated): ").split(',')

    # Removing duplicates from the lists
    SEComp = removeDuplicate(SEComp)
    Cricket = removeDuplicate(Cricket)
    Football = removeDuplicate(Football)
    Badminton = removeDuplicate(Badminton)

    flag = True
    while flag:
        print("\n--------------------MENU--------------------")
        print("1. List of students who play both cricket and badminton")
        print("2. List of students who play either cricket or badminton but not both")
        print("3. List of students who play neither cricket nor badminton")
        print("4. Number of students who play cricket and football but not badminton")
        print("5. Exit")

        choice = int(input("Enter your choice (1 to 5): "))

        if choice == 1:
            common_CB = intersection(Cricket, Badminton)
            print("List of students who play both cricket and badminton:", common_CB)

        elif choice == 2:
            either_C_or_B = symmetric_diff(Cricket, Badminton)
            print("List of students who play either cricket or badminton but not both:", either_C_or_B)

        elif choice == 3:
            neither_C_nor_B = difference(SEComp, union(Cricket, Badminton))
            print("List of students who play neither cricket nor badminton:", neither_C_nor_B)

        elif choice == 4:
            cricket_and_football = intersection(Cricket, Football)
            not_badminton = difference(cricket_and_football, Badminton)
            print("List of students who play cricket and football but not badminton:", not_badminton)

        elif choice == 5:
            flag = False
            print("Thanks for using this program!")

        else:
            print("Invalid choice!")

# Run the main function
if __name__ == "__main__":
    main()
