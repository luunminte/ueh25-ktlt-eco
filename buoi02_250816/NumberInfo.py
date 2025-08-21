# Input
n = int(input())   # n < 1000

# Process
def number_of_digits(n: int) -> int:
    return len(str(abs(n)))

def sum_of_digits(n: int) -> int:
    s = 0
    for ch in str(abs(n)):
        s += int(ch)
    return s

def last_digit(n: int) -> int:
    return abs(n) % 10

def first_digit(n: int) -> int:
    return int(str(abs(n))[0])

pass  # helper functions

count = number_of_digits(n)
sumd  = sum_of_digits(n)
last  = last_digit(n)
first = first_digit(n)

# Output
print("%d has %d digits." % (n, count))

# in phép cộng các chữ số
digits = [int(ch) for ch in str(abs(n))]
print(" + ".join(str(d) for d in digits) + " = %d." % sumd)

print("Last digit is %d." % last)
print("First digit is %d." % first)
