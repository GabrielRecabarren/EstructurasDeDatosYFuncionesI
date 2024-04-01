
def contar_caracteres_distintos(texto):
    caracteres_distintos = set(texto)
    return len(caracteres_distintos)

def contar_palabras_distintas(texto):
    palabras = texto.split()
    palabras_distintas = set(palabras)
    return len(palabras_distintas)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso incorrecto. Debe proporcionar la ruta del archivo de texto.")
        sys.exit(1)

    try:
        with open(sys.argv[1], "r") as file:
            texto = file.read()
    except FileNotFoundError:
        print("El archivo especificado no se encuentra.")
        sys.exit(1)

    caracteres_distintos = contar_caracteres_distintos(texto)
    palabras_distintas = contar_palabras_distintas(texto)

    print(f"El número de caracteres distintos es: {caracteres_distintos}")
    print(f"El número de palabras distintas es: {palabras_distintas}")
