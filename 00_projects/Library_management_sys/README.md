Simple Library Management System

This project implements a basic library management system using Python, designed to manage book borrowing, returning, donating, and tracking operations. It provides a command-line interface for users to interact with the library functionalities.

Features :
- Book Management: Add, display, borrow, return, and donate books.
- User Interaction: Students can borrow, return, and donate books using their names.
- Tracking: Tracks borrowed books and their borrowers.
- Error Handling: Provides error messages for invalid inputs or unavailable books.

Technologies Used :
- Python: Primary programming language for the application logic.

Code Structure :
- library_management.py: Contains the main implementation of the library management system.

Classes:
- Library: Manages the books and their operations.
- Student: Handles interactions related to borrowing, returning, and donating books.

Functions:
- displayAvailableBooks(): Displays all available books in the library.
- borrowBook(name, bookname): Allows a student to borrow a book.
- returnBook(bookname): Handles the return of a borrowed book.
- donateBook(bookname): Adds a donated book to the library.
