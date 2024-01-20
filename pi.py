n = int(input("Ingrese el numero de digitos;\n"))
pi = 0
signo = 1
for i in range (n):
    T = signo / (2*i+1)
    pi += T
    signo *= -1
valorpi = 4*pi
print(f"La estimacion de pi es: {valorpi}")