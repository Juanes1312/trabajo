g = []
conta = 0

while(conta<10):
    h={}

    h["nombre"] = input("Digite nombre: ")
    h["color"] = input("Digite color: ")
    h["precio"] = input("Digite precio: ")
    g.append(h)

    conta = conta + 1
 
g.reverse()

print(f"{g}")
    