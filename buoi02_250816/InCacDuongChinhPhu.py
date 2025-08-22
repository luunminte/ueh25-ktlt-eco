# Input n
n = int(input())

# Nhập ma trận A
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Các đường song song với chéo chính
ds_chinh = []
for k in range(-(n-1), n):  # độ lệch i - j
    duong = []
    for i in range(n):
        j = i - k
        if 0 <= j < n:
            duong.append(A[i][j])
    if duong:
        ds_chinh.append(duong)

# Các đường song song với chéo phụ
ds_phu = []
for k in range(0, 2*n - 1):  # i + j = k
    duong = []
    for i in range(n):
        j = k - i
        if 0 <= j < n:
            duong.append(A[i][j])
    if duong:
        ds_phu.append(duong)

# Output
print("Cac duong song song cheo chinh:", ds_chinh)
print("Cac duong song song cheo phu:", ds_phu)
