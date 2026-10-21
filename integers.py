items=["Dev",12,"Tanish",7,3.5,"Maahi",20,True,"Pooja"]
integers=list(filter(lambda x:isinstance(x,int) and not isinstance(x,bool),items))
print("Mixed:",items); print("Integers:",integers)
