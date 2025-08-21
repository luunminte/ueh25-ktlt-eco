# Input
math = float(input())     # điểm Toán
physic = float(input())   # điểm Lý
chem = float(input())     # điểm Hóa

# Process
def average(math, physic, chem):
    return (math*2 + physic*3 + chem) / 6
pass  # average

def classify(gpa: float) -> str:
    if 8 <= gpa <= 10:
        return "Good"
    elif 6.5 <= gpa < 8:
        return "Pretty"
    elif 5 <= gpa < 6.5:
        return "Average"
    else:
        return "Weak"
pass  # classify

gpa = average(math, physic, chem)
rating = classify(gpa)

# Output
print("Average point = %.2f, rating %s." % (gpa, rating))
