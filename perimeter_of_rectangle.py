def peri_of_rectangle(l,b):
    perimeter = 2*(l+b)
    return perimeter

x = int(input("enter your length : "))
y = int(input("enter your breadth: "))
z = peri_of_rectangle(x,y)
print(z)
