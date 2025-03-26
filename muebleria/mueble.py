import json #importacion de json para convertir objeto a diccionario y crear objeto desde diccionario
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

    def to_dict(self): #Convierte el objeto en un diccionario para JSON
        return {
            "tipo": self.__class__.__name__,
            "material": self._material,
            "precio": self._precio
        }    
    @staticmethod
    def from_dict(data): #deserialización
        tipo = data["tipo"]
        if tipo == "Silla":
            return Silla(data["material"], data["precio"], data["num_patas"])
        elif tipo == "Mesa":
            return Mesa(data["material"], data["precio"], data["forma"])
        elif tipo == "Armario":
            return Armario(data["material"], data["precio"], data["num_cajones"])
        else:
            raise ValueError(f"Tipo de mueble desconocido: {tipo}")

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
    def to_dict(self): #Extencion de la serialización para incluir atributo
        data = super().to_dict()
        data["num_patas"] = self.num_patas
        return data
    
class Mesa(Mueble):
    def __init__(self, material: str, precio: float, forma: str):
        super().__init__(material, precio)
        self.forma=forma

    def calcu_preciof(self) -> float:
        #Precio con 15% de margen
        return self._precio * 1.15
    def to_dict(self):
        data = super().to_dict()
        data["forma"] = self.forma
        return data
    
class Armario(Mueble):
    def __init__(self, material: str, precio: float, num_cajones: int):
        super().__init__(material, precio)
        self.num_cajones=num_cajones
    
    def calcu_preciof(self)-> float:
        #Precio con 20% de margen
        return self._precio * 1.2
    def to_dict(self):
        data = super().to_dict()
        data["num_cajones"] = self.num_cajones
        return data
