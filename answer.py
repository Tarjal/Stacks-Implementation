class Stack:
    #Stack implementation for expression evaluation
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


def precedence(operator):
    #Return precedence of operators
    if operator in ['+', '-']:
        return 1
    elif operator in ['*', '/']:
        return 2
    elif operator == '**':
        return 3
    return 0


def apply_operator(operators, values):
    #Apply operator to values
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    
    #performing operations
    if operator == '+':
        values.push(left + right)
    elif operator == '-':
        values.push(left - right)
    elif operator == '*':
        values.push(left * right)
    elif operator == '/':
        values.push(left / right)
    elif operator == '**':
        values.push(left ** right)


def evaluate_expression(expression):
    #Evaluate mathematical expression using stack
    
    expression = expression.replace(" ", "") # Remove whitespace
    
    values = Stack()
    operators = Stack()
    
    i = 0
    while i < len(expression):
        # Handle numbers
        if expression[i].isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.push(num)
            continue
        
        # Handle parentheses
        elif expression[i] == '(':
            operators.push(expression[i])
        
        elif expression[i] == ')':
            while not operators.is_empty() and operators.peek() != '(':
                apply_operator(operators, values)
            operators.pop()  # Remove '('
        
        # Handle operators
        else:
            # Check for exponentiation operator '**'
            if (i + 1 < len(expression) and expression[i] == '*' 
                and expression[i + 1] == '*'):
                current_operator = '**'
                i += 1  # Skip next '*'
            else:
                current_operator = expression[i]
            
            while (not operators.is_empty() and 
                   precedence(operators.peek()) >= precedence(current_operator)):
                apply_operator(operators, values)
            
            operators.push(current_operator)
        
        i += 1
    
    # Apply remaining operators
    while not operators.is_empty():
        apply_operator(operators, values)
    
    return values.pop()


def process_file(input_file='input.txt', output_file='output.txt'):
    """Process input file and write results to output file"""
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                line = line.strip()
                
                # Check if line is a separator
                if line and all(c in '-=' for c in line):
                    outfile.write(line + '\n')
                elif line:  # It's an expression to evaluate
                    try:
                        result = evaluate_expression(line)
                        outfile.write(f"{result}\n")
                    except Exception as e:
                        outfile.write(f"Error evaluating: {line} -> {str(e)}\n")
        
        print(f"Processing complete. Results written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"Error processing files: {str(e)}")


# Main execution
if __name__ == "__main__":
    print("Sample input.txt created.")
    process_file()