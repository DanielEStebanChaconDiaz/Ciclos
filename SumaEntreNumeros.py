n1 = int(input("Ingrese el primer numero:\n"))
n2 = int(input("Ingrese el segundo numero:\n"))
if n1 > n2:
    n1, n2 = n2, n1
suma = 0
for i in range(n1 + 1, n2):
    suma += i
print(f"La suma de los numeros {n1} y {n2} es: {suma}")
