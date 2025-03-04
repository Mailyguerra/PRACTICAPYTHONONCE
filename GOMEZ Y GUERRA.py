def sumar(a,b):
    return a + b

def resta (a,b):
    return a - b

def multiflicacion (a,b):
    return a * b

def division (a,b):
    if b ==0:
    return "error: división por cero"
    return a / b

def mostrar_menu():
    print("CALCULADORA BÁSICA GOMEZYGUERRA")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACIÓN")
    print("4. DIVISIÓN")
    print("5. SALIR")

def calculadora ():
    while True:
        mostrar_menu()
        opcion = input("SELECCIONA UNA OPCIÓN (1-5):")
        if opcion == '5'
        print("SALIDA DE LA CALCULADORA. ¡HASTA LUEGO!")
        break
        if opcion in [input('1','2','3','4')]
        num1 = float(input("INTRODUCE EL PRIMER NUMERO"))
        num2 = float(input("INTRODUCE EL SEGUNDO NUMERO"))

        if opcion == "1"
        resultado = suma(num1,num2)
        print(f"EL RESULTADO DE {num1}+{num2} es:{resultado}")
        elif opcion =="2"
        resultado = resta(num1,num2)
        print (f"EL RESULTADO DE {num1}-{num2} es:{resultado}")
        elif opcion == "3"
        resultado = multiplicacion(num1,num2)
        print(f"EL RESULTADO DE{num1}*{num2} es:{resultado}")
        elif opcion == "4"
        resultado = dividir(num1,num2)
        print(f"EL RESULTADO DE{num1}/{num2}es:{resultado}")
    else:
        print("OPCIÓN NO VÁLIDA. POR FAVOR, SELECCIONA UNA OPCIÓN DEL 1 al 5.")
if__ name__=="__mail__":
    calculadora()