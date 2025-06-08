# Homework 1

```python
# Initialize the library inventory
library = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "Classic"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction"},
    # Add more books here...
]

# Main program loop
while True:
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Generate a report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Add a book
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = int(input("Enter the year of the book: "))
        genre = input("Enter the genre of the book: ")

        book = {"title": title, "author": author, "year": year, "genre": genre}
        library.append(book)
        print(f"Book '{title}' added successfully.")

    elif choice == "2":
        # Remove a book
        title = input("Enter the title of the book to remove: ")
        found = False

        for book in library:
            if book["title"].lower() == title.lower():
                library.remove(book)
                found = True
                print(f"Book '{title}' removed successfully.")
                break

        if not found:
            print(f"Book '{title}' not found in the library.")

    elif choice == "3":
        # Search for a book
        search_term = input("Enter a search term (title, author, or genre): ").lower()
        found_books = []

        for book in library:
            if (search_term in book["title"].lower() or
                search_term in book["author"].lower() or
                search_term in book["genre"].lower()):
                found_books.append(book)

        if found_books:
            print("\nMatching books:")
            for book in found_books:
                print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}")
        else:
            print("No books matched the search term.")

    elif choice == "4":
        # Generate a report
        total_books = len(library)
        unique_genres = set(book["genre"] for book in library)
        genre_counts = {genre: sum(1 for book in library if book["genre"] == genre) for genre in unique_genres}
        most_recent_book = max(library, key=lambda book: book["year"])

        print("\nLibrary Report")
        print(f"Total number of books: {total_books}")
        print("Unique genres:", ", ".join(unique_genres))
        print("Number of books in each genre:")
        for genre, count in genre_counts.items():
            print(f"{genre}: {count}")
        print(f"Most recent book: {most_recent_book['title']} ({most_recent_book['year']})")

    elif choice == "5":
        # Exit the program
        print("Exiting the Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
```