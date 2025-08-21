# Input
A = [12, 24, 35, 70, 88, 120, 155]

# Process
remove_index = {0, 1, 2, 5}  # các vị trí cần xóa

# dùng list comprehension + enumerate
result = [val for idx, val in enumerate(A) if idx not in remove_index]

# Output
print("Original list:", A)
print("After removing positions 1,2,3,6:", result)
