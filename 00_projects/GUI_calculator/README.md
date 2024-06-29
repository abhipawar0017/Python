**Calculator Application**

This project is a simple calculator application built using Python's Tkinter library. The calculator provides basic arithmetic operations and features a user-friendly graphical interface.

Features:
- Basic Arithmetic Operations: Supports addition, subtraction, multiplication, and division.
- Decimal Points and Modulo Operation: Includes support for decimal calculations and the modulo operation.
- Clear and Delete Functionality: Clear the entire display or delete the last character entered.
- Error Handling: Displays an error message for invalid operations to ensure a smooth user experience.

Usage :
- Launch the application by running the calculator.py script.
- Use the buttons on the interface to input numbers and perform operations.
- The display shows the current input and results.
- Use the 'C' button to clear the entire input, '⌫' button to delete the last character, and '=' button to calculate the result.

Code Structure :
- calculator.py: Contains the main code for the calculator application, including button definitions, event handling, and GUI layout.

How It Works
- Initialization: The Tkinter window is initialized with a specified geometry and title.
- Display: A text widget is used to display the current input and results.
- Buttons: Buttons for digits (0-9), operations (+, -, *, /, %, .), and special functions (C, CE, ⌫, =) are created and positioned using a grid layout.
- Event Handling: Functions are defined to handle button clicks, clear the display, delete the last character, and calculate the result.

Technologies Used :
- Python: The primary programming language.
- Tkinter: The standard Python interface to the Tk GUI toolkit.
