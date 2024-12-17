from vehiculos import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta
import csv

def primera_parte():
    print("##-Primera parte-##")

    print("Ingreso e impresión de instancias: \n")
    automoviles = []
    cantidad = int(input("¿Cuantos Vehiculos desea insertar?: "))
    for i in range(cantidad):
        print(f"Datos del automóvil {i+1}: ")
        marca_n = input("Inserte la marca del automóvil: ")
        modelo_n = input("Inserte el modelo: ")
        nro_ruedas_n = int(input("Inserte el número de ruedas:"))
        velocidad_n = int(input("Inserte la velocidad en km/h: "))
        cilindrada_n = int(input("Inserte el cilindraje en cc: "))
        # creamos la primera instancia
        automoviles.append(
            Automovil(marca_n, modelo_n, nro_ruedas_n, velocidad_n, cilindrada_n)
        )

    count = 1
    print("Imprimiendo por pantalla los Vehículos: \n")
    for auto in automoviles:
        print(f"Datos del automóvil {count}: {auto}.")
        count += 1

    print("\n************************\n")


def segunda_parte():
    print("##-Segunda Parte-##")
    # ingresamos las instancias solicitadas para cada medio de transporte
    print("Ingreso e impresión de instancias: \n")
    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
    # impresiones
    print(particular)
    print(carga)
    print(bicicleta)
    print(motocicleta)
    # Verificamos la relación que existe de la instancia motocicleta con las demás
    print("\nComprobación de instancias: \n")
    print(
        "Motocicleta es instancia con relación a Vehículo:",
        isinstance(motocicleta, Vehiculo),
    )
    print(
        "Motocicleta es instancia con relación a Automovil:",
        isinstance(motocicleta, Automovil),
    )
    print(
        "Motocicleta es instancia con relación a Vehículo particular:",
        isinstance(motocicleta, Particular),
    )
    print(
        "Motocicleta es instancia con relación a Vehículo de Carga:",
        isinstance(motocicleta, Carga),
    )
    print(
        "Motocicleta es instancia con relación a Bicicleta:",
        isinstance(motocicleta, Bicicleta),
    )
    print(
        "Motocicleta es instancia con relación a Motocicleta:",
        isinstance(motocicleta, Motocicleta),
    )

    print("\n**********************\n")


# En esta tercera parte el cliente quiere que se guarden los datos en un archivo con el nombre de vehiculos.csv,
def tercera_parte():
    print("##-Tercera parte-##")

    print("Ingreso y lectura de información de archivo: \n")
    print("Se están guardando los datos...")

    guardar_datos_csv()

    print("¡Los datos se guardaron satisfactoriamente!\n")
    print("\nLeyendo datos: ")

    leer_datos_csv()

    print("¡Datos leídos exitosamente!")

    print("\n***************************\n")


particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

vehiculos = [particular, carga, bicicleta, motocicleta]


def guardar_datos_csv():
    try:
        with open("vehiculo.csv", "w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(
                [
                    "tipo",
                    "marca",
                    "modelo",
                    "nro_ruedas",
                    "velocidad",
                    "cilindrada",
                    "nro_puestos",
                    "peso_carga",
                    "tipo_bicicleta",
                    "motor",
                    "cuadro",
                    "nro_radios",
                ]
            )
            for vehiculo in vehiculos:
                if isinstance(vehiculo, Motocicleta):
                    escritor.writerow(
                        [
                            vehiculo.tipo(),
                            vehiculo.marca,
                            vehiculo.modelo,
                            vehiculo.nro_ruedas,
                            "",
                            "",
                            "",
                            "",
                            vehiculo.tipo_bicicleta,
                            vehiculo.motor,
                            vehiculo.cuadro,
                            vehiculo.nro_radios,
                        ]
                    )
                elif isinstance(vehiculo, Bicicleta):
                    escritor.writerow(
                        [
                            vehiculo.tipo(),
                            vehiculo.marca,
                            vehiculo.modelo,
                            vehiculo.nro_ruedas,
                            "",
                            "",
                            "",
                            "",
                            vehiculo.tipo_bicicleta,
                            "",
                            "",
                            "",
                        ]
                    )

                elif isinstance(vehiculo, Carga):
                    escritor.writerow(
                        [
                            vehiculo.tipo(),
                            vehiculo.marca,
                            vehiculo.modelo,
                            vehiculo.nro_ruedas,
                            vehiculo.velocidad,
                            vehiculo.cilindrada,
                            "",
                            vehiculo.peso_carga,
                            "",
                            "",
                            "",
                            "",
                        ]
                    )

                elif isinstance(vehiculo, Particular):
                    escritor.writerow(
                        [
                            vehiculo.tipo(),
                            vehiculo.marca,
                            vehiculo.modelo,
                            vehiculo.nro_ruedas,
                            vehiculo.velocidad,
                            vehiculo.cilindrada,
                            vehiculo.nro_puestos,
                            "",
                            "",
                            "",
                            "",
                            "",
                        ]
                    )

                elif isinstance(vehiculo, Automovil):
                    escritor.writerow(
                        [
                            vehiculo.tipo(),
                            vehiculo.marca,
                            vehiculo.modelo,
                            vehiculo.nro_ruedas,
                            vehiculo.velocidad,
                            vehiculo.cilindrada,
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                        ]
                    )
    except Exception:
        print("Ocurrió un error inesperado")


