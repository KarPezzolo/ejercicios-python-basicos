#Calculadora Básica

#Se quiere programar una calculadora que realice las operaciones:
#Sumar, Restar, Multiplicar y Dividir; además de una opción para Salir de la calculadora. 

def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")
    return int(input("Elige una operación:"))

def solicitud_num():
    primer_numero = int(input("Ingrese el primer número:"))
    segundo_numero = int(input("Ingrese el segundo número:"))
    return primer_numero, segundo_numero

def operacion(op_usuario, primer_numero, segundo_numero):
    if op_usuario == 1:
        resultado = primer_numero + segundo_numero
        print(f"El resultado de {primer_numero} + {segundo_numero} es: {resultado}")
    elif op_usuario == 2:
        resultado = primer_numero - segundo_numero
        print(f"El resultado de {primer_numero} - {segundo_numero} es: {resultado}")
    elif op_usuario == 3:
        resultado = primer_numero * segundo_numero
        print(f"El resultado de {primer_numero} * {segundo_numero} es: {resultado}")
    elif op_usuario == 4:
        if segundo_numero == 0:
            print("Error: División por cero")
        else:
            resultado = primer_numero / segundo_numero
            print(f"El resultado de {primer_numero} / {segundo_numero} es: {resultado}")
    else:
        print("Ingrese una opción válida.")

while True:
    opcion = menu()
    if opcion == 0:
        break
    num1, num2 = solicitud_num()
    operacion(opcion,num1,num2)
