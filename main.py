from lib import cuadrado

print("Proyecto figuras")

print(cuadrado.get_identificador())

lado = 4
print(f"El area de un {cuadrado.get_identificador()} de lado {lado} es: 
      {cuadrado.get_area(lado)} y el perímetro es {cuadrado.get_perimetro(lado)}")