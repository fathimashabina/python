l=int(input("enter the length of the rectangle:"))
b=int(input("enter the breadth of the rectangle:"))
s=int(input("enter the side of the square:"))
area =lambda l,b : l*b
perimeter=lambda l,b: 2 *(l+b)
sperimeter=lambda  s:4*s
sarea=lambda s: s*s
print("area of the rectangle is",area(l,b))
print("perimeter of the rectangle is ",perimeter(l,b))
print("area of the square",sarea(s))
print("perimeter of the square ",sperimeter(s))

