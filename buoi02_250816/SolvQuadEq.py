import math

# Input
a = float(input())
b = float(input())
c = float(input())

# Process
def solve_quadratic(a, b, c):
    # Trường hợp bậc 1 hoặc vô số nghiệm
    if a == 0:
        if b == 0:
            if c == 0:
                return "Unlimited solutions"
            else:
                return "No solution"
        else:
            x = -c / b
            return "x1=%.2f" % x
    
    # Phương trình bậc 2
    delta = b*b - 4*a*c
    if delta < 0:
        return "No solution"
    elif delta == 0:
        x = -b / (2*a)
        return "x1=%.2f" % x
    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return "x1=%.2f, x2=%.2f" % (x1, x2)
pass  # solve_quadratic

ans = solve_quadratic(a, b, c)

# Output
print(ans)
