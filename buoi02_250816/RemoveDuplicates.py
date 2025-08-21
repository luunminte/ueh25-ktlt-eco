# Input
A = [1, 2, 3, 1, 2, 5, 6, 7, 8]

# Process
B = []
for x in A:
    if x not in B:   # chỉ thêm nếu chưa có trong B
        B.append(x)

# Output
print("Input A =", A)
print("Output B =", B)
