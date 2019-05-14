d = int(input("Enter dd :"))
m = int(input("Enter mm :"))
y = int(input("Enter yyyy :"))


if(y % 100 == 0 and y % 400 != 0):
    result = False
elif(y % 4 != 0):
    result = False
else:
    if(d == 29 and m == 2):
        result = True
    else:
        result = False
        
print(result)