# Ubicaciones
DERECHA = "derecha"
IZQUIERDA = "izquierda"

# Cambio de lugar
def cruzar(posicion):
    return DERECHA if posicion == IZQUIERDA else IZQUIERDA

# Estado inicial
estado_inicial={
        "persona": IZQUIERDA,
        "gallina": IZQUIERDA, 
        "lobo": IZQUIERDA,
        "maiz": IZQUIERDA
}

# Objetivo 
objetivo = {
        "persona": DERECHA,
        "gallina": DERECHA, 
        "lobo": DERECHA,
        "maiz": DERECHA
    }

# Movimientos
movimientos = [
    {
        "nombre" : "M1",
        "pasajero": None,
        "accion" : "movimiento_solo"
    },
    {
        "nombre" : "M2",
        "pasajero": "gallina",
        "accion" : "movimiento_gallina"
    },
    {
        "nombre" : "M3",
        "pasajero": "maiz",
        "accion" : "movimiento_maiz"
    },
    {
        "nombre" : "M4",
        "pasajero": "lobo",
        "accion" : "movimiento_lobo"
    }
]

# Restricciones
restricciones = [
    {
        "nombre": "R1",
        "come": "gallina",
        "comido" : "maiz",
        "explicacion" : "La gallina se come el maiz"
    },
    {
        "nombre": "R2",
        "come": "lobo",
        "comido" : "gallina",
        "explicacion": "El lobo se come la gallina"
    }
]

