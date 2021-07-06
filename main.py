import random

lista_palabras = ["irreversible", "xilofon", "cavernicola", "paralelepipedo", "ventrilocuo", "extrasensorial", "linterna", "escaleras", "reaccionario", "dificultad", "saxofonista", "atmosfera", "literatura", "zanahoria", "muchedumbre", "jengibre", "insipido", "electromagnetismo", "peyorativo", "hemisferio", "keratina"]

def main():
    continuar = "S"
    while continuar.lower()=="s":
        modo_juego = elegir_modo()
        if modo_juego==1:
            modo_un_jugador()
        else:
            modo_dos_jugadores()
        continuar = input("Desea continuar jugando? s para si, n para no: ")


def elegir_modo():
    """Pide al usuario que ingrese la cantidad de jugadores con un maximo de 2 y lo devuelve."""
    modo = "a"
    while modo.isalpha():
        modo = input("Ingrese la cantidad de jugadores (maximo 2):\n")
        if modo=="1" or modo=="2":
            return int(modo)
        else:
            modo = "a"


def elegir_palabra_aleatoria(palabras):
    """Recibe una lista con palabras y selecciona al azar una palabra de la lista."""
    if len(palabras)>0:
        palabra = random.choice(palabras)
        return palabra
    else:
        print("La lista de palabras esta vacia.")


def seleccionar_palabra():
    """Pide a cada jugador el ingreso de una palabra y las devuelve en modo de tupla."""
    palabra_jugador_2 = input("Jugador 1 ingrese una palabra para el jugador 2:\n")
    while not palabra_jugador_2.isalpha():
        palabra_jugador_2 = input("Ingrese una palabra para el jugador 2:\n")
    palabra_jugador_1 = input("Jugador 2 ingrese una palabra para el jugador 1:\n")
    while not palabra_jugador_1.isalpha():
        palabra_jugador_1 = input("Ingrese una palabra para el jugador 1:\n")
    tupla_palabras = (palabra_jugador_1,palabra_jugador_2)
    return tupla_palabras


def ingresar_letra():
    """Pide al usuario el ingreso de una letra y devuelve la letra ingresada."""
    letra = input("Ingrese una letra: ")
    while not letra.isalpha() and len(letra)>1:
        letra = input("Ingrese una letra: ")
    return letra


def codificar_palabra(palabra):
    """Recibe una palabra y la devuelve codificada."""
    palabra_codificada = "-"*len(palabra)
    return palabra_codificada


def completar_palabra(letra,palabra_codificada,palabra):
    """Recibe una letra, la palabra seleccionada y una representacion de la palabra, la agrega en la representacion de la palabra y devuelve una lista con las letras de la palabra."""
    lista_palabra = []
    for a in palabra_codificada:
        lista_palabra.append(a)
    for i in range(len(palabra)):
        if letra==palabra[i]:
            lista_palabra[i] = palabra[i]
    return lista_palabra


