from mueble import Mueble

class Inventario:
    def __init__(self):
        self.muebles = [] #se crea lista para almacenar los muebles

    def agregar_mueble(self, mueble: Mueble): #se agrega el mueble al inventario
        self.muebles.append(mueble)

    def eliminar_mueble(self, mueble: Mueble): #Elimina un mueble del inventario si este existe
        if mueble in self.muebles:
            self.muebles.remove(mueble)
        else:
            print("El mueble no está en el inventario")

    def listar_muebles(self): #Muestra todos los muebles en el inventario
        if not self.muebles:
            print("El inventario está vacío.")
        else:
            for mueble in self.muebles:
                print(mueble)
    def buscar_por_material(self, material: str): #Busca muebles por material y los devuelve en una lista
        return [mueble for mueble in self.muebles if mueble._material.lower() == material.lower()]

    
