
import pandas as pd
from figuras import rectangulo, triangulo, circulo

df = pd.read_csv("figuras.csv")
print("El archivo ha sido leido")


for index, row in df.iterrows():
	print(f"Fila {index}: FIGURA={row['FIGURA']}, MEDIDA1={row['MEDIDA1']}, MEDIDA2={row['MEDIDA2']}")

for index, row in df.iterrows():
	figura = row['FIGURA']
	m1 = row['MEDIDA1']
	m2 = row['MEDIDA2']

if figura == 'r':  # rectángulo
	area, perimetro = rectangulo(m1, m2)
	print(f"Fila {index}: Rectángulo base={m1}, altura={m2} -> Área={area:.2f}, Perímetro={perimetro:.2f}")

elif figura == 't':  # triángulo
	area, perimetro = triangulo(m1, m2)
	print(f"Fila {index}: Triángulo base={m1}, altura={m2} -> Área={area:.2f}, Perímetro={perimetro:.2f}")

elif figura == 'c':  # círculo
	area, perimetro = circulo(m1)  # solo usa MEDIDA1 como radio
	print(f"Fila {index}: Círculo radio={m1} -> Área={area:.2f}, Perímetro={perimetro:.2f}")



