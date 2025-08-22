# Input n
n = int(input())

# Nhập mảng
nums = list(map(int, input().split()))

# Thuật toán Boyer-Moore Majority Vote
candidate = None
count = 0
for num in nums:
    if count == 0:
        candidate = num
    count += (1 if num == candidate else -1)

# Output
print(candidate)
