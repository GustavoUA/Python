#definimos la función y le pasamos el texto y la letra a buscar
def contar(texto,buscar):
#inicializamos un contador
    contador=0
#pasamos la letra a buscar a la variable "letra"
    letra=buscar
#recorremos el texto que hemos introducido
    for i in texto:
#comparamos letra por letra si se encuentra la letra que buscamos, si existe suma 1
        if(i==letra):
            contador+=1
#imprime o muestra por pantalla el resultado en forma numérico
    print(contador)

#variable que usamos para introducir el texto por teclado
texto=input("introduce un texto: ")

#indicamos que el texto introducido si tiene alguna mayúscula la convierta en minúscula
texto = texto.lower()

#introducimos la letra que deseamos buscar
buscar=input("introduce la letra a buscar: ")

#la convertimos a minúscula
buscar = buscar.lower()

#llamamos a la función y le pasamos los dos parámetros necesarios.
contar(texto,buscar)
