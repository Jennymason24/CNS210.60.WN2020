def fibonacci(n):
    F0=0
    F1=1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return F0
    elif n == 1:
        return F1
   
    print(fibonacci(9))

