def main():
    pregunta = input("desea ingresar mas datos? SI|NO")
    while (pregunta == "SI") or (pregunta == "sI") or (pregunta == "Si") or (pregunta == "si"):
        numero = int(input("ingrese un numero entero: "))
        respuesta = clasifica_num(numero)
        print("la calificacion de", num,"es",respuesta)
        pregunta = input("desea ingresar mas datos? SI|NO")


main()
