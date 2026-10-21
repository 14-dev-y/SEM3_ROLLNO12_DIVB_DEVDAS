def extract_string(str_list1, l):
    return [word for word in str_list1 if len(word) >= l]

str_list1 = ['Python', 'list', 'exercises', 'practice', 'solution']
l = 8
print(extract_string(str_list1, l))
