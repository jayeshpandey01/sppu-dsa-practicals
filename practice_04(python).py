# Write a Python program for department library which has N books, write functions for 
# following:
# a) Delete the duplicate entries
# b) Display books in ascending order based on cost of books
# c) Count number of books with cost more than 500. 
# d) Copy books in a new list which has cost less than 500.

class Book:
    def __init__(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

def delete_duplicates(books):
    unique_books = []
    for book in books:
        if book not in unique_books:
            unique_books.append(book)
    return unique_books

def display_books_sorted_by_cost(books):
    sorted_books = sorted(books, key=lambda book: book.cost)
    print("Books in ascending order of cost:")
    for book in sorted_books:
        print(f"{book.title} by {book.author} - Cost: {book.cost}")

def count_expensive_books(books):
    expensive_count = sum(1 for book in books if book.cost > 500)
    return expensive_count

def copy_cheap_books(books):
    cheap_books = [book for book in books if book.cost < 500]
    return cheap_books

def main():
    n = int(input("Enter the number of books: "))
    books = []
    
    for i in range(n):
        title = input(f"Enter title of book {i+1}: ")
        author = input(f"Enter author of book {i+1}: ")
        cost = float(input(f"Enter cost of book {i+1}: "))
        books.append(Book(title, author, cost))
    
    unique_books = delete_duplicates(books)
    print("Books after removing duplicates:")
    for book in unique_books:
        print(f"{book.title} by {book.author} - Cost: {book.cost}")
    
    display_books_sorted_by_cost(unique_books)
    
    expensive_count = count_expensive_books(unique_books)
    print(f"Number of books with cost more than 500: {expensive_count}")
    
    cheap_books = copy_cheap_books(unique_books)
    print("Books with cost less than 500:")
    for book in cheap_books:
        print(f"{book.title} by {book.author} - Cost: {book.cost}")

if __name__ == "__main__":
    main()
