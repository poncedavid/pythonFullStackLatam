# funciones_intermedias_1.py

# 1. Actualizar valores en diccionarios y listas
matriz = [[10, 15, 20], [3, 7, 14]]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambia el valor de 3 en matriz por 6
matriz[1][0] = 6 
print(f"Matriz actualizada: {matriz}")

# Cambia el nombre del primer cantante
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(f"Cantantes actualizados: {cantantes}")

# Cambia "Cancún" por "Monterrey" en ciudades
ciudades["México"][2] = "Monterrey" 
print(f"Ciudades actualizadas: {ciudades}")

# Cambia el valor de "latitud" en coordenadas
coordenadas[0]["latitud"] = 9.9355431
print(f"Coordenadas actualizadas: {coordenadas}")


# 2. Iterar a través de una lista de diccionarios
def iterarDiccionario(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave} - {valor}")  # Formato BONUS

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

print("\nIterar a través de una lista de diccionarios:")
iterarDiccionario(cantantes)


# 3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        print(diccionario[llave])

print("\nObtener valores de una lista de diccionarios (nombre):")
iterarDiccionario2("nombre", cantantes)

print("\nObtener valores de una lista de diccionarios (pais):")
iterarDiccionario2("pais", cantantes)


# 4. Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    for llave, lista in diccionario.items():
        print(len(lista), llave.upper())  # Imprime el tamaño y la llave en mayúsculas
        for valor in lista:
            print(valor)

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

print("\nIterar a través de un diccionario con valores de lista:")
imprimirInformacion(costa_rica)