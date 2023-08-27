# Write a Python program to compute following operations on String:
# a) To display word with the longest length
# b) To determines the frequency of occurrence of particular character in the string
# c) To check whether given string is palindrome or not 
# d) To display index of first appearance of the substring
# e) To count the occurrences of each word in a given string

def longest_word(s):
    words = s.split()
    longest = max(words, key=len)
    return longest

def char_frequency(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def first_appearance(s, sub):
    index = s.find(sub)
    return index

def word_occurrences(s):
    words = s.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def main():
    string = input("Enter a string: ")

    longest = longest_word(string)
    print(f"Longest word: {longest}")

    char = input("Enter a character to count its frequency: ")
    frequency = char_frequency(string, char)
    print(f"Frequency of '{char}': {frequency}")

    palindrome_result = is_palindrome(string)
    if palindrome_result:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

    sub = input("Enter a substring to find its first appearance index: ")
    index = first_appearance(string, sub)
    if index != -1:
        print(f"First appearance of '{sub}': {index}")
    else:
        print(f"'{sub}' not found in the string.")

    word_count = word_occurrences(string)
    print("Word occurrences:")
    for word, count in word_count.items():
        print(f"'{word}': {count}")

if __name__ == "__main__":
    main()
