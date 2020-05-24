import requests
import json

exit = False

def get_rooms():
    URL = "http://localhost:8080/rooms"
    PARAMS = {}
    
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()

    if str(data) == "[]":
        print("> No hay habitaciones.\n")
    else:
        for room in data:
                print("Numero de habitacion (ID): " + str(room["id"]))
                print(" _____________________________________________\n")
                print(" | Numero de plazas: " + str(room["numPlazas"]))
                print(" | Numero de minibares: " + str(room["miniBar"]))
                print(" | Numero de armarios: " + str(room["armario"]))
                print(" | Numero de televisiones: " + str(room["television"]))
                print(" | Numero de escritorios: " + str(room["escritorio"]))
                print(" | Numero de cajas fuertes: " + str(room["cajaFuerte"]))
                print(" | Numero de aires acondicionados: " + str(room["aireAcondicionado"]))

                if room["ocupada"] == True:
                    print(" | Disponibilidad: Ocupada\n")
                else:
                    print(" | Disponibilidad: Desocupada\n")

                print("\n")
    

def get_room():
    id = input("Introduce la ID de la habitacion: ")
    URL = "http://localhost:8080/rooms/" + str(id)
    PARAMS = {}
    
    r = requests.get(url = URL, params = PARAMS)
    if r.text == "ERROR ID":
        print("\n>>> ERROR: No existe la habitacion.\n")
    else:
        room = r.json()

        print("\nNumero de habitacion (ID): " + str(room["id"]))
        print(" _____________________________________________\n")
        print(" | Numero de plazas: " + str(room["numPlazas"]))
        print(" | Numero de minibares: " + str(room["miniBar"]))
        print(" | Numero de armarios: " + str(room["armario"]))
        print(" | Numero de televisiones: " + str(room["television"]))
        print(" | Numero de escritorios: " + str(room["escritorio"]))
        print(" | Numero de cajas fuertes: " + str(room["cajaFuerte"]))
        print(" | Numero de aires acondicionados: " + str(room["aireAcondicionado"]))

        if room["ocupada"] == True:
            print(" | Disponibilidad: Ocupada\n")
        else:
            print(" | Disponibilidad: Desocupada\n")

def get_room_by_estado():
    estado = 0
    while estado <= 0 or estado > 2:
        print("1. Habitaciones ocupadas\n2. Habitaciones desocupadas\n")
        estado = input("Escoge la operacion: ")
    if(estado == 1):
        estado = "ocupada"
    else:
        estado = "desocupada"
    
    URL = "http://localhost:8080/habitaciones_disponibles/" + estado
    PARAMS = {}
    
    r = requests.get(url = URL, params = PARAMS)
    if r.text == "[]":
        print("\n> No hay habitaciones con estado " + estado + ".\n")
    else:
        data = r.json()
        for room in data:
            print("\nNumero de habitacion (ID): " + str(room["id"]))
            print(" _____________________________________________\n")
            print(" | Numero de plazas: " + str(room["numPlazas"]))
            print(" | Numero de minibares: " + str(room["miniBar"]))
            print(" | Numero de armarios: " + str(room["armario"]))
            print(" | Numero de televisiones: " + str(room["television"]))
            print(" | Numero de escritorios: " + str(room["escritorio"]))
            print(" | Numero de cajas fuertes: " + str(room["cajaFuerte"]))
            print(" | Numero de aires acondicionados: " + str(room["aireAcondicionado"]))
            if room["ocupada"] == True:
                print(" | Disponibilidad: Ocupada\n")
            else:
                print(" | Disponibilidad: Desocupada\n")

def del_room():
    id = input("Introduce la ID de la habitacion: ")
    URL = "http://localhost:8080/rooms/" + str(id)
    
    r = requests.delete(url = URL)
    if r.text == "ERROR ID":
        print("\n>>> ERROR: No existe la habitacion\n")
    else:
        room = r.json()
        print("\nHabitacion borrada con exito: ")

        print("\nNumero de habitacion (ID): " + str(room["id"]))
        print(" _____________________________________________\n")
        print(" | Numero de plazas: " + str(room["numPlazas"]))
        print(" | Numero de minibares: " + str(room["miniBar"]))
        print(" | Numero de armarios: " + str(room["armario"]))
        print(" | Numero de televisiones: " + str(room["television"]))
        print(" | Numero de escritorios: " + str(room["escritorio"]))
        print(" | Numero de cajas fuertes: " + str(room["cajaFuerte"]))
        print(" | Numero de aires acondicionados: " + str(room["aireAcondicionado"]))
        if room["ocupada"] == True:
            print(" | Disponibilidad: Ocupada\n")
        else:
            print(" | Disponibilidad: Desocupada\n")

