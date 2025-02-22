def print_squares(n):
    for i in range(1, n):
        print(i ** 2)

if name == "main":
    n = int(input("Enter a number: "))
    print_squares(n)