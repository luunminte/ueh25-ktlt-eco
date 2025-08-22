# Input n
n = int(input())

# Nhập ma trận A
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# In các dòng theo hình (so le xuôi - ngược)
dong = []
for i in range(n):
    if i % 2 == 0:   # dòng chẵn: in xuôi
        dong.append(A[i])
    else:            # dòng lẻ: in ngược
        dong.append(A[i][::-1])

# In các cột theo hình (so le xuôi - ngược)
cot = []
for j in range(n):
    col = [A[i][j] for i in range(n)]
    if j % 2 == 0:   # cột chẵn: in xuôi
        cot.append(col)
    else:            # cột lẻ: in ngược
        cot.append(col[::-1])

# Output
print("Cac dong:", dong)
print("Cac cot:", cot)
