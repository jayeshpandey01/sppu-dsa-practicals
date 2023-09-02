# Write a Python program to compute following operations on String:
# a) To display word with the longest length
# b) To determines the frequency of occurrence of particular character in the string
# c) To check whether given string is palindrome or not 
# d) To display index of first appearance of the substring
# e) To count the occurrences of each word in a given string

def main():
    string = input('Enter string : ')
    stringfreq = dict()

    for i in string:
        stringfreq[i] = stringfreq.get(i, 0) + 1
    stringfreqword = dict()

    for i in string.split():
        stringfreqword[i] = stringfreqword.get(i, 0) + 1

    print(f'\nWord with maximum length : {max(string.split(), key=len)}')
    print(f'\nFrequency of each character :')
    print(stringfreq)

    pali = input('\nEnter a string to check Palindrome: ')
    print(f"Given string is {'not ' if pali != pali[::-1] else ''}a palindrome.\n")

    print(f"First occurrence of given substring is at index : {string.index(input('Enter substring to be searched : '))}")

    print(f'\nFrequency of each word :')
    print(stringfreqword)


if __name__ == "__main__":
    main()
