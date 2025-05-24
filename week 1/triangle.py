# lower Triangle
print("Lower Triangle:")
for i in range (1,6):
    print("*" * i)

# Upper Triangle 
print("\nUpper Triangle:")
for i in range (5,0,-1):
    print(" "*(6-i) + "*"*i)

#Pyramid
print("\nPyramid:")
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2*i-1))