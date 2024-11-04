listan = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista1a9 = []
lista8a13 = []
listapares = []
listaimpar = []
listamult2 = []
listamult3 = []
listamult4 = []
intervalo10a15 = []
lista1a9_2 = []
print("intervalo de 1 a 9")
for i in listan:
    if i >= 1 and i <10:
        lista1a9.append(i)
print(lista1a9)

print("intervalo de 8 a 13")
for i in listan:
    if i >= 8 and i <14:
        lista8a13.append(i)
print(lista8a13)

print("Numeros pares")
for i in listan:
    if i % 2 == 0:
        listapares.append(i)
print(listapares)

print("Numeros impares")
for i in listan:
    if i % 2 != 0:
        listaimpar.append(i)
print(listaimpar)
print("Multiplos de 2")
for i in listan:
    if i % 2 == 0:
        listamult2.append(i)
print(listamult2)

print("Multiplos de 3")
for i in listan:
    if i % 3 == 0:
        listamult3.append(i)
print(listamult3)

print("Multiplos de 4")
for i in listan:
    if i % 4 == 0:
        listamult4.append(i)
print(listamult4)

print("Lista reversa:")
listareversa = listan[::-1]
print(listareversa)

for i in listan:
    if i >=10 and i <=15:
        intervalo10a15.append(i)

soma10a15 = sum(intervalo10a15)


for i in listan:
    if i >=3 and i <=9:
        lista1a9_2.append(i)

lista1a9_2 = sum(lista1a9_2)

print("Razão entre a soma dos intervalos: ")
razaodosintervalos = (soma10a15 / lista1a9_2)
print(razaodosintervalos)









