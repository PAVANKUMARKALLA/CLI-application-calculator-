# CLI-application-calculator-
cli application for calculator using python
### *Step-by-Step Explanation*

1. *Overview of the Program*
   - Start by describing the purpose: "This is a Python-based command-line calculator that performs basic arithmetic operations (add, subtract, multiply, divide, modulus) and stores calculation history for user reference."
    
2. *Key Features*
   - *Arithmetic Operations*: Explain how the program uses conditional statements to handle operations like addition, subtraction, multiplication, division, and modulus.
 - *Error Handling*: Discuss how exceptions (InvalidArgs) are raised for invalid inputs or unsupported operations.

3. *Code Structure*
   - *Main Functionality*:
     - The main() function processes user input, performs calculations based on the operation provided, and stores results in the history list.
   - *Global History List*:
     - A global variable history is used to store past calculations.
   - *Error Handling*:
     - Invalid arguments raise an exception with helpful error messages.
     - Division/modulus by zero is handled explicitly to avoid runtime errors.
   - *User Commands*:
     - The ? command retrieves past calculations stored in the history list.

4. *Design Choices*
   - Modular Design: The main functionality is encapsulated in a function (main()), making it easy to extend or modify.
   - User-Friendly Interface: Clear error messages and usage instructions guide users.
   - Scalability: The program can be extended to include more operations or features like saving history to a file.

5. *Demonstration*
   - Walk through an example:
     bash
     python calc.py add 5 3  # Outputs: 8
     python calc.py sub 10 4 # Outputs: 6
       - Show how invalid inputs (e.g., unsupported operations or missing arguments) are handled gracefully.

6. *Why This Code Is Effective*
   - "This code demonstrates my ability to write clean, modular Python programs with error handling and user-friendly features. It also shows my understanding of basic programming concepts like loops, conditionals, and exception handling."
