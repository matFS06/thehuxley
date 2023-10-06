print('Helo World')
nome = input("Digite seu nome: ")
print("Você é amado por Deus", nome)

# LISTAS EM  PYTHON 

carros=["Mercedes", "Ferrari", "GOL"]
carros.append("Corola")
carros.append("LAmborguine")
carros.append("Skyline")

print(str(len(carros)) + " carros na lista")

print(carros)

carros2 = list(carros)
print("LISTA 2:", carros2)
carros.remove("GOL")

carros3 = carros+carros2
print(carros3)

print(str(len(carros)) + " carros na lista após remoção")

print(carros)

carros.clear()

print(carros)


#USO DO IF
a = 10
b = 5
op = "-"
resultado = 0 

if a>b:
    print("A é maior")

print("Congratulations")

if op=="-":
    resultado = a-b
    print("RESULTADO DA SUBTRAÇÃO É:", resultado)
