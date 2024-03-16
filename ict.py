class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero!"

# Create an instance of the Calculator class
calc = Calculator()

while True:
    expression = input("Enter an expression (e.g., '1+1'): ")
    
    if expression.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    
    # Split the expression into operands and operator
    operands = expression.split('+') if '+' in expression else \
               expression.split('-') if '-' in expression else \
               expression.split('*') if '*' in expression else \
               expression.split('/')
    operator = '+' if '+' in expression else \
               '-' if '-' in expression else \
               '*' if '*' in expression else \
               '/'
    
    if len(operands) != 2 or not operands[0].strip().isdigit() or not operands[1].strip().isdigit():
        print("Invalid expression. Please enter a valid expression.")
        continue
    
    num1 = float(operands[0].strip())
    num2 = float(operands[1].strip())
    

    
    if operator == '+':
        print("Result:", calc.add(num1, num2))
    elif operator == '-':
        print("Result:", calc.subtract(num1, num2))
    elif operator == '*':
        print("Result:", calc.multiply(num1, num2))
    elif operator == '/':
        print("Result:", calc.divide(num1, num2))

