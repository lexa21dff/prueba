vectoruno = []
vectordos = []
N = int (input('ingresar cuantos valores quiere  ver del vector')) 
print('ingresar los valores para agregar al vector')
if N <= 15: # el tamaño maximo de los vectores
    for i in range(N):
        b = int(input('ingrese un valor al vector uno '))
        if b <= 30:
            vectoruno.append(b)
        else:
            print('el valor ingresado es mayor que 30')
            
    for i in range(N):
        b = int(input('ingrese un valor al vector dos '))
        if b <= 30:
            vectordos.append(b)
        else:
            print('el valor ingresado es mayor que 30')

else:
    print('no se puede superar este valor')

print('primer vector',vectoruno)
print('segundo vector',vectordos)

vectoruno.sort() # orden ascedente del vector uno
vectordos.sort() # orden ascedente del vector dos
print('primer vector orden ascedente',vectoruno)
print('segundo vector orden ascedente',vectordos)

lista = [] #suma de los dos vectores
lista2 = [] #orden ascedente de los dos vectores
suma = 0
for i in vectoruno:
  lista.extend([i])


for i in vectordos:
  suma = suma + i
  lista.extend([suma])


print(lista)
lista2.sort()
print(lista2)
