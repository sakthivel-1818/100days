

def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operators={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div}


def calc():
    should_continue=True
    value=0
    while should_continue:
        n1 = float(input("what is the first number:"))
        operation = input("+\n-\n*\n/\n pick the operation")
        n2 = float(input("what is the second number"))

        result = operators[operation](n1, n2)
        print(f"{n1}{operation}{n2}={result}")
        value = result
        repeat_calc=True
        while repeat_calc:
            continuous_cal = input(f"Type 'y' to continue calculating with ''{result}'', or type 'n' to start a new calculation:").lower()
            if continuous_cal=="y":
                operation = input(f"+\n-\n*\n/\n pick any operation:")
                new_num = float(input("what is the next number:"))
                result= operators[operation](value, new_num)
                print(f"{value}{operation}{new_num}={result}")
                value=result
            elif continuous_cal=="n":
                repeat_calc=False
                print("\n"*20)
                calc()

calc()