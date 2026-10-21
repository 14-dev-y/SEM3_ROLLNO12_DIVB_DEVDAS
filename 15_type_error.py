"""Program 15: Catch TypeError when incompatible types are added."""

try:
    result = "Marks: " + 90
    print(result)
except TypeError:
    print("TypeError: convert the number to text before joining.")
