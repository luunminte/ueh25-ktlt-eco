def max_fn(a, b):
    return a if a > b else b

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

vmax = max_fn(a, b)
vmax = max_fn(vmax, c)

print("Max(%d, %d, %d) = %d" % (a, b, c, vmax))