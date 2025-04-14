#----------------------------------------------------------------------------
# Ejercicio 3. Usando la función, dada como ejemplo en la presentación de
# La Receta en Python, para convertir una temperatura en Fahrenheit a Celsius
# se pide que genere una tabla de conversión de temperaturas, desde 0◦F hasta
# 120◦F, de 10 en 10.
#----------------------------------------------------------------------------

def far_cel(temp_f):
  '''
  Representamos temperaturas mediante números float
  temperatura: float
  far_cel: float -> float
  El parámetro representa una temperatura en Fahrenheit y retorna su
  equivalente en Celsius.
  Ejemplos:
  far_cel(32) = 0
  far_cel(212) = 100
  far_cel( -40) = -40
  far_cel(90) = 32.22 '''
  temp_c = (temp_f -32)* 5/9
  return temp_c

def main():
  resultado = 0
  for i in range (0,121,10):
    resultado = far_cel(i)
    print(resultado)

if __name__ == '__main__':
  main()
