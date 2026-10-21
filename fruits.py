fruits=["Apple","Banana","Mango"]
def show(): print("Fruits:",fruits)
def add_fruit(name):
    global fruits
    fruits.append(name)
def insert_fruit(name,position=1):
    global fruits
    fruits.insert(position,name)
def update_fruit(old_name=None,new_name=None):
    global fruits
    if old_name in fruits and new_name is not None: fruits[fruits.index(old_name)]=new_name
def remove_fruit(value):
    global fruits
    if isinstance(value,int):
        if 0<=value<len(fruits): fruits.pop(value)
    elif value in fruits: fruits.remove(value)
def arrange():
    global fruits
    fruits.sort()
show(); add_fruit("Orange"); insert_fruit("Strawberry")
update_fruit(old_name="Mango",new_name="Kiwi"); remove_fruit("Banana"); arrange(); show()
# global() built-in returns the global symbol table; global keyword allows reassignment.
