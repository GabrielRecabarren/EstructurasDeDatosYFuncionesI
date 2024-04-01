
import sys

def convertir_pesos(tasa_sol, tasa_peso_arg, tasa_dolar, valor_pesos):
    valor_sol = valor_pesos * tasa_sol
    valor_peso_arg = valor_pesos * tasa_peso_arg
    valor_dolar = valor_pesos * tasa_dolar
    return valor_sol, valor_peso_arg, valor_dolar

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso incorrecto. Debe proporcionar 4 tasas de conversión y el valor en pesos chilenos a convertir.")
        sys.exit(1)

    try:
        tasa_sol = float(sys.argv[1])
        tasa_peso_arg = float(sys.argv[2])
        tasa_dolar = float(sys.argv[3])
        valor_pesos = float(sys.argv[4])
    except ValueError:
        print("Los argumentos deben ser números válidos.")
        sys.exit(1)

    valor_sol, valor_peso_arg, valor_dolar = convertir_pesos(tasa_sol, tasa_peso_arg, tasa_dolar, valor_pesos)
    print(f"Los {valor_pesos} pesos equivalen a:")
    print(f"{valor_sol} Soles")
    print(f"{valor_peso_arg} Pesos Argentinos")
    print(f"{valor_dolar} Dólares")
