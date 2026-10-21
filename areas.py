import math
def rectangle_area(width,length): return width*length
def triangle_area(height,base): return 0.5*height*base
def circle_area(radius): return math.pi*radius*radius
print("Dev's area calculator")
print("Rectangle:",rectangle_area(5,8))
print("Triangle:",triangle_area(6,4))
print("Circle:",round(circle_area(3),2))
