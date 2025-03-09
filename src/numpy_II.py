import numpy as np

# 📝 Examen de NumPy - Nivel 2 (Manipulación de Arrays y Operaciones Matemáticas)

# Duración: 60 minutos
# Total de preguntas: 30
# Formato: Opción múltiple, verdadero/falso y ejercicios prácticos

# 📌 Sección 1: Opción Múltiple (10 preguntas)

# (Selecciona la opción correcta)

# 1️⃣ ¿Qué resultado se obtiene al ejecutar arr[2:10:2] sobre un array de 10 elementos?
# a) Devuelve los elementos en posiciones impares
# b) Devuelve los elementos en posiciones pares entre los índices 2 y 10 ✅
# c) Devuelve todos los elementos del array
# d) Genera un error

# 2️⃣ Dado arr = np.array([4, 7, 1, 8, 3]), ¿cuál es el resultado de arr[arr > 5]?
# a) [4, 7, 8]
# b) [7, 8] ✅
# c) [4, 1, 3]
# d) [7, 8, 3]

# 3️⃣ ¿Qué hace np.where(arr % 2 == 0, "par", "impar")? No tengo idea pero voy a adivinar
# a) Reemplaza los números pares por "par" y los impares por "impar" ✅
# b) Filtra solo los números pares
# c) Retorna la posición de los números pares
# d) Crea un array de ceros y unos

# 4️⃣ ¿Qué valor retorna np.percentile(arr, 50) en un array ordenado? No sé
# a) Media
# b) Mediana
# c) Mínimo
# d) Máximo

# 5️⃣ ¿Cuál es el resultado de np.mean(np.array([10, 20, 30]))?
# a) 10
# b) 20 ✅
# c) 30
# d) 15

# 6️⃣ ¿Cómo se genera un array de 5 valores aleatorios entre 0 y 1?
# a) np.random.randint(0, 1, 5)
# b) np.random.random(5) ✅
# c) np.random.rand(5, 5)
# d) np.random.uniform(0, 1, 5)

# 7️⃣ ¿Cuál de las siguientes opciones es una operación válida en NumPy?
# a) arr **= 2
# b) arr *= 5
# c) arr = arr / 2
# d) Todas las anteriores ✅ Creo que esta

# 8️⃣ ¿Qué hace arr[arr % 2 == 0] = -1?
# a) Reemplaza los valores impares por -1
# b) Elimina los valores pares
# c) Reemplaza los valores pares por -1 ✅ Creo que esta
# d) Genera un error

# 9️⃣ ¿Cuál es el resultado de np.var(np.array([10, 20, 30]))?
# a) 66.67 ✅
# b) 50.0
# c) 25.0
# d) 100.0

# 🔟 ¿Cuál de los siguientes métodos genera un array con valores entre 5 y 15 en pasos de 2?
# a) np.arange(5, 15, 2) ✅
# b) np.linspace(5, 15, 2)
# c) np.arange(5, 15, 5)
# d) np.linspace(5, 15, 5)

# 📌 Sección 2: Verdadero o Falso (10 preguntas)

# 1️⃣ arr[::-1] revierte el array.
# Respuesta: No sé la verdad
# 2️⃣ arr[::2] selecciona elementos en posiciones pares del array.
# Respuesta: Verdad
# 3️⃣ np.where(arr > 0, "positivo", "negativo") cambia valores positivos por "positivo" y negativos por "negativo".
# Respuesta: Sí
# 4️⃣ np.median(arr) y np.percentile(arr, 50) siempre devuelven el mismo resultado.
# Respuesta: No sé. No debería.
# 5️⃣ np.random.randint(10, 50, 5) genera 5 números enteros aleatorios entre 10 y 50, incluyendo el 50.
# Respuesta: Sí, aunque no sé si el 50 es incluido.
# 6️⃣ arr[arr > 5] devuelve las posiciones donde los valores son mayores a 5.
# Respuesta: Sí
# 7️⃣ arr[arr % 3 == 0] = -1 reemplaza los valores múltiplos de 3 por -1.
# Respuesta: Sí
# 8️⃣ np.std(arr) y np.var(arr) siempre devuelven el mismo valor.
# Respuesta: No
# 9️⃣ arr[5] = 100 modifica el sexto elemento de arr.
# Respuesta: Sí
# 🔟 np.random.rand(3,3) genera una matriz de 3x3 con valores entre 0 y 1.
# Respuesta: No sé

# 📌 Sección 3: Ejercicios Prácticos (10 preguntas)

# ✍ Escribe el código necesario para realizar cada tarea.

# 1️⃣ Crea un array de números del 1 al 20, pero selecciona solo los números en posiciones impares.
arr = np.arange(1, 21, step=2)
print(arr)

# 2️⃣ Genera un array con valores de 10 a 100 en pasos de 10, y reemplaza los valores mayores a 50 por -1.
arr = np.arange(10, 101, step=10)
arr[arr > 50] = -1
print(arr)

# 3️⃣ Genera un array de 10 números aleatorios entre 0 y 1, y selecciona los valores menores a 0.5.
arr = np.random.random(10)
arr = arr[arr > 0.5]
print(arr)

# 4️⃣ Crea un array con los valores [4, 8, 12, 16], y usa np.where() para reemplazar los valores mayores a 10 por "Alto" y los menores o iguales a 10 por "Bajo".
arr = np.array([4, 8, 12, 16])
print(arr)
print(np.where(arr > 10, "Alto", "Bajo"))

# 5️⃣ Genera un array de 20 valores aleatorios entre 1 y 100, y calcula su media, mediana, varianza y desviación estándar.
arr = np.random.randint(1, 101, 20)
print(arr)
print("Mean", arr.mean())
print("Var", arr.var())
print("Std", arr.std())
print("Median", np.median(arr))

# 6️⃣ Crea un array con valores de 50 a 100 en pasos de 5, y selecciona los valores que sean múltiplos de 10.
arr = np.arange(50, 100, 5)
arr = arr[arr % 10 == 0]
print(arr)

# 7️⃣ Genera una matriz 4x4 de números aleatorios entre 1 y 50, y encuentra el valor mínimo y máximo de cada columna.
arr = np.random.randint(1, 51, (4, 4))
print(arr)
print(arr.min(axis=0))
print(arr.max(axis=0))

# 8️⃣ Crea un array de 15 valores aleatorios enteros entre 1 y 100, y reemplaza los números pares por 0.
arr = np.random.choice(100, 15)
print(arr)
arr[arr % 2 == 0] = 0
print(arr)

# 9️⃣ Genera un array de 10 elementos y reemplaza los valores mayores a la media por 1 y los menores o iguales a la media por 0.
arr = np.random.choice(100, 10)
print(arr)
print(np.where(arr > arr.mean(), 1, 0))

# 🔟 Ejercicio Retador:
# 	•	Crea un array con los números del 1 al 100.
# 	•	Reemplaza los valores múltiplos de 3 por -1.
# 	•	Imprime el array resultante.
arr = np.arange(1, 101)
print(arr)
arr[arr % 3 == 0] = -1
print(arr)

# 📌 Criterios de Evaluación

# Sección	Preguntas	Puntuación Total
# Opción múltiple	10	30 pts (3 c/u)
# Verdadero/Falso	10	20 pts (2 c/u)
# Ejercicios prácticos	10	50 pts (5 c/u)
# TOTAL	30	100 pts


### Correcciones
arr = np.array([10, 20, 30])
print(np.var(arr))

arr = np.arange(1, 100)
print(arr[::5][::-1])

arr = np.random.randint(1, 51, (4, 4))
print(arr)
