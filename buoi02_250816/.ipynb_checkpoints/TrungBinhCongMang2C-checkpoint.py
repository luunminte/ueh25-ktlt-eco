# Input n, m
n, m = map(int, input().split())

# Nhập ma trận A
A = []
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

# Tính trung bình cộng các số dương
tong = 0
dem = 0
for i in range(n):
    for j in range(m):
        if A[i][j] > 0:
            tong += A[i][j]
            dem += 1

if dem > 0:
    print("Trung binh cong cac so duong:", tong / dem)
else:
    print("Khong co so duong nao trong ma tran")