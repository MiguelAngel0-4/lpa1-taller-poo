from abc import ABC, abstractmethod

class Mueble(ABC):
    def __init__(self, material: str, precio: float):
        self._material = material
        self._precio = precio

#Metodo abstracto para calcular el precio final
    @abstractmethod
    def calcu_preciof(self) -> float:
        pass
#Aplica un descuento al precio
    def aplicar_descuento(self, porcentaje: float):
        
        descuento = self._precio * (porcentaje / 100)
        self._precio -= descuento
    def __str__(self):
        return f"""--- {self.__class__.__name__} ---
material {self._material}
precio {self._precio}"""
    
class Silla(Mueble):
    def __init__(self, material: str, precio: float, num_patas: int):
        #Llama al constructor de Mueble
        super().__init__(material, precio)
        # Nuevo atributo de Silla
        self.num_patas= num_patas

    def calcu_preciof(self) -> float:
        #Precio con 10% de margen
        return self._precio * 1.1  
    def __str__(self):
        return super().__str__() + f"\nNumero de Patas: {self.num_patas}"
    
class Mesa(Mueble):
    def __init__(self, material: str, precio: float, forma: str):
        super().__init__(material, precio)
        self.forma=forma

    def calcu_preciof(self) -> float:
        #Precio con 15% de margen
        return self._precio * 1.15
    def __str__(self):
        return super().__str__() + f"\nForma: {self.forma}"
    
