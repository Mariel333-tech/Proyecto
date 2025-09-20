import math
def rectangulo(base , altura):
	area= base * altura
	perimetro= 2 * (base + altura)
	return area, perimetro
def triangulo(base, altura):
    area = (base * altura) / 2
    lado = math.sqrt((base / 2)**2 + altura**2)
    perimetro = base + 2 * lado
    return area, perimetro
def circulo(radio):
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    return area, perimetro


