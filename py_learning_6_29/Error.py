def add_two_number():
    a = input("input first number:")
    b = input("input second number:")

    try:
        c = int(a) + int(b)
    except ValueError:
        error = "Not a number!"
        print(error)
    else:
        print("The result is " + str(c))
