items = input('Enter values separated by spaces (e.g. Dev 1 Tanish 2): ').split()
check_digit = lambda item: item.isdigit()
print([check_digit(item) for item in items])
