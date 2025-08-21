# Input
a = float(input())
b = float(input())
op = input().strip()

# Process
def calculate(a, b, op):
    ans = None
    if op == '+':
        ans = a + b
    elif op == '-':
        ans = a - b
    elif op == '*':
        ans = a * b
    elif op == '/':
        if b != 0:
            ans = a / b
    return ans
pass  # calculate

ans = calculate(a, b, op)

# Output
if ans is not None:
    print("%.0f %s %.0f = %.2f" % (a, op, b, ans))
else:
    print("Error: invalid operation or division by zero")
