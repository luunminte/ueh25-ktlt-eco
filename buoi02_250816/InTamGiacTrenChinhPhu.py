# Input n
n = int(input())

# Nhập ma trận A
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Tam giác trên chéo chính (i < j)
tg_chinh = []
for i in range(n):
    for j in range(n):
        if i < j:
            tg_chinh.append(A[i][j])

# Tam giác trên chéo phụ (i + j < n - 1)
tg_phu = []
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            tg_phu.append(A[i][j])

# Output
print("Tam giac tren cheo chinh:", " ".join(map(str, tg_chinh)))
print("Tam giac tren cheo phu:", " ".join(map(str, tg_phu)))