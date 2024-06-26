"""importamos la libreria necesaria"""
import requests

"""creamos función de la ciudad que introduzcamos por teclado"""

def tiempo_actual(ciudad):

    """creamos variable con la url y la ciudad pasada por teclado"""
    url="http://wttr.in/"+ciudad
    ""le pasamos al parámetro requests la ciudad con la url a la variable respuesta"""
    respuesta = requests.get(url)

    """ controlamos si la ciudad existe"""
    if respuesta.status_code == 200:
        print(respuesta.txt)
    else:
        print("revisa si la ciudad introducida, está bien escrita y existe")

""" Ahora introducimos el nombre la ciudad por teclado"""
ciudad = input("Introduce una ciudad: ")

"""llamamos a la función pasandole la ciudad escrita por teclado"""
tiempo_actual(ciudad)
    
