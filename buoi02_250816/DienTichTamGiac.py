import math

# Input
a = float(input())
b = float(input())
c = float(input())

# Process
p = (a + b + c) / 2.0
S = 0.0
if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
else:
    S = 0.0  # không tạo thành tam giác hợp lệ

# Output (2 chữ số thập phân)
print("Dien tich tam giac S = %.2f" % S)
