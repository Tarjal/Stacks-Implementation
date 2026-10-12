
# Stack-Based Mathematical Expression Evaluator

## Project Overview

This project implements a Python program that reads mathematical expressions from `input.txt`, evaluates each expression using a stack-based approach, and writes the calculated results to `output.txt`.

The program demonstrates the use of:
- Stack data structures
- Push, pop, peek, and is-empty operations
- Mathematical expression evaluation
- Operator precedence
- Parentheses
- File input and output
- Sequential processing of multiple expressions

## Files in This Project

- `main.py` - Python program that evaluates the expressions.
- `input.txt` - Contains the mathematical expressions to be evaluated.
- `output.txt` - Contains the calculated results.
- `README.md` - Project documentation.

## Requirements

- Python 3.x
- No external Python packages are required.

## Input File Format

Each mathematical expression is written on a separate line. A separator line containing `-----` is used between expressions.

Example:

```text
3+5*2
-----
(8/4)+7*2
-----
10 - (2 + 3) * 4



## Expected Output Format

The result of each expression is written in the same order as the input expressions. The separator lines are preserved.

Example:

```text
13
-----
16
-----
-10
```

## How to Run the Program

1. Make sure `main.py`, `input.txt`, and `output.txt` are in the same folder.
2. Open Command Prompt, PowerShell, or a terminal in the project folder.
3. Run:

```bash
python main.py
```

4. The program reads the expressions from `input.txt`.
5. It evaluates each expression using a stack.
6. It writes the results to `output.txt`.

## Stack Operations

The Stack class provides the following operations:

- **push()** - adds an item to the top of the stack.
- **pop()** - removes and returns the item at the top.
- **peek()** - returns the top item without removing it.
- **is_empty()** - checks whether the stack is empty.

The stack follows the **Last-In, First-Out (LIFO)** principle.

## Operator Precedence

The program follows normal arithmetic precedence:

1. Parentheses `( )`
2. Multiplication `*` and division `/`
3. Addition `+` and subtraction `-`

For example:

`3 + 5 * 2`

is evaluated as:

`3 + (5 * 2) = 13`

## Test Cases

The input file includes these test expressions:

| Expression | Expected Result |
|---|---:|
| `3 + 5 * 2` | 13 |
| `(8 / 4) + 7 * 2` | 16 |
| `10 - (2 + 3) * 4` | -10 |
| `8 - 3 + 2` | 7 |

## Testing

The test cases check:
- Multiplication precedence
- Division
- Parentheses
- Addition and subtraction
- Negative results
- Left-to-right evaluation for operators with equal precedence
- Correct processing of multiple expressions
- Correct preservation of separator lines

## Project Structure

```text
stack_expression_assignment/
│
├── main.py
├── input.txt
├── output.txt
└── README.md
```

## Academic Context

This project is prepared for the DCOMP320 Data Structures and Algorithm assignment on Stack Implementation at Limkokwing University of Creative Technology.

The assignment focuses on applying a stack to mathematical expression evaluation and demonstrating file input/output.

## Reference
- Python Software Foundation. Python 3 Documentation.
