import argparse
import json
from mueble import Silla, Mesa, Armario, Mueble

# Lista de muebles en memoria
muebles = []

def cargar_muebles():
    global muebles
    try:
        with open("muebles.json", "r") as file:
            data = json.load(file)
            print("Contenido de muebles.json:", data)  #Depuración
            muebles = [Mueble.from_dict(item) for item in data]
        print("Muebles cargados desde 'muebles.json'.")
    except FileNotFoundError:
        print("No se encontró el archivo 'muebles.json'.")
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON.")

def agregar_mueble(tipo, material, precio, extra):
    #Agrega un nuevo mueble a la lista en memoria
    precio = float(precio)
    
    if tipo == "silla":
        mueble = Silla(material, precio, int(extra))  # extra -> num_patas
    elif tipo == "mesa":
        mueble = Mesa(material, precio, extra)  # extra -> forma
    elif tipo == "armario":
        mueble = Armario(material, precio, int(extra))  # extra -> num_cajones
    else:
        print("Tipo de mueble no válido.")
        return

    muebles.append(mueble)
    print(f"{tipo.capitalize()} agregado con éxito.")

def mostrar_muebles():
    """Muestra todos los muebles en memoria."""
    if not muebles:
        print("No hay muebles en el inventario.")
        return
    
    print("\nLista de Muebles:")
    for mueble in muebles:
        print(mueble)

def guardar_muebles():
    """Guarda la lista de muebles en un archivo JSON."""
    with open("muebles.json", "w") as file:
        json.dump([mueble.to_dict() for mueble in muebles], file, indent=4)
    print("Muebles guardados en 'muebles.json'.")

# Configuración de argparse para la CLI
parser = argparse.ArgumentParser(description="Sistema de Gestión de Muebles")
subparsers = parser.add_subparsers(dest="comando")

# Comando para cargar muebles desde JSON
parser_cargar = subparsers.add_parser("cargar", help="Cargar muebles desde un archivo JSON")

# Comando para agregar muebles
parser_agregar = subparsers.add_parser("agregar", help="Agregar un mueble")
parser_agregar.add_argument("tipo", choices=["silla", "mesa", "armario"], help="Tipo de mueble")
parser_agregar.add_argument("material", help="Material del mueble")
parser_agregar.add_argument("precio", help="Precio del mueble")
parser_agregar.add_argument("extra", help="Número de patas (silla), forma (mesa) o número de cajones (armario)")

# Comando para mostrar muebles
parser_mostrar = subparsers.add_parser("mostrar", help="Mostrar todos los muebles")

# Comando para guardar muebles en JSON
parser_guardar = subparsers.add_parser("guardar", help="Guardar muebles en un archivo JSON")

# Ejecutar la CLI
args = parser.parse_args()

if args.comando == "cargar":
    cargar_muebles()
elif args.comando == "agregar":
    agregar_mueble(args.tipo, args.material, args.precio, args.extra)
elif args.comando == "mostrar":
    mostrar_muebles()
elif args.comando == "guardar":
    guardar_muebles()
else:
    parser.print_help()