def leer_datos_csv():
    automoviles = []
    particulares = []
    cargas = []
    bicicletas = []
    motocicletas = []
    with open("vehiculo.csv", "r") as archivo:
        try:
            lector = csv.DictReader(archivo)
            for fila in lector:
                tipo = fila["tipo"]
                if tipo == "Motocicleta":
                    vehiculo = Motocicleta(
                        fila["marca"],
                        fila["modelo"],
                        fila["nro_ruedas"],
                        fila["tipo_bicicleta"],
                        fila["motor"],
                        fila["cuadro"],
                        fila["nro_radios"],
                    )
                    motocicletas.append(vehiculo)
                elif tipo == "Bicicleta":
                    vehiculo = Bicicleta(
                        fila["marca"],
                        fila["modelo"],
                        fila["nro_ruedas"],
                        fila["tipo_bicicleta"],
                    )
                    bicicletas.append(vehiculo)
                elif tipo == "Carga":
                    vehiculo = Carga(
                        fila["marca"],
                        fila["modelo"],
                        fila["nro_ruedas"],
                        fila["velocidad"],
                        fila["cilindrada"],
                        fila["peso_carga"],
                    )
                    cargas.append(vehiculo)
                elif tipo == "Particular":
                    vehiculo = Particular(
                        fila["marca"],
                        fila["modelo"],
                        fila["nro_ruedas"],
                        fila["velocidad"],
                        fila["cilindrada"],
                        fila["nro_puestos"],
                    )
                    particulares.append(vehiculo)
                elif tipo == "Automovil":
                    vehiculo = Automovil(
                        fila["marca"],
                        fila["modelo"],
                        fila["nro_ruedas"],
                        fila["velocidad"],
                        fila["cilindrada"],
                    )
                    automoviles.append(vehiculo)

            print("\nListado de Automoviles:")
            imprimir_listado(automoviles)
            print("\nListado de Vehiculos Particulares:")
            imprimir_listado(particulares)
            print("\nListado de Vehiculos de Carga:")
            imprimir_listado(cargas)
            print("\nListado de Bicicletas:")
            imprimir_listado(bicicletas)
            print("\nListado de Motocicletas: ")
            imprimir_listado(motocicletas)

        except Exception as error:
            print("Ocurrió un error inesperado:", error)


def imprimir_listado(listado):
    for elemento in listado:
        if elemento is not None:  # Cambio realizado aquí
            print(elemento)


def iniciar_menu(funcionando):
    print("##### SISTEMA DE CONTROL DE VEHÍCULOS #####")
    print("")

    while funcionando:
        print("##   Por favor, seleccione una de las opciones disponibles  ##")
        print("1   .- Primera Parte...")
        print("2  .- Segunda Parte...")
        print("3  .- Tercera Parte...")
        print("4  .- Salir del Sistema...")
        opcion = input()

        match opcion:
            case "1":
                primera_parte()
            case "2":
                segunda_parte()
            case "3":
                tercera_parte()
            case "4":
                print("Saliendo del sistema...")
                funcionando = False
            case _:
                print("Opción no válida. Por favor, elija un número entre 1 y 4.")


# Función para iniciar el programa
iniciar_menu(True)
