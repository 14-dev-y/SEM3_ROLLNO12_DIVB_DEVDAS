d1 = {
    "S1": {
        "roll no" : 1,
        "name": "Dev",
        "age" : 20,
        "course" : "MSCIT",
        "sem" : 3,
        "city" : "ahmedabad",
        "phone number" : 8141045916,
         "subjects": {"Python": 90, "DBMS": 85, "OS": 88}
    },

     "S2": {
            "roll no" : 2,
            "name": "Tanish",
            "age" : 19,
            "course" : "MSCIT",
            "sem" : 5,
            "city" : "ahmedabad",
            "phone number" :  1234567812,
             "subjects": {"Python": 77, "DBMS": 65, "OS": 78}
        },

         "S3": {
                "roll no" : 3,
                "name": "pooja",
                "age" : 19,
                "course" : "MSCIT",
                "sem" : 3,
                "city" : "ahmedabad",
                "phone number" : 2345678912,
                 "subjects": {"Python": 70, "DBMS": 85, "OS": 98}
            },

             "S4": {
                    "roll no" : 4,
                    "name": "Maahi",
                    "age" : 19,
                    "course" : "MSCIT",
                    "sem" : 5,
                    "city" : "ahmedabad",
                    "phone number" : 567891234,
                    "subjects": {"Python": 90, "DBMS": 85, "OS": 88}
                },

                 "S5": {
                        "roll no" : 5,
                        "name": "Dhruv",
                        "age" : 20,
                        "course" : "MSCIT",
                        "sem" : 7,
                        "city" : "ahmedabad",
                        "phone number" : 1234567891,
                        "subjects": {"Python": 82, "DBMS": 79, "OS": 84}
                    }
}
for key, d2 in d1.items():
    print("Roll no:", d2["roll no"])
    print("Student name :", d2["name"])
    print("age:", d2["age"])
    print("course:", d2["course"])
    print("sem:", d2["sem"])
    print("city:", d2["city"])
    print("phone no:",  d2["phone number"])
    print("Subjects and Marks:", d2["subjects"])
    print("\n")


roll = int(input("Enter Roll No: "))

for key, d2 in d1.items():
    if d2["roll no"] == roll:
        print(d2)
        break
else:
    print("Student not found")
 