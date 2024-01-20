n = int(input("Ingresa un numero: \n"))
div = []
for i in range(1, n + 1):
    if n % i == 0:
        div.append(i)
print(f"Los divisores del numero ingresado son: {div}")