a = int(input("Enter number one:"))
b = int(input("Enter number two:"))
c = int(input("Enter number three:"))
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
