# Input (danh sách ban đầu)
A = ['3', '27', '5', '123', '9', '1']

# Process
# string compare (mặc định của sorted)
sorted_str = sorted(A)

# integer compare (so sánh theo int)
sorted_int = sorted(A, key=int)

# Output
print("Original list:", A)
print("Sorted by string compare:", sorted_str)
print("Sorted by integer compare:", sorted_int)
