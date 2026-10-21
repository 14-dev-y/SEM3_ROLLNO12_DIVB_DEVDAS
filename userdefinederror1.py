class PriceError(Exception):
    pass


class quantityError(Exception):
    pass


try:
    price = int(input("Enter your Price: "))

    if price < 100 or price > 1000:
        raise PriceError("PLSSSS ENTER  BETWEEN 100 AND 1000")

    print("YOU HAVE ENTERED A VALID PRICE:", price)
   
    quantity = int(input("Enter your Quantity: "))
    
    if quantity < 1 or quantity > 100:
        raise quantityError("PLSSSS ENTER  BETWEEN 1 AND 100")

    print("YOU HAVE ENTERED A VALID QUANTITY:", quantity)

except PriceError as a:
    print("Error:", a)
    
except quantityError as b:
    print("Error:", b)