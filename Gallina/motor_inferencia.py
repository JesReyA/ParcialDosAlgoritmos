from base_conocimientos import *
from collections import deque


# Indica si se infringe la regla/restriccion mencionada mediante las posiciones de la persona y ambos individuos
def restriccion_violada(regla, estado):
    lado = estado[regla["come"]]
    return estado[regla["comido"]] == lado and estado["persona"] != lado


# Obtiene el pasajero de algun tipo de movimiento/regla e indica sino hay pasajero o si la posicion del pasajero es la misma que la persona
def regla_aplicable(regla, estado):
    pasajero = regla["pasajero"]
    return pasajero is None or estado[pasajero] == estado["persona"]


# Recorre cada restriccion y busca cuales se violan dependiendo del estado actual usando el metodo restriccion_vialada
# Genera una lista con las violaciones
def violaciones_reglas(estado):
    return [regla for regla in restricciones if restriccion_violada(regla, estado)]

# Metodo que sirve para realizar el cruce de los individuos dependiendo de la regla
def aplicar_regla(movimiento, estado):
    nuevo_estado = dict(estado)
    nuevo_estado["persona"] = cruzar(estado["persona"])
    if movimiento["pasajero"]:
        nuevo_estado[movimiento["pasajero"]] = nuevo_estado["persona"]
    return nuevo_estado


# Genera las tuplas y las ordena siempre en orden alfabético para comparar más fácil
def ordenar_tupla(estado):
    return tuple(sorted(estado.items()))


# En este método se realiza la inferencia en búsqueda de el objetivo y las reglas que se pueden violar en cada estado
def inferencia(estado_inicial, objetivo):
    # Ingresa a una cola el estado inicial junto con el camino, por ahora vacío
    cola_pendientes = deque([(estado_inicial, [])])
    # Se utiliza para guardar los caminos o estados que ya se han recorrido para encontrar bucles
    visitados = {ordenar_tupla(estado_inicial)}
    
    # Mientras haya datos en la cola se sigue el while
    while cola_pendientes:
        # Se saca el dato de la cola y se guarda en dos variables
        estado, camino = cola_pendientes.popleft()
        
        # Se busca saber si el estado ya es el objetivo
        if(estado == objetivo):
            return camino
        
        # Se recorre el diccionario de los movimientos posibles
        for movimiento in movimientos:
            # Si no encuentra que el movimiento sea aplicable al estado pasa al siguiente
            if not regla_aplicable(movimiento, estado):
                continue
            
            # Aplica la regla si es que es posible y la guarda en un nuevo estado
            nueva_posicion = aplicar_regla(movimiento, estado)
            
            # Revisa si la nueva posicion viola alguna regla o si ya se visitó el mismo estado anteriormente
            if violaciones_reglas(nueva_posicion) or ordenar_tupla(nueva_posicion) in visitados:
                continue
            
            # Si nada de lo anterio ocurrió, agrega la nueva posicion a visitados pero primero la ordena
            visitados.add(ordenar_tupla(nueva_posicion))
            
            # Agrega a la cola el nuevo estado y junta el camino actual con el movimiento que se ocupó para el nuevo estado
            cola_pendientes.append((nueva_posicion, camino + [(movimiento, nueva_posicion)]))
            
    # Regresa none si nunca hubo solución
    return None


# Este método sirve para mostrar un string con los individuos que se encuentran de cada lado en un estado
def describir(estado):
    izquierda = [i for i,p in estado.items() if p == IZQUIERDA ]
    derecha = [i for i, p in estado.items() if p == DERECHA]
    return f"IZQUIERDA {izquierda or '...'} | DERECHA {derecha or '...'}"


# El metodo verifica si el inicial no viola la regla antes de iniciar, genera la inferencia y ve primero si existieron pasos
# Si los hay, entonces los muestra uno por uno ayudándose del método anterior, además, al terminar indica cuantos pasos fueron necesarios
def verificar_mostrar_estado():
    if violaciones_reglas(estado_inicial):
        print ("El estado inicial ya viola las reglas")
        return

    pasos = inferencia(estado_inicial, objetivo)

    if pasos is None:
        print("No existe solucion")
        return
    
    print("INICIO PASOS")
    print(f"{describir(estado_inicial)}\n")
    
    for indice, (movimiento, estado) in enumerate(pasos, 1):
        print(f"Paso {indice}: [{movimiento['nombre']}] {movimiento['accion']}")
        print(f"       {describir(estado)}\n")
        
    print(f"\nSe ha alcanzado el objetivo en {len(pasos)} pasos.")
        