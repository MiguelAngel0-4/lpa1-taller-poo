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
        json.dump([Mueble.to_dict() for mueble in muebles], file, indent=4)
    print("Muebles guardados en 'muebles.json'.")

def cargar_muebles():
    #Carga muebles desde un archivo JSON
    global muebles
    try:
        with open("muebles.json", "r") as file:
            data = json.load(file)
            if not isinstance(data, list):  # Verifica que los datos sean una lista
                raise ValueError("El archivo JSON tiene un formato incorrecto.")
            
            muebles = [Mueble.from_dict(item) for item in data]
        print("Muebles cargados desde 'muebles.json'.")
    except FileNotFoundError:
        print("No se encontro el archivo 'muebles.json'.")
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Error al cargar muebles: {e}")

#configuracion argparse para la CLI
parser = argparse.ArgumentParser(description="Sistema de Gestion de Muebles")
subparsers = parser.add_subparsers(dest="comando")

#Comando para agregar muebles
parser_agregar = subparsers.add_parser("agregar", help="Agregar un mueble")
parser_agregar.add_argument("tipo", choices=["silla", "mesa", "armario"], help="Tipo de mueble")
parser_agregar.add_argument("material", help="Material del mueble")
parser_agregar.add_argument("precio", type=float, help="Precio del mueble")
parser_agregar.add_argument("extra", help="Número de patas (silla), forma (mesa) o número de cajones (armario)")

#comando para mostrar muebles
parser_mostrar = subparsers.add_parser("mostrar", help="Mostrar todos los muebles")

#Comando para guardar muebles en JSON
parser_guardar = subparsers.add_parser("guardar", help="Guardar muebles en un archivo JSON")

#Comando para cargar muebles desde JSON
parser_cargar = subparsers.add_parser("cargar", help="Cargar muebles desde un archivo JSON")

#Para Ejecutar la CLI
args = parser.parse_args()

if args.comando == "agregar":
    agregar_mueble(args.tipo, args.material, args.precio, args.extra)
elif args.comando == "mostrar":
    mostrar_muebles()
elif args.comando == "guardar":
    guardar_muebles()
elif args.comando == "cargar":
    cargar_muebles()
else:
    parser.print_help()

