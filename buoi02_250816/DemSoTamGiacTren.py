# Input n
n = int(input())

# Nhập ma trận A
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Biến đếm
so_am = so_duong = so_khong = 0

# Duyệt tam giác trên chéo chính (i < j)
for i in range(n):
    for j in range(n):
        if i < j:
            if A[i][j] < 0:
                so_am += 1
            elif A[i][j] > 0:
                so_duong += 1
            else:
                so_khong += 1

# Output
print("Trong nua tam giac tren cheo chinh:")
print("+", so_am, "so am")
print("+", so_duong, "so duong")
print("+", so_khong, "so khong")
