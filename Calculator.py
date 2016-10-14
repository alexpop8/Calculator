def adunare(x, y):
    return x + y
def scadere(x, y):
    return x - y
def inmultire(x, y):
    return x * y
def impartire(x, y):
    return x / y
def patrat(x):
    return x * x
def cub(x):
    return x * x * x

print("Selectează optiunea")
print("1.Adunare")
print("2.Scadere")
print("3.Inmultire")
print("4.Impartire")
print("5.Patratul unui numar")
print("6.Cubul unui numar")

optiune = input("Introdu o optiune: ")

num1 = int(input("x= "))

if optiune == '5':
    print(num1, "*", num1, "=", patrat(num1))
elif optiune == '6':
    print(num1, "*", num1, "*", num1, "=", cub(num1))
          
num2 = int(input("y= "))

if optiune == '1':
    print(num1, "+", num2, "=", adunare(num1, num2))

elif optiune == '2':
    print(num1, "-", num2, "=", scadere(num1, num2))

elif optiune == '3':
    print(num1, "*", num2, "=", inmultire(num1, num2))

elif optiune == '4':
    print(num1, "/", num2, "=", impartire(num1, num2))



else:
    print("Alegerea nu exista.")
