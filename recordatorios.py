
def agregar_evento(recordatorios, fecha, hora, descripcion):
    nuevo_evento = [fecha, hora, descripcion]
    recordatorios.append(nuevo_evento)
    recordatorios.sort()
    return recordatorios

def corregir_evento(recordatorios, fecha, nueva_fecha):
    for evento in recordatorios:
        if evento[0] == fecha:
            evento[0] = nueva_fecha
    recordatorios.sort()
    return recordatorios

def eliminar_evento(recordatorios, descripcion):
    recordatorios = [evento for evento in recordatorios if evento[2] != descripcion]
    return recordatorios

if __name__ == "__main__":
    recordatorios = [
        ['2021-01-01', '11:00', 'Levantarse y ejercitar'],
        ['2021-07-15', '13:00', 'No hacer nada es feriado'],
        ['2021-09-18', '16:00', 'Ramadas']
    ]

    recordatorios = agregar_evento(recordatorios, '2021-02-02', '06:00', 'Empezar el año')
    recordatorios = corregir_evento(recordatorios, '2021-07-15', '2021-07-16')
    recordatorios = eliminar_evento(recordatorios, 'Día del trabajo')
    recordatorios = agregar_evento(recordatorios, '2021-12-24', '22:00', 'Cena de Navidad')
    recordatorios = agregar_evento(recordatorios, '2021-12-25', '00:00', 'Navidad')
    recordatorios = agregar_evento(recordatorios, '2021-12-31', '22:00', 'Cena de Año Nuevo')

    print(recordatorios)
