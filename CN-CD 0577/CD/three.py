# Define operators and their precedence
OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2}


### Infix to Postfix Conversion ###

def infix_to_postfix(formula):
    """
    Converts infix notation to postfix notation.

    Args:
        formula (str): Infix expression.

    Returns:
        str: Postfix expression.
    """
    stack = []
    output = ""

    for char in formula:
        if char not in OPERATORS:
            output += char
        elif char == '(':
            stack.append('(')
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # pop '('
        else:
            while stack and stack[-1] != '(' and PRECEDENCE[char] <= PRECEDENCE[stack[-1]]:
                output += stack.pop()
            stack.append(char)

    # Process leftover operators
    while stack:
        output += stack.pop()

    print(f"POSTFIX: {output}")
    return output

### Three Address Code Generation ###

def generate_three_address_code(postfix):
    """
    Generates three address code from postfix notation.

    Args:
        postfix (str): Postfix expression.
    """
    print("### THREE ADDRESS CODE GENERATION ###")
    exp_stack = []
    temp_var = 1

    for char in postfix:
        if char not in OPERATORS:
            exp_stack.append(char)
        else:
            print(f"t{temp_var} := {exp_stack[-2]} {char} {exp_stack[-1]}")
            exp_stack = exp_stack[:-2]
            exp_stack.append(f"t{temp_var}")
            temp_var += 1


# Main program
expression = input("INPUT THE EXPRESSION: ")
# prefix = infix_to_prefix(expression)
postfix = infix_to_postfix(expression)
generate_three_address_code(postfix)