def update_room():
    id = input("Introduce la ID de la habitacion: ")
    URL = "http://localhost:8080/rooms/" + str(id)
    PARAMS = {}

    r = requests.put(url = URL, json = PARAMS)

    if r.text == "ERROR ID":
        print("\n>>> ERROR: No existe la habitacion.\n")
    else:
        op = 0
        numPlazas = None
        miniBar = None
        armario = None
        television = None
        escritorio = None
        cajaFuerte = None
        aireAcondicionado = None
        ocupada = None

        while op != 9:
            print("\nIntroduce el numero del parametro que quieras modificar.\n\n    1. Numero de plazas\n    2. Numero de minibares\n    3. Numero de armarios\n    4. Numero de televisiones\n    5. Numero de escritorios\n    6. Numero de cajas fuertes\n    7. Numero de aires acondicionados\n    8. Disponibilidad\n    9. Terminar\n")
            op = input("\nIntroduce el numero: ")
            if op == 1:
                numPlazas = input("\nIntroduce Numero de plazas: ")
            elif op == 2:
                miniBar = input("\nIntroduce Numero de minibares: ")
            elif op == 3:
                armario = input("\nIntroduce Numero de armarios: ")
            elif op == 4:
                television = input("\nIntroduce Numero de televisiones: ")
            elif op == 5:
                escritorio = input("\nIntroduce Numero de escritorios: ")
            elif op == 6:
                cajaFuerte = input("\nIntroduce Numero de cajas fuertes: ") 
            elif op == 7:
                aireAcondicionado = input("\nIntroduce Numero de aires acondicionados: ")
            elif op == 8:
                ocupada = input("\n0. Desocupada\n1. Ocupada\n\nIntroduce la disponibilidad: ")
            
        PARAMS = {"numPlazas": numPlazas, "miniBar": miniBar, "armario": armario, "television": television, "escritorio": escritorio, "cajaFuerte": cajaFuerte, "aireAcondicionado": aireAcondicionado, "ocupada": ocupada}
        r = requests.put(url = URL, json = PARAMS)
        data = r.json()

        for i in data:
            if (str(i)[0] == 'E'):
                print("\n" + i)
            else:
                print("\nNumero de habitacion (ID): " + str(i["id"]))
                print(" _____________________________________________\n")
                print(" | Numero de plazas: " + str(i["numPlazas"]))
                print(" | Numero de minibares: " + str(i["miniBar"]))
                print(" | Numero de armarios: " + str(i["armario"]))
                print(" | Numero de televisiones: " + str(i["television"]))
                print(" | Numero de escritorios: " + str(i["escritorio"]))
                print(" | Numero de cajas fuertes: " + str(i["cajaFuerte"]))
                print(" | Numero de aires acondicionados: " + str(i["aireAcondicionado"]))

                if i["ocupada"] == True:
                    print(" | Disponibilidad: Ocupada\n")
                else:
                    print(" | Disponibilidad: Desocupada\n")


def create_room():
    URL = "http://localhost:8080/rooms"

    op = 0
    numPlazas = None
    miniBar = None
    armario = None
    television = None
    escritorio = None
    cajaFuerte = None
    aireAcondicionado = None

    while op != 8:
        print("Introduce el numero del parametro que quieras modificar.\nEn el caso de que un parametro no sea modificado por el usuario, se le asignara un valor por defecto.\n\n    1. Numero de plazas\n    2. Numero de minibares\n    3. Numero de armarios\n    4. Numero de televisiones\n    5. Numero de escritorios\n    6. Numero de cajas fuertes\n    7. Numero de aires acondicionados\n    8. Terminar\n")
        op = input("\nIntroduce el parametro: ")
        if op == 1:
            numPlazas = input("\nIntroduce Numero de plazas: ")
        elif op == 2:
            miniBar = input("\nIntroduce Numero de minibares: ")
        elif op == 3:
            armario = input("\nIntroduce Numero de armarios: ")
        elif op == 4:
            television = input("\nIntroduce Numero de televisiones: ")
        elif op == 5:
            escritorio = input("\nIntroduce Numero de escritorios: ")
        elif op == 6:
            cajaFuerte = input("\nIntroduce Numero de cajas fuertes: ") 
        elif op == 7:
            aireAcondicionado = input("\nIntroduce Numero de aires acondicionados: ")
        
    PARAMS = {"numPlazas": numPlazas, "miniBar": miniBar, "armario": armario, "television": television, "escritorio": escritorio, "cajaFuerte": cajaFuerte, "aireAcondicionado": aireAcondicionado}
    r = requests.post(url = URL, json = PARAMS)
    data = r.json()

    for i in data:
        if (str(i)[0] == 'E'):
            print("\n" + i)
        else:
            print("\nNumero de habitacion (ID): " + str(i["id"]))
            print(" _____________________________________________\n")
            print(" | Numero de plazas: " + str(i["numPlazas"]))
            print(" | Numero de minibares: " + str(i["miniBar"]))
            print(" | Numero de armarios: " + str(i["armario"]))
            print(" | Numero de televisiones: " + str(i["television"]))
            print(" | Numero de escritorios: " + str(i["escritorio"]))
            print(" | Numero de cajas fuertes: " + str(i["cajaFuerte"]))
            print(" | Numero de aires acondicionados: " + str(i["aireAcondicionado"]) + "\n")



print("\n      ####    Bienvenido al Hotel COVID-19    ####\n")

while not exit:
    print("__________________________ MENU __________________________")
    print("\nElige que operacion desea realizar: \n\n   1. Dar de alta una nueva habitacion.\n   2. Modificar los datos de una habitacion.\n   3. Consultar la lista completa de habitaciones.\n   4. Consultar una habitacion mediante un identificador.\n   5. Consultar lista de habitaciones ocupadas o desocupadas.\n   6. Eliminar una habitacion.\n   7. Salir.\n")

    opcion = input("Introduce una de las opciones: ")
    print("\n")
 
    if opcion == 1:
        create_room()
    elif opcion == 2:
        update_room()
    elif opcion == 3:
        get_rooms()
    elif opcion == 4:
        get_room()
    elif opcion == 5:
        get_room_by_estado()
    elif opcion == 6:
        del_room()
    elif opcion == 7:
        exit = True
    else:
        print ("\nERROR: Introduce una opcion valida")
