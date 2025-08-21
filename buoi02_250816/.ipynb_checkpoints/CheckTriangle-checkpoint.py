# Input
a = float(input())
b = float(input())
c = float(input())

# Process
def max3(a, b, c):
    m = a
    if b > m: m = b
    if c > m: m = c
    return m
pass  # max3

def can_form_triangle(a, b, c):
    # Sắp xếp để áp dụng điều kiện rút gọn
    x, y, z = sorted([a, b, c])  # x <= y <= z
    return x > 0 and y > 0 and z > 0 and (x + y > z)
pass  # can_form_triangle

m = max3(a, b, c)
ok = can_form_triangle(a, b, c)

# Output
# Dòng minh họa theo đề
print("Max(%.0f, %.0f, %.0f)= %.0f." % (a, b, c, m))
# Kết quả kiểm tra tam giác
print("Yes" if ok else "No")
