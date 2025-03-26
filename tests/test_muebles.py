# pruebas unitarias utilizando pytest
#importamos las subclases y pytest
import pytest
from muebleria.mueble import Silla, Mesa, Armario

#tests
def test_silla_precio():
    silla = Silla("Madera", 100.0, 4)  #Creamos una silla con precio 100.0
    assert round(silla.calcu_preciof(), 2) == 110.0  #Verificacion

def test_mesa_precio():
    mesa = Mesa("Metal", 200.0, "Redonda")  #mesa con precio 200.0
    assert round(mesa.calcu_preciof(), 2) == 230.0  #precio final debería ser 230.0

def test_armario_precio():
    armario = Armario("Plástico", 300.0, 5)  #armario con precio 300.0
    assert armario.calcu_preciof() == 360.0  #precio final debería ser 360.0

def test_precio_cero():
    silla = Silla("Madera", 0.0, 4)  #Silla con precio 0
    assert silla.calcu_preciof() == 0.0  #recio final también debería ser 0.0

def test_descuento_mayor():
    armario = Armario("Vidrio", 50.0, 3)  #armario con precio 50.0
    armario.aplicar_descuento(200)  #200% de descuento
    assert armario._precio == -50.0  #precio debería quedar en -50.0

def test_precio_negativo():
    with pytest.raises(ValueError):  #lanza un error
        silla = Silla("Plástico", -50.0, 4) #precio no deberia ser negativo

def test_descuento_100():
    mesa = Mesa("Madera", 500.0, "Cuadrada")
    mesa.aplicar_descuento(100)  #Descuento del 100%
    assert mesa._precio == 0.0  #Debe dar cero 0