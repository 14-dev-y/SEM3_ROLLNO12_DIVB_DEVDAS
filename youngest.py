students = {
    "D": [19, "MSc IT", "Python"],
    "T": [20, "BCA", "Maths"],
    "M": [18, "BSc", "Computer"]
}

youngest = min(students, key=lambda name: students[name][0])
print("Youngest student initial:", youngest)
print("Details:", students[youngest])
