import numpy as np

# 📝 Examen de NumPy - Nivel 1 (Fundamentos)

# Duración: 45 minutos
# Total de preguntas: 30
# Formato: Opción múltiple, verdadero/falso y ejercicios prácticos

# 📌 Sección 1: Opción Múltiple (10 preguntas)

# (Selecciona la opción correcta)

# 1️⃣ ¿Cuál es el propósito principal de NumPy?
# a) Crear sitios web
# b) Procesar imágenes
# c) Manipulación y cálculo eficiente de datos numéricos ✅
# d) Desarrollo de interfaces gráficas

# 2️⃣ ¿Cuál de las siguientes opciones es la manera correcta de importar NumPy en Python?
# a) import numpy
# b) import np as numpy
# c) import numpy as np ✅
# d) import numpy(numpy)

# 3️⃣ ¿Cómo creas un array unidimensional en NumPy?
# a) arr = np.array[1, 2, 3, 4]
# b) arr = np.array((1, 2, 3, 4))
# c) arr = np.array([1, 2, 3, 4]) ✅
arr = np.array([1, 2, 3, 4])
print(arr)
# d) arr = array([1, 2, 3, 4])

# 4️⃣ ¿Qué devuelve la función np.zeros((3, 2))?
# a) Un array de 3x2 lleno de ceros ✅
zeros = np.zeros((3, 2))
print(zeros)
# b) Un array de 2x3 lleno de ceros
# c) Un array de 3 elementos llenos de ceros
# d) Un error, porque los valores deben ser enteros

# 5️⃣ ¿Qué método utilizas para conocer el tipo de datos de un array en NumPy?
# a) arr.type()
# b) arr.dtype ✅
print(arr.dtype)
# c) type(arr)
# d) np.dtype(arr) ❌

# 6️⃣ ¿Qué función de NumPy se usa para generar una secuencia de números enteros de 0 a 10 con paso de 2?
# a) np.linspace(0, 10, 2)
# b) np.arange(0, 10, 2) ✅
arange = np.arange(0, 10, 2)
print(arange)
# c) np.array(0, 10, 2)
# d) np.range(0, 10, 2)

# 7️⃣ ¿Cuál de los siguientes métodos genera un array de valores equidistantes entre 1 y 10 en 5 pasos?
# a) np.linspace(1, 10, 5) ✅
linspace = np.linspace(1, 10, 5)
print(linspace)
# b) np.arange(1, 10, 5)
# c) np.arange(1, 10, 2)
# d) np.linspace(1, 10, 2)

# 8️⃣ Si arr = np.array([5, 10, 15, 20, 25]), ¿qué retorna arr[2]?
arr = np.array([5, 10, 15, 20, 25])
# a) 5
# b) 10
# c) 15 ✅
print(arr[2])
# d) 20

# 9️⃣ ¿Qué función de NumPy genera un array de números aleatorios entre 0 y 1?
# a) np.random.rand()
# b) np.random.randint()
# c) np.random.random() ✅
random = np.random.random()
print(random)
# d) np.random.uniform()

# 🔟 ¿Cuál es el tamaño de un array generado con np.zeros((4,3))?
zeros = np.zeros((4, 3))
print(zeros)
# a) 4
# b) 3
# c) 12 ✅
print(zeros.size)
# d) 7

# 📌 Sección 2: Verdadero o Falso (10 preguntas)

# (Escribe V si es verdadero y F si es falso)

# 1️⃣ np.array([1, 2, 3]) crea una lista en Python.
# Respuesta ❌ No, crea un array de numpy
# 2️⃣ NumPy es más rápido que las listas de Python en operaciones numéricas.
# Respuesta ✅
# 3️⃣ np.ones((3, 3)) crea una matriz de ceros de 3x3.
# Respuesta: ❌ No, crea una matriz de unos
# 4️⃣ np.eye(4) crea una matriz identidad de 4x4.
# Respuesta: ✅
# 5️⃣ np.arange(0, 10, 2) crea un array con valores [0, 2, 4, 6, 8].
# Respuesta: ✅
# 6️⃣ np.linspace(1, 5, 3) genera [1.0, 3.0, 5.0].
# Respuesta: ❌ Creo que no, porque el 5 no lo incluye
# 7️⃣ arr.shape devuelve el número total de elementos en un array.
# Respuesta: ❌ No, devuelve la composición del array
# 8️⃣ np.random.randint(1, 10, 5) genera un array con 5 números aleatorios entre 1 y 10.
# Respuesta: No tengo ni idea
# 9️⃣ np.full((2,2), 7) genera una matriz [[7, 7], [7, 7]].
# Respuesta: ✅
# 🔟 np.array([1, 2, 3]) + 2 devuelve [3, 4, 5].
# Respuesta: No tengo ni idea

# 📌 Sección 3: Ejercicios Prácticos (10 preguntas)

# (Escribe el código necesario para realizar cada tarea)

# 1️⃣ Importa la librería NumPy con el alias np.
import numpy as np

# 2️⃣ Crea un array de enteros con los valores [10, 20, 30, 40].
arr = np.array([10, 20, 30, 40])
print(arr)
# 3️⃣ Genera un array de ceros de tamaño 4x3.
zeros = np.zeros((4, 3))
print(zeros)
# 4️⃣ Crea un array con los números del 1 al 10 usando np.arange().
arange = np.arange(1, 11)
print(arange)
# 5️⃣ Genera un array de 5 elementos equidistantes entre 0 y 50.
linspace = np.linspace(0, 50, 5)
print(linspace)
# 6️⃣ Accede al tercer elemento de arr = np.array([5, 15, 25, 35, 45]).
print(arr[2])
# 7️⃣ Crea una matriz de identidad de 3x3.
identity = np.eye(3)
print(identity)
# 8️⃣ Genera un array de 5 números aleatorios entre 0 y 1.
random = np.random.random(5)
print(random)

# 9️⃣ Convierte el array arr = np.array([1.5, 2.8, 3.9]) a enteros. No sé cómo

# 🔟 Genera un array de 10 elementos con valores aleatorios entre 50 y 100.
random = np.random.randint(50, 100, 10)
print(random)


# 📌 Criterios de Evaluación

# Sección Preguntas Puntuación Total
# Opción múltiple 10 30 pts (3 c/u)
# Verdadero/Falso 10 20 pts (2 c/u)
# Ejercicios prácticos 10 50 pts (5 c/u)
# TOTAL 30 100 pts


### Ejercicios de refuerzo

# 1.	Crea un array de 3x4 con números del 1 al 12.
arr = np.random.randint(1, 12, 12).reshape(3, 4)
print(arr)
print("shape: ", arr.shape)
print("size: ", arr.size)
print("shape[0] * shape[1] = size: ", arr.shape[0] * arr.shape[1] == arr.size)


# 2.
arr = np.random.randint(5, 20, 7)
print(arr)
print("Min: ", arr.min())
print("Max: ", arr.max())
print("Mean: ", arr.mean())
print("Median: ", np.median(arr))
print("Std: ", arr.std())
print("Var: ", arr.var())

# 3.
arr = np.linspace(2, 10, 4)
print(arr)

# 4.
arr = np.array([5, 10, 15])
print(arr)
print(arr + 3)

# 5.
arr = np.array([1.7, 3.9, 5.2])
print(arr)
print(arr.astype(np.int32))
print(arr.astype(np.int32), arr.round(), arr.astype(np.int32) == arr.round())
