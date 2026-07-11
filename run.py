talleres = ["Pintura", "Danza Moderna", "Teatro", "Guitarra"]
cupos = [12, 15, 8, 10]
inscripciones = []


def obtener_nombre(etiqueta):
    valor = input("Ingrese su " + etiqueta + ": ").strip()
    if valor == "":
        print("El campo no puede estar vacio. Intente de nuevo.")
        return obtener_nombre(etiqueta)
    return valor


def mostrar_talleres():
    print("\n--- Talleres disponibles ---")
    for i in range(len(talleres)):
        print(str(i + 1) + ". " + talleres[i] + " - cupos disponibles: " + str(cupos[i]))


def elegir_taller():
    opcion = input("Elija el numero del taller: ").strip()
    if not opcion.isdigit():
        print("Debe ingresar un numero.")
        return elegir_taller()
    indice = int(opcion) - 1
    if indice < 0 or indice >= len(talleres):
        print("Ese taller no existe en la lista.")
        return elegir_taller()
    return indice


def inscribir():
    nombre = obtener_nombre("nombre")
    apellido = obtener_nombre("apellido")

    mostrar_talleres()
    indice = elegir_taller()

    if cupos[indice] > 0:
        cupos[indice] = cupos[indice] - 1
        inscripciones.append({
            "nombre": nombre,
            "apellido": apellido,
            "taller": talleres[indice],
        })
        print("\nInscripcion confirmada: " + nombre + " " + apellido +
              " en " + talleres[indice] + ".")
    else:
        print("\nLo sentimos, el taller " + talleres[indice] + " ya no tiene cupos.")


def ver_inscripciones():
    print("\n--- Inscripciones registradas ---")
    if len(inscripciones) == 0:
        print("Todavia no hay inscripciones.")
        return
    for i in range(len(inscripciones)):
        registro = inscripciones[i]
        print(str(i + 1) + ". " + registro["nombre"] + " " + registro["apellido"] +
              " - " + registro["taller"])


def menu():
    opcion = ""
    while opcion != "3":
        print("\n===== Casa de la Juventud =====")
        print("1. Inscribirse en un taller")
        print("2. Ver inscripciones")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            inscribir()
        elif opcion == "2":
            ver_inscripciones()
        elif opcion == "3":
            print("Gracias por usar el sistema. Hasta pronto.")
        else:
            print("Opcion invalida. Elija 1, 2 o 3.")


menu()
