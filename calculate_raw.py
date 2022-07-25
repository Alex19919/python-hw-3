import sys
if len(sys.argv) != 4:
    print('Arg len should be 4')
    sys.exit()

left_operand = sys.argv[1]
right_operand = sys.argv[3]

operation = sys.argv[2]

allowed_operations = ['+', '-', '/', '*', '%']



if operation not in allowed_operations:
    print('Operation is not allowed')
    sys.exit()
try:
    left_operand = int(left_operand)
    right_operand = int(right_operand)
except ValueError:
    print('Left and Right operands must be int')
    sys.exit()
if operation == '/' and right_operand == 0:
    print('Division by zero is not allowed')
    sys.exit()

# ## Option 1
match operation:
    case '+':
        print(left_operand + right_operand)
    case '-':
        print(left_operand - right_operand)
    case '*':
        print(left_operand * right_operand)
    case '/':
        print(left_operand / right_operand)
    case '%':
        print(left_operand % right_operand)
# Option 2
# if operation == '+':
#     print(left_operand + right_operand)
# elif operation == '*':
#     print(left_operand * right_operand)
# elif operation == '-':
#     print(left_operand - right_operand)
# elif operation == '/' and right_operand == 0:
#     print('Division by zero is not allowed')
# elif operation == '/':
#     print(left_operand / right_operand)
# elif operation == '%' and right_operand == 0:
#     print('Division by zero is not allowed')
# elif operation == '%':
#     print(left_operand % right_operand)



# print (calculation(left_operand, right_operand, operation))
