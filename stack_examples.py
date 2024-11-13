

def check_balanced_parenthesis(expresion):
    my_stack = []
    for ch in expresion:
        if ch == "(":
            my_stack.append(ch)
        elif ch == ")":
            try:
                my_stack.pop()
            except IndexError:
                return False
    return len(my_stack) == 0 


print(check_balanced_parenthesis("(+(+)+)+(+(+)+)"))

def PolishNotation(str):
    items = str.split()
    result = ""
    operator_stack = []
    for i in items:
        if i in "(*/":
            operator_stack.append(i)
        elif i in "+-":
            while len(operator_stack) > 0 and operator_stack[-1] in "*/":
                result += operator_stack.pop()
            operator_stack.append(i)
        elif i == ")":
            while len(operator_stack) > 0 and operator_stack[-1] != "(":
                op = operator_stack.pop()
                if op != "(":
                    result += op
        else:
            result += i
    while len(operator_stack)> 0:
        op = operator_stack.pop()
        if op != "(":
            result += op
    return result

print(PolishNotation("( ( A + B ) - C * ( D / E ) ) + F"))

def operation(a,b,op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b



def evaluation(str):
    result_stack = []
    items = str.split()
    for i in items:
        if i in "+-*/":
            n1 = result_stack.pop()
            n2 = result_stack.pop()
            result_stack.append(operation(n2,n1,i))
        else:
            result_stack.append(int(i))
    return result_stack.pop()


print(evaluation("1 -10 1 * 1 - +"))