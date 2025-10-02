def pedir_int_rango(mensaje, limite_inf = float("inf"), limite_sup = float("inf")):
    """
    Pide un numero entero y valida que este dentro dentro del rango solicitado\n
    mensaje = mensaje a mostrar en input\n
    limite_inf = limite inferior del rango\n
    limite_sup = limite superior del rango\n
    retorna int
    """
    while True:
        n = input(mensaje)
        try: int(n)
        except: 
            print("ERROR: Ingresa un numero entero")
            continue
        n = int(n)
        if not limite_inf<=n<=limite_sup:
            print(f"ERROR: El numero ingresado no esta entre {limite_inf} y {limite_sup}")
            continue
        return n

def imprimir_tabla(lista, titulo):
    print(f"-------------{titulo}-------------")
    for i in range(0,len(lista[0])):
        print(f"Codigo: {lista[0][i]} | Nombre: {lista[1][i]} | Cantidad: {lista[2][i]} ")

def pedir_codigo_golosina(): 
    return pedir_int_rango("Ingresa el codigo de la golosina requerida: ", 1, golosinas[0][-1])-1 #-1 pq la golosina de codigo 4 corresponde al indice 3 por ej.
     
def restar_golosina(codigo_elegido):
    salir = False
    while not salir:
        if golosinas[2][codigo_elegido] == 0:
            print (f"Lo sentimos, la golosina {golosinas[1][codigo_elegido]} no se encuentra disponible, ingresa otro codigo de golosina o ingresa salir si no desea otra. ")
            codigo_elegido = input()
            if codigo_elegido.lower() == "salir": 
                salir = True
                continue
            else: 
                try: #try para evitar errores si no ingreso un entero
                    codigo_elegido = int(codigo_elegido)-1
                    if codigo_elegido not in golosinas[0]: #validar si es un codigo valido
                        print ("El codigo ingresado no existe")
                        codigo_elegido = pedir_codigo_golosina
                except: 
                        print ("Ingresa un codigo numerico")
                        codigo_elegido = pedir_codigo_golosina()
        else: 
            golosinas[2][codigo_elegido] -= 1
            salir = True

def registrar_pedido(codigo_elegido):
    if codigo_elegido in golosinas_pedidas[0]:
        golosinas_pedidas[2][codigo_elegido] += 1
    else:
        golosinas_pedidas[0].append(codigo_elegido+1)
        golosinas_pedidas[1].append(golosinas[1][codigo_elegido])
        golosinas_pedidas[2].append(1)

def pedir_golosina():
    legajo_ingresado = input("Ingresa tu legajo: ")
    if legajo_ingresado not in empleados.keys(): 
        print("No eres un empleado de esta empresa.")
        return

    codigo_elegido = pedir_codigo_golosina()
    restar_golosina(codigo_elegido)
    registrar_pedido(codigo_elegido)
    print(f"Retiro de {golosinas[1][codigo_elegido]} exitoso")
    input("Enter para continuar")

def mostrar_golosinas():
    imprimir_tabla(golosinas, "Stock Golosinas")
    input("Enter para volver")

def rellenar_golosinas():
    contraseña_ingresada_1 = input("Ingresa la primer contraseña: ")
    if contraseña_ingresada_1 != clave_tecnico[0]:
        print("No tiene permiso para ejecutar la función de recarga.")
        return
    contraseña_ingresada_2 = input("Ingresa la segunda contraseña: ")
    if contraseña_ingresada_2 != clave_tecnico[1]:
        print("No tiene permiso para ejecutar la función de recarga.")
        return
    contraseña_ingresada_3 = input("Ingresa la tercer contraseña: ")
    if contraseña_ingresada_3 != clave_tecnico[2]:
        print("No tiene permiso para ejecutar la función de recarga.")
        return

    cogido_ingresado = pedir_codigo_golosina()
    cantidad_golosinas = pedir_int_rango("Ingresa la cantidad a rellenar: ", 1)
    golosinas[2][cogido_ingresado] += cantidad_golosinas
    print("Reposicion exitosa")
    input("Enter para continuar")

def apagar_maquina():
    imprimir_tabla(golosinas_pedidas, "Golosinas Pedidas")
    total_pedidas = sum(golosinas_pedidas[2])
    print(f"Se pidieron {total_pedidas} golosinas en total.")

def menu():
    seguir = True
    opciones = {"a":pedir_golosina, "b":mostrar_golosinas, "c":rellenar_golosinas, "d":apagar_maquina}
    while seguir:
        print("------------MAQUINA EXPENDEDORA------------")
        opcion_elegida = input("Ingresa una opcion\na- Pedir golosina\nb- Mostrar stock\nc- Rellenar maquina\nd- Apagar maquina\n").lower()
        while opcion_elegida not in (opciones.keys()):
            print("ERROR. Opcion invalida. Intentalo de nuevo")
            opcion_elegida = input("Ingresa una opcion\na- Pedir golosina\nb- Mostrar stock\nc- Rellenar maquina\nd- Apagar maquina\n")

        opciones[opcion_elegida]()
        if opcion_elegida == "d": seguir = False

#main
nombres_golosinas = ["KitKat", "Chicles", "Caramelos de Menta", "Huevo Kinder", "Chetoos", "Twix", "M&M'S", "Papas Lays", "Milkybar", "Alfajor Tofi", "Lata Coca", "Chitos"]
cantidad_golosinas_inicial = [20, 50, 50, 10, 10, 10, 10, 2, 10, 11, 15, 20, 10]
golosinas = [range(1,13),nombres_golosinas,cantidad_golosinas_inicial]

empleados = {"1100": "José Alonso",
    "1200": "Federico Pacheco",
    "1300": "Nelson Pereira",
    "1400": "Osvaldo Tejada",
    "1500": "Gastón Garcia"}

clave_tecnico = ("admin", "CCCDDD", "2020")

golosinas_pedidas = [[],[],[]]

menu()