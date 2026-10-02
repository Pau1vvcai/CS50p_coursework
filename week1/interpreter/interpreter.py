x, y, z = input(
        "Expression:"
        ).split(" ")

x, z = int(x), int(z)

if y == "+":
    print(float(x+z))

if y == "-":
    print(float(x-z))

if y == "*":
    print(float(x*z))

if y == "/" and z != "0":
    print(float(x/z))