def graficar_cuerpo(vidas):
    """Recibe un numero entero e imprime por pantalla una representacion grafica del estado actual de las vidas del jugador."""
    if vidas==6:
        print("  ___  ")
        print(" |  |  ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print("_|_    ")
    elif vidas==5:
        print("  ___  ")
        print(" |  |  ")
        print(" |  O  ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print("_|_    ")
    elif vidas==4:
        print("  ___  ")
        print(" |  |  ")
        print(" |  O  ")
        print(" |  |  ")
        print(" |  |  ")
        print(" |     ")
        print("_|_    ")
    elif vidas==3:
        print("  ___  ")
        print(" |  |  ")
        print(" |  O  ")
        print(" | /|  ")
        print(" |  |  ")
        print(" |     ")
        print("_|_    ")
    elif vidas==2:
        print("  ___  ")
        print(" |  |  ")
        print(" |  O  ")
        print(" | /|\ ")
        print(" |  |  ")
        print(" |     ")
        print("_|_    ")
    elif vidas==1:
        print("  ___  ")
        print(" |  |  ")
        print(" |  O  ")
        print(" | /|\ ")
        print(" |  |  ")
        print(" | /   ")
        print("_|_    ")
    elif vidas==0:
        print("  ___  ")
        print(" |  |  ")
        print(" |  O  ")
        print(" | /|\ ")
        print(" |  |  ")
        print(" | / \ ")
        print("_|_    ")



def imprimir_letras_descartadas(letras_descartadas):
    """Recibe una lista de letras descartadas y las muestra por pantalla. """
    print("Letras descartadas: ",", ".join(letras_descartadas))


def modo_un_jugador():
    vidas = 6
    palabra_jugador = elegir_palabra_aleatoria(lista_palabras)
    palabra_codificada = codificar_palabra(palabra_jugador)
    letras_descartadas = []
    terminar = "no"
    while terminar=="no":
        graficar_cuerpo(vidas)
        print(palabra_codificada)
        imprimir_letras_descartadas(letras_descartadas)
        letra = ingresar_letra()
        if letra in palabra_jugador and not letra in palabra_codificada:
            print("Ha acertado!")
            lista_palabra_jugador = completar_palabra(letra,palabra_codificada,palabra_jugador)
            progreso_palabra = "".join(lista_palabra_jugador)
            palabra_codificada = progreso_palabra
        elif letra in palabra_codificada or letra in letras_descartadas:
            print("Ya elegiste esa letra!")
        else:
            print("U.U ", letra,"no se encuentra en la palabra")
            letras_descartadas.append(letra)
            vidas -= 1
        if palabra_codificada==palabra_jugador:
            print("Has ganado! La palabra secreta es: ",palabra_jugador)
            terminar = "si"
        elif vidas==0:
            graficar_cuerpo(vidas)
            print("Game Over! Usted ha perdido, la palabra secreta era: ",palabra_jugador)
            terminar = "si"

def modo_dos_jugadores():
    vida_jugador_1 = 6
    vida_jugador_2 = 6
    
    palabras_seleccionadas = seleccionar_palabra()
    
    palabra_jugador_1 = palabras_seleccionadas[0]
    palabra_jugador_2 = palabras_seleccionadas[1]
    
    palabra_j1_codificada = codificar_palabra(palabra_jugador_1)
    palabra_j2_codificada = codificar_palabra(palabra_jugador_2)
    
    letras_descartadas_j1 = []
    letras_descartadas_j2 = []
    
    terminar_j1 = "no"
    terminar_j2 = "no"
    
    while terminar_j1=="no" and terminar_j2=="no":
        print("\nTurno jugador nº1. Vidas: ", vida_jugador_1)
        graficar_cuerpo(vida_jugador_1)
        print(palabra_j1_codificada)
        letra_j1 = ingresar_letra()
        if letra_j1 in palabra_jugador_1 and not letra_j1 in palabra_j1_codificada:
            print("Ha acertado!")
            lista_palabra_j1 = completar_palabra(letra_j1,palabra_j1_codificada,palabra_jugador_1)
            progreso_j1 = "".join(lista_palabra_j1)
            palabra_j1_codificada = progreso_j1
        elif letra_j1 in palabra_j1_codificada or letra_j1 in letras_descartadas_j1:
            print("Ya elegiste esa letra!")
        else:
            print("U.U ", letra_j1,"no se encuentra en la palabra.")
            letras_descartadas_j1.append(letra_j1)
            print("Letras descartadas jugador 1: ",", ".join(letras_descartadas_j1))
            vida_jugador_1 -= 1
        if palabra_j1_codificada==palabra_jugador_1:
            print("El jugador nº1 ha ganado! Su palabra secreta es: ",palabra_jugador_1)
            terminar_j1 = "si"
        elif vida_jugador_1==0:
            mostrar_derrota(1, vida_jugador_1, palabra_jugador_1)
            terminar_j1=="si"
        while terminar_j2=="no" and (vida_jugador_1<vida_jugador_2 or terminar_j1=="si"):
            print("\nTurno jugador nº2. Vidas: ", vida_jugador_2)
            graficar_cuerpo(vida_jugador_2)
            print(palabra_j2_codificada)
            letra_j2 = ingresar_letra()
            if letra_j2 in palabra_jugador_2:
                print("Ha acertado!")
                lista_palabra_j2 = completar_palabra(letra_j2,palabra_j2_codificada,palabra_jugador_2)
                progreso_j2 = "".join(lista_palabra_j2)
                palabra_j2_codificada = progreso_j2
            else:
                print("U.U ", letra_j2,"no se encuentra en la palabra.")
                letras_descartadas_j2.append(letra_j2)
                print("Letras descartadas jugador 2: ",", ".join(letras_descartadas_j2))
                vida_jugador_2 -= 1
            if palabra_j2_codificada==palabra_jugador_2:
                print("Eljugador nº2 ha ganado! Su palabra secreta es: ",palabra_jugador_2)
                terminar_j2 = "si"
            elif vida_jugador_2==0:
                mostrar_derrota(2, vida_jugador_2, palabra_jugador_2)
                terminar_j2 = "si"

def mostrar_derrota(numero_jugador, vidas, palabra):
    """Recibe el numero, las vidas y la palabra del jugador, grafica el cuerpo del ahorcado y muestra un mensaje por pantalla."""
    graficar_cuerpo(vidas)
    print("El jugador nº",numero_jugador," ha perdido... Su palabra secreta era: ",palabra)


main()