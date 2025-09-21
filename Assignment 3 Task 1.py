a = int(input("enter a number"))
def fact():
    global a
    s=1
    while a>0:
        s=s*a
        a=a-1
    return s
t = fact()
print("factorial of the number is", t)
