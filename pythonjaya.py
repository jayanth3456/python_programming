n = input()
n1 = input()
if n.isnumeric() and n1.isnumeric():
    a = int(input())
    b = int(input())
    c = input()
    if c == "+":
        print(a+b)
    elif c == "-":
        if a>b:
            print(a-b)
        else:
            print(b-a)
    elif c == "*":
        print(a*b)
    elif c == "%":
        print(a%b)
    elif c == "/":
        if a>b:
            print(a/b)
        else:
            print(b/a)
elif n.isnumeric() or n1.isnumeric():
    print("type of objects are different")
else:
    print("it is string")



    

        
        
    
    
    



