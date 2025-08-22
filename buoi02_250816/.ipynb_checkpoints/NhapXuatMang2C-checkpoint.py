# Input n, m
n, m = map(int, input().split())

# Nhập mảng A
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Output
print("Array A:")
for row in A:
    print(" ".join(map(str, row)))