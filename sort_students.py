students=[
 {"name":"Amit","age":25},{"name":"Bina","age":22},{"name":"Dax","age":25},
 {"name":"Dev","age":22},{"name":"Tanish","age":25},{"name":"Dhruv","age":22},
 {"name":"Maahi","age":23},{"name":"Pooja","age":23},{"name":"Adishree","age":21},
 {"name":"Rutvi","age":23}]
for student in sorted(students,key=lambda s:(s["age"],s["name"])):
    print(student)
