import argparse
import json
from mueble import Silla, Mesa, Armario, Mueble

#creacion Lista de muebles de forma de memoria
muebles = []

def agregar_mueble(tipo, material, precio, extra):
    #Agrega un nuevo mueble a la lista
    precio = float(precio)
    
    if tipo == "silla":
        mueble = Silla(material, precio, int(extra))  #extra->num_patas
    elif tipo == "mesa":
        mueble = Mesa(material, precio, extra)  #extra->forma
    elif tipo == "armario":
        mueble = Armario(material, precio, int(extra))  #extra->num_cajones
    else:
        print("Tipo de mueble no valido")
        return

    muebles.append(mueble)
    print(f"{tipo.capitalize()} agregado con éxito.")

def mostrar_muebles():
    #Mostre todos los muebles en la lista
    if not muebles:
        print("No hay muebles en el inventario.")
        return
    
    print("\nLista de Muebles:")
    for mueble in muebles:
        print(mueble)

def guardar_muebles():
    #Guarda la lista de muebles en un archivo JSON
    with open("muebles.json", "w") as file:
        json.dump([mueble.to_dict() for mueble in muebles], file, indent=4)
    print("Muebles guardados en 'muebles.json'.")

def cargar_muebles():
    #Carga muebles desde un archivo JSON
    global muebles
    try:
        with open("muebles.json", "r") as file:
            data = json.load(file)
            muebles = [Mueble.from_dict(item) for item in data]
        print("Muebles cargados desde 'muebles.json'.")
    except FileNotFoundError:
        print("No se encontro el archivo 'muebles.json'.")

