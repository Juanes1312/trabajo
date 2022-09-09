n = int(input("Digita la cantidad de numeros a ingresar: "))
print(f"La cantidad de numeros es: {n}")
cont = 0
countMul2 = 0
countMul3 = 0
lista = []
while (cont < n):
    numero = int(input("Digite el numero a agregar: "))
    lista.append(numero)
    cont += 1
for e in lista:
    if(e % 2 == 0 and e % 3 == 0):
        countMul2 += 1
        countMul3 += 1
    elif(e % 2 == 0):
        countMul2 += 1
    elif(e % 3 == 0):
        countMul3 += 1
    else:
        print("no es multiplo")    
        
print(f"Multiplos de 2 son: {countMul2}")
print(f"Multiplos de 3 son: {countMul3}")
