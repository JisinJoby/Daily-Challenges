from math import factorial as fact

n=int(input("Enter the 1st dimension of Grid:"))
m=int(input("Enter the 2nd dimension of Grid:"))
Grid_routes= fact(n+m) // fact(n) // fact(m)
print(Grid_routes)
