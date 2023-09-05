import random

class Playlist:
    def __init__(self,nombre):
        self.nombre = nombre
        self.canciones = []
        self.estado = "Detenido"
        self.indice_actual = None
    
    def agregar_cancion(self,cancion):
        self.canciones.append(cancion)
    
    def eliminar_cancion(self,cancion):
        if cancion in self.canciones:
            self.canciones.remove(cancion)
            if self.indice_actual is not None and self.indice_actual >= len(self.canciones):
                self.detener()
                print("La canción eliminada se estaba reproduciendo. La reproducción se detuvo.")
        else:
            print("La canción no está agregada en la playlist")

    def mostrar_canciones(self):
        print(f"Canciones en la playlist {self.nombre}")
        for i, cancion in enumerate(self.canciones, start=1):
            print(f"{i}.{cancion}")

    def reproducir(self):
        if len(self.canciones)== 0:
            print("No hay canciones en la playlist")
            return
        if self.estado == "Detenido":
            self.indice_actual = 0
        self.estado = "Reproduciendo"
        print(f"Reproduciendo: {self.canciones[self.indice_actual]}")

    def seleccionar_cancion(self, indice):
        if 0 <= indice < len(self.canciones):
            self.indice_actual = indice
            self.estado = "Reproduciendo"
            print(f"Reproduciendo {self.canciones[self.indice_actual]}")
        else:
            print("El índice de la canción no es válido")

    def pausar (self):
        if self.estado == "Reproduciendo":
            self.estado = "Pausa"
            print("Pausa.")

    def detener(self):
        self.estado = "Detenido"
        print("Reproducción detenida.")

    def siguiente_cancion(self):
        if self.estado == "Reproduciendo":
            self.indice_actual +=1
            if self.indice_actual >= len(self.canciones):
                self.indice_actual = 0
            print(f"Reproduciendo siguiente canción: {self.canciones[self.indice_actual]}")

    def cancion_anterior(self):
        if self.estado == "Reproduciendo":
            self.indice_actual -=1
            if self.indice_actual < 0:
                self.indice_actual = len(self.canciones)-1
            print(f"Reproduciendo canción anterior: {self.canciones[self.indice_actual]}")

    def reproduccion_aleatoria (self):
        if self.estado == "Reproduciendo":
            print("No se puede reproducir aleatoriamente mientras una canción está en reproducción.")
            return
        if len(self.canciones) == 0:
            print("No hay canciones en la playlist.")

        indice_aleatorio = random.randint (0, len(self.canciones)-1)
        self.seleccionar_cancion(indice_aleatorio)

    def ver_estado (self):
        print(f"Estado de la playlist {self.nombre}: {self.estado}")

    def ver_cancion_actual(self):
        if self.estado == "Reproduciendo":
            print(f"Canción actual: {self.canciones[self.indice_actual]}")
        else:
            print("Ninguna canción está en reproducción")

playlist= Playlist("Leve")

while True:
    print("\n--- Menú de la Playlist ---")
    print("1. Agregar canción")
    print("2. Eliminar cancón")
    print("3. Mostrar canciones")
    print("4. Reproducir")
    print("5. Seleccionar canción")
    print("6. Pausar")
    print("7. Detener")
    print("8. Siguiente canción")
    print("9. Canción Anterior")
    print("10. Reproducción aleatoria")
    print("11. Ver Estado")
    print("12. Ver canción actual")
    print("13. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cancion = str(input("Ingresa el nombre de la canción: "))
        playlist.agregar_cancion(cancion)
    elif opcion == "2":
        cancion = str(input("Ingresa el nombre de la canción a eliminar: "))
        playlist.eliminar_cancion(cancion)
    elif opcion == "3":
        playlist.mostrar_canciones()
    elif opcion == "4":
        playlist.reproducir()
    elif opcion == "5":
        indice = int(input("Ingresa el índice de la canción a seleccionar: "))
        playlist.seleccionar_cancion(indice - 1)
    elif opcion == "6":
        playlist.pausar()
    elif opcion == "7":
        playlist.detener()
    elif opcion == "8":
        playlist.siguiente_cancion()
    elif opcion == "9":
        playlist.cancion_anterior()
    elif opcion == "10":
        playlist.reproduccion_aleatoria()
    elif opcion == "11":
        playlist.ver_estado()
    elif opcion == "12":
        playlist.ver_cancion_actual()
    elif opcion == "13":
        break

del playlist