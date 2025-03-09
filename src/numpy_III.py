import numpy as np

# 📝 Examen de NumPy - Nivel 3 (Manipulación Avanzada de Arrays)

# Duración: 60 minutos
# Total de preguntas: 30
# Formato: Opción múltiple, verdadero/falso y ejercicios prácticos

# 📌 Sección 1: Opción Múltiple (10 preguntas)

# (Selecciona la opción correcta)

# 1️⃣ ¿Qué hace arr.reshape(3, 2) si arr tiene 6 elementos?
# a) Devuelve un error
# b) Crea una matriz de 3x2 ✅
# c) Crea una matriz de 2x3
# d) Modifica el array original

# 2️⃣ ¿Cuál de las siguientes opciones aplana un array multidimensional en un solo vector?
# a) arr.flatten() ✅
# b) arr.reshape(-1)
# c) arr.ravel()
# d) Todas las anteriores

# 3️⃣ ¿Cómo se concatenan dos arrays horizontalmente en NumPy? No sé. Creo que es la D
# a) np.vstack((arr1, arr2))
# b) np.hstack((arr1, arr2))
# c) np.concatenate((arr1, arr2), axis=1)
# d) b) y c) son correctas

# 4️⃣ Si arr.shape = (4, 3), ¿cuál será su nueva forma tras aplicar arr.T?
# a) (3, 4) ✅
# b) (4, 3)
# c) (12, 1)
# d) (1, 12)

# 5️⃣ ¿Qué hace np.newaxis en un array 1D? No sé
# a) Agrega una nueva dimensión
# b) Cambia el tipo de dato (dtype)
# c) Ordena el array en orden ascendente
# d) No tiene efecto en el array

# 6️⃣ ¿Cuál es el resultado de np.expand_dims(arr, axis=1) en un array 1D? No sé.
# a) Convierte el array en una fila (1xN)
# b) Convierte el array en una columna (Nx1)
# c) No hace nada
# d) Aplica una transposición

# 7️⃣ ¿Cómo dividir un array arr en 3 partes iguales?
# a) np.hsplit(arr, 3)
# b) np.vsplit(arr, 3)
# c) np.split(arr, 3) ✅
# d) np.array_split(arr, 3)

# 8️⃣ ¿Qué hace np.clip(arr, a_min=0, a_max=10)? No sé
# a) Elimina valores fuera del rango [0,10]
# b) Sustituye valores menores a 0 con 0, y mayores a 10 con 10
# c) Normaliza el array entre 0 y 10
# d) Redondea los valores del array

# 9️⃣ ¿Cuál de las siguientes funciones aplica operaciones matemáticas elemento a elemento?
# a) np.sqrt(arr)
# b) np.log(arr)
# c) np.exp(arr)
# d) Todas las anteriores ✅

# 🔟 Si A tiene forma (2,3) y B tiene forma (3,), ¿puede A + B ejecutarse correctamente?
# a) No, porque las formas no son iguales
# b) Sí, gracias a broadcasting
# c) Solo si B se transpone antes (B.T)
# d) Solo si B es convertido en una matriz (3,1) ✅

# 📌 Sección 2: Verdadero o Falso (10 preguntas)

# 1️⃣ arr.reshape(-1, 2) convierte un array 1D en una matriz con 2 columnas.
# 2️⃣ arr.ravel() y arr.flatten() devuelven el mismo resultado, pero ravel() evita hacer copias.
# 3️⃣ np.hstack() y np.vstack() son equivalentes.
# 4️⃣ np.transpose(arr) es lo mismo que arr.T.
# 5️⃣ np.newaxis solo funciona en arrays 2D.
# 6️⃣ np.expand_dims(arr, axis=0) agrega una nueva fila.
# 7️⃣ np.clip(arr, 5, 10) asegura que todos los valores estén entre 5 y 10.
# 8️⃣ np.log(arr) puede generar errores si arr tiene valores negativos.
# 9️⃣ np.sqrt(arr) puede manejar valores negativos sin error.
# 🔟 np.split(arr, 3) siempre dividirá el array en partes exactas.

# 📌 Sección 3: Ejercicios Prácticos (10 preguntas)

# ✍ Escribe el código necesario para realizar cada tarea.

# 1️⃣ Cambia la forma de un array de tamaño 12 a una matriz 3x4.

# 2️⃣ Aplana una matriz 4x4 en un vector 1D.

# 3️⃣ Concatena dos arrays:
# 	•	arr1 = np.array([[1, 2], [3, 4]])
# 	•	arr2 = np.array([[5, 6], [7, 8]])
# 	•	Une los arrays verticalmente y horizontalmente.

# 4️⃣ Divide un array np.arange(12) en tres partes iguales.

# 5️⃣ Transpone una matriz 3x5 y verifica su nueva forma.

# 6️⃣ Usa broadcasting para sumar un array de forma (3,1) con otro de (3,).

# 7️⃣ Usa np.newaxis para convertir un array de (5,) en una columna (5,1).

# 8️⃣ Filtra valores en un array np.random.randint(0, 100, 10) para obtener solo los números mayores a 50.

# 9️⃣ Usa np.clip() para forzar que los valores de un array np.random.randint(-10, 20, 10) estén en el rango [0, 10].

# 🔟 Ejercicio Retador:
# 	•	Genera una matriz 4x4 de valores aleatorios.
# 	•	Normaliza sus valores entre 0 y 1 (usa min-max scaling).
# 	•	Imprime la matriz resultante.

# 📌 Criterios de Evaluación

# Sección	Preguntas	Puntuación Total
# Opción múltiple	10	30 pts (3 c/u)
# Verdadero/Falso	10	20 pts (2 c/u)
# Ejercicios prácticos	10	50 pts (5 c/u)
# TOTAL	30	100 pts

# 🚀 ¿Listo para el reto?

# 💡 Resuelve el examen sin buscar respuestas y dime cuándo termines para calificarte. ¡Éxito! 🎯🔥


### Correcciones
arr = np.random.randint(0, 100, (3, 4))
print(arr)
print(arr.reshape(6, -1))

arr = np.random.randint(0, 100, (4, 4))
print(arr)
print(arr.flatten())

arr = np.random.randint(0, 100, (2, 2))
print(arr)
print(arr.ravel())


arr1 = np.random.randint(0, 100, (3, 2))
arr2 = np.random.randint(0, 100, (3, 2))

print("arr1 --------->", arr1)
print("arr2 --------->", arr2)
print("concatenate -->", np.concatenate((arr1, arr2), axis=1))
# print("vstack ------->", np.vstack((arr1, arr2)))
# print("hstack ------->", np.hstack((arr1, arr2)))


arr = np.random.randint(0, 100, 4)
print(arr)
print(arr[np.newaxis, :])
print(np.expand_dims(arr, axis=0))

arr = np.random.randint(0, 100, (3, 4))
print("\n")
print(arr)
print(arr.clip(50, 100))
print(np.clip(arr, 50, 100))
