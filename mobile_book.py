mobiles={}
def create():
    global mobiles
    mobiles={"Samsung A55":{"price":39999,"features":"AMOLED, 5G"}}
def add_mobile(name,price,features): mobiles[name]={"price":price,"features":features}
def update_mobile(name,price=None,features=None):
    if name in mobiles:
        if price is not None: mobiles[name]["price"]=price
        if features is not None: mobiles[name]["features"]=features
def delete_mobile(name):
    if name in mobiles: del mobiles[name]
create(); add_mobile("Dev's Choice Phone",30000,"5G, long battery")
update_mobile("Samsung A55",price=37999); delete_mobile("Dev's Choice Phone")
print(mobiles)
