# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round (x+y)

# to round integer 
# z = round (x / y, 2)

# z = x / y

# this is the way you specify in f string how many digits you wanna round up to 
# print (f"{z:.2f}")

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()