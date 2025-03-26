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