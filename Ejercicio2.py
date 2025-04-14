#------------------------------------------------------------------------------
# Ejercicio 2.
# Escribir una función que tome un una cantidad m de valores que son ingresados
# por el usuario y, en la medida que lo ingresa, se muestra el factorial de ese
# número. El valor de m es ingresado inicialmente por el usuario.
#------------------------------------------------------------------------------

def main():
  m = int(input("Ingrese un numero: "))
  resultado = 1
  for i in range(1,m+1):
    resultado *= i
  print(resultado) 

if __name__ == '__main__':
  main()
