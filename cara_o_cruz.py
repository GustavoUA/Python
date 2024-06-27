#Cara o Cruz
#importamos la libreria
import random 

#introducimos por teclado una de las dos posibilidades
usuario=input("¿Cara o Cruz?")

#creamos la lista con las dos posibilidades que jugará el ordenador
probabilidad = ["Cara","Cruz"]

#lanzamos el random, donde el ordenador decidirá si elije cara o Cruz
ordenador = random.choice(probabilidad)

#devolvemos lo introducido en minúscula para el control de variables.
ordenador = ordenador.lower()
usuario = usuario.lower()

#comprobamos si coincide la elección del usuario con la elección del ordenador.
if(ordenador==usuario):
    print("Has acertado")
else:
    print("Has perdido")

print("El ordenador ha elegido", ordenador)
