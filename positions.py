def findString(string1,string2="all"):
    positions=[]; start=0
    while True:
        pos=string1.find(string2,start)
        if pos==-1: break
        positions.append(pos); start=pos+1
    return positions if positions else "String2 was not found"
s="Hello all, Good Morning to all. Dev and Tanish say hello to all."
print("Default search:",findString(s))
print("Search Dev:",findString(s,"Dev"))
