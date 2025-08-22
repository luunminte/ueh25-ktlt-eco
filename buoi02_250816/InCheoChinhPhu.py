# Input n
n = int(input())

# Nhập ma trận A
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Lấy các phần tử trên đường chéo chính
cheo_chinh = [A[i][i] for i in range(n)]

# Lấy các phần tử trên đường chéo phụ
cheo_phu = [A[i][n - 1 - i] for i in range(n)]

# Output
print("Cac phan tu tren cheo chinh:", " ".join(map(str, cheo_chinh)))
print("Cac phan tu tren cheo phu:", " ".join(map(str, cheo_phu)))
