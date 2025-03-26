import json  # Importación de JSON para serializar y deserializar
from abc import ABC, abstractmethod

class Mueble(ABC):
    def __init__(self, material: str, precio: float):
        self._material = material
        self._precio = precio

    # Método abstracto para calcular el precio final
    @abstractmethod
    def calcu_preciof(self) -> float:
        pass

    # Aplica un descuento al precio
    def aplicar_descuento(self, porcentaje: float):
        descuento = self._precio * (porcentaje / 100)
        self._precio -= descuento

    # Convierte el objeto en un diccionario para JSON
    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "material": self._material,
            "precio": self._precio
        }

    # Deserialización desde un diccionario
    @staticmethod
    def from_dict(data):
        tipo = data["tipo"]
        if tipo == "Silla":
            return Silla.from_dict(data)
        elif tipo == "Mesa":
            return Mesa.from_dict(data)
        elif tipo == "Armario":
            return Armario.from_dict(data)
        else:
            raise ValueError(f"Tipo de mueble desconocido: {tipo}")

    def __str__(self):
        return f"""--- {self.__class__.__name__} ---
Material: {self._material}
Precio: {self._precio:.2f}"""


class Silla(Mueble):
    def __init__(self, material: str, precio: float, num_patas: int):
        super().__init__(material, precio)
        self.num_patas = num_patas

    def calcu_preciof(self) -> float:
        return self._precio * 1.1  

    # Serialización con atributo extra
    def to_dict(self):
        data = super().to_dict()
        data["num_patas"] = self.num_patas
        return data

    @staticmethod
    def from_dict(data):
        return Silla(data["material"], data["precio"], data["num_patas"])

    def __str__(self):
        return super().__str__() + f"\nNúmero de Patas: {self.num_patas}"


class Mesa(Mueble):
    def __init__(self, material: str, precio: float, forma: str):
        super().__init__(material, precio)
        self.forma = forma

    def calcu_preciof(self) -> float:
        return self._precio * 1.15

    def to_dict(self):
        data = super().to_dict()
        data["forma"] = self.forma
        return data

    @staticmethod
    def from_dict(data):
        return Mesa(data["material"], data["precio"], data["forma"])

    def __str__(self):
        return super().__str__() + f"\nForma: {self.forma}"


class Armario(Mueble):
    def __init__(self, material: str, precio: float, num_cajones: int):
        super().__init__(material, precio)
        self.num_cajones = num_cajones

    def calcu_preciof(self) -> float:
        return self._precio * 1.2

    def to_dict(self):
        data = super().to_dict()
        data["num_cajones"] = self.num_cajones
        return data

    @staticmethod
    def from_dict(data):
        return Armario(data["material"], data["precio"], data["num_cajones"])

    def __str__(self):
        return super().__str__() + f"\nNúmero de cajones: {self.num_cajones}"
