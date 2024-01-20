# Cuadrado
# A = int(input("Ingrese la altura:\n"))
# B = int(input("Ingrese el ancho:\n"))
# for i in range(A):
#     for j in range(B):
#         print("*", end=" ")
#     print()

# Triangulo
# A = int(input("Ingrese la altura:\n"))
# for i in range(1, A + 1):
#     esp = A - 1
#     print(" " * esp + "*" * (2*i-1))

#Hexagono
L = int(input("Ingrese la longitud: \n"))
for i in range(L):
    esp = L - i - 1
    print(" " * esp * 2 + "* " * (i + 1))
for i in range(L - 2, -1, -1):
    esp = L - i - 1
    print(" " * esp * 2 + "* " * (i + 1))

