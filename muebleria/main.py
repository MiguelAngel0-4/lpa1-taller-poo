# ejecutar el programa y probar las clases
#importamos las subclases de mueble.py
from mueble import Silla, Mesa, Armario
from rich.console import Console
from rich.table import Table

#creacion consola formateada
Console = Console()

#instanciar muebles
silla = Silla("Madera", 100, 4)
mesa = Mesa("Vidrio", 200, "Redonda")
armario = Armario("Metal", 500, 3)

#creacion tabla con titulo
table = Table(title="Inventario de Muebles")

#definicion de columnas
table.add_column("Tipo", justify="left", style="cyan", no_wrap=True)
table.add_column("Material", style="magenta")
table.add_column("Precio Base", justify="right", style="blue")
table.add_column("Precio Final", justify="right", style="red")

#datos de cada mueble
table.add_row("Silla", silla._material, f"${silla._precio:.2f}", f"${silla.calcu_preciof():.2f}")
table.add_row("Mesa", mesa._material, f"${mesa._precio:.2f}", f"${mesa.calcu_preciof():.2f}")
table.add_row("Armario", armario._material, f"${armario._precio:.2f}", f"${armario.calcu_preciof():.2f}")

Console.print(table)

from inventario import Inventario #importancion de inventario

inventario = Inventario()
inventario.agregar_mueble(silla)
inventario.agregar_mueble(mesa)
inventario.agregar_mueble(armario)

#Mostra los muebles del inventario
print("\n Inventario de la muebleria:")
inventario.listar_muebles()

#Busqueda de muebles por material
muebles_madera = inventario.buscar_por_material("Madera")
print("\n Muebles de madera encontrados:")
for mueble in muebles_madera:
    print(mueble)
