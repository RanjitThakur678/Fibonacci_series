'''fibonacci series with while loop without function'''
num = int(input("Enter a number : "))
a=0
b=1
count = 0

if num == a:
    print("Wrong Input")
elif num == 1:
    print(a)
elif num == 2:
    print(a,b)
else:
    
    while count < num:
        print(a)
        c = a+b
        a = b
        b = c
        count += 1 