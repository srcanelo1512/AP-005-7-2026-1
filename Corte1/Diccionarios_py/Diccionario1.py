
# ---------- CREACIÓN BÁSICA DE DICCIONARIOS ----------
# Un diccionario se define con llaves {} y pares clave:valor

sensors = {
    "living room": 21,   # clave: "living room" | valor: temperatura
    "kitchen": 23,
    "bedroom": 20,
    "pantry": 22
}

num_cameras = {
    "backyard": 6,       # clave: ubicación | valor: número de cámaras
    "garage": 2,
    "driveway": 1
}

print("Sensors:", sensors)        # Imprime todo el diccionario sensors
print("Cameras:", num_cameras)
print()


# ---------- DICCIONARIO DE TRADUCCIÓN ----------
# Las claves y los valores pueden ser strings

translations = {
    "mountain": "orod",  # palabra en inglés → traducción
    "bread": "bass",
    "friend": "mellon",
    "horse": "roch"
}

print("Translations:", translations)
print()


# ---------- ERROR COMÚN (NO EJECUTAR) ----------
# Las listas NO pueden ser claves porque son mutables
# Solo tipos inmutables (str, int, tuple) pueden ser claves

# powers = {[1, 2, 4, 8, 16]: 2}


# ---------- VALORES COMO LISTAS ----------
# Un diccionario puede almacenar listas como valores

children = {
    "von Trapp": ["Johannes", "Rosmarie", "Eleonore"],
    "Corleone": ["Sonny", "Fredo", "Michael"]
}

print("Children:", children)
print()


# ---------- DICCIONARIO VACÍO ----------
# Se usa cuando aún no se tienen datos

my_empty_dictionary = {}
print("Empty dictionary:", my_empty_dictionary)
print()


# ---------- AGREGAR Y MODIFICAR ELEMENTOS ----------
menu = {
    "oatmeal": 3,
    "avocado toast": 6,
    "carrot juice": 5,
    "blueberry muffin": 2
}

print("Menu before:", menu)

menu["cheesecake"] = 8
# ↑ Agrega una nueva clave si no existe

menu["oatmeal"] = 5
# ↑ Modifica el valor si la clave ya existe

print("Menu after:", menu)
print()


# ---------- REEMPLAZO TOTAL DEL DICCIONARIO ----------
animals_in_zoo = {"dinosaurs": 0}

animals_in_zoo = {"horses": 2}
# ↑ Este diccionario reemplaza COMPLETAMENTE al anterior

print("Animals in zoo:", animals_in_zoo)
print()


# ---------- AGREGAR VARIOS ELEMENTOS CON update() ----------
sensors.update({
    "guest room": 25,
    "patio": 34
})
# ↑ update() agrega múltiples pares clave:valor

print("Updated sensors:", sensors)
print()


# ---------- UPDATE VS ASIGNACIÓN DIRECTA ----------
oscar_winners = {
    "Best Picture": "La La Land",
    "Best Actor": "Casey Affleck",
    "Best Actress": "Emma Stone",
    "Animated Feature": "Zootopia"
}

print("Oscars before:", oscar_winners)

oscar_winners.update({"Supporting Actress": "Viola Davis"})
# ↑ Agrega una nueva clave

oscar_winners["Best Picture"] = "Moonlight"
# ↑ Cambia el valor de una clave existente

print("Oscars after:", oscar_winners)
print()


# ======================================================
# DICT COMPREHENSIONS + zip()
# ======================================================

# Dos listas relacionadas por posición
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# zip() une ambas listas en pares (nombre, altura)
# dict comprehension crea el diccionario en una sola línea

students = {
    name: height
    for name, height in zip(names, heights)
}

print("Students:", students)
print()


# ---------- OTRO EJEMPLO CON zip() ----------
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

drinks_to_caffeine = {
    drink: caf
    for drink, caf in zip(drinks, caffeine)
}

print("Drinks caffeine:", drinks_to_caffeine)
print()


# ======================================================
# EJEMPLO FINAL: DICCIONARIOS ANIDADOS
# ======================================================

songs = [
    "Like a Rolling Stone",
    "Satisfaction",
    "Imagine",
    "What's Going On",
    "Respect",
    "Good Vibrations"
]

playcounts = [78, 29, 44, 21, 89, 5]

plays = {
    song: count
    for song, count in zip(songs, playcounts)
}
# ↑ Crea un diccionario canción → número de reproducciones

plays.update({"Purple Haze": 1})
# ↑ Agrega una nueva canción

plays.update({"Respect": 94})
# ↑ Actualiza una canción existente

print("Plays:", plays)
print()


# ---------- DICCIONARIO ANIDADO ----------
library = {
    "The Best Songs": plays,  # diccionario dentro de otro diccionario
    "Sunday Feelings": {}
}

print("Library:", library)
