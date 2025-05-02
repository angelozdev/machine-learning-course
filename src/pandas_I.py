import pandas as pd
import numpy as np

# 📋 Quiz: Introducción a Pandas (Nivel 1 - Principiante)

# 🟢 Duración: 30 minutos
# 🟢 Preguntas: 30
# 🟢 Formato: Opción múltiple, Verdadero/Falso, Preguntas abiertas

# 🔹 Sección 1: Fundamentos de Pandas (10 preguntas)
# 	1.	¿Qué es Pandas y cuál es su propósito principal en Python?
# a) Una librería para desarrollo web
# b) Un framework para inteligencia artificial
# c) Una librería para manipulación y análisis de datos ←----------
# d) Un módulo para generar gráficos

# 	2.	¿Cómo se instala Pandas en un entorno de Python?
# a) install pandas
# b) pip install pandas <----------
# c) import pandas as pd
# d) python pandas install

# 	3.	¿Cuál es la diferencia principal entre una Series y un DataFrame en Pandas?
# a) Una Series es una lista simple, un DataFrame es una tabla de datos ←----------
# b) No hay diferencia, son lo mismo
# c) Un DataFrame solo permite datos numéricos, una Series permite todo tipo de datos
# d) Un DataFrame es una matriz 3D y una Series es 2D

# 	4.	Verdadero o Falso: Pandas está basado en la librería NumPy. Verdadero

# 	5.	¿Cuál de las siguientes es la forma correcta de importar Pandas en un script de Python?
# a) import pandas
# b) import pandas as pd ←----------
# c) from pandas import *
# d) import pd

# 	6.	¿Qué función de Pandas se usa para obtener información general sobre un DataFrame, incluyendo el número de valores nulos?
# a) df.describe() <----------
# b) df.head()
# c) df.info()
# d) df.columns()

# 	7.	Verdadero o Falso: En Pandas, un DataFrame siempre tiene al menos una columna. Verdadero

# 	8.	¿Cuál de los siguientes métodos devuelve los primeros N registros de un DataFrame?
# a) df.head(N) <----------
# b) df.tail(N)
# c) df.first(N)
# d) df.top(N)

# 	9.	¿Cómo se puede obtener la cantidad de filas y columnas de un DataFrame?
# a) df.size
# b) df.length()
# c) df.shape <----------
# d) df.dimensions()

# 	10.	¿Cuál de los siguientes NO es un tipo de estructura de datos en Pandas? No sé si sea Dictionary o Panel
# a) Series
# b) DataFrame
# c) Dictionary
# d) Panel

# 🔹 Sección 2: Manejo de Datos Básico (10 preguntas)

# 	11.	¿Cuál de los siguientes métodos se usa para crear una Series desde una lista en Pandas?
# a) pd.Series(lista) <----------
# b) pd.DataFrame(lista)
# c) pd.List(lista)
# d) pd.Array(lista)

# 	12.	¿Cómo se crea un DataFrame a partir de un diccionario en Pandas?
# a) pd.DataFrame(diccionario) <----------
# b) pd.Series(diccionario)
# c) pd.Table(diccionario)
# d) pd.Array(diccionario)

# 	13.	¿Qué función de Pandas se usa para leer un archivo CSV en un DataFrame?
# a) pd.read_csv() <----------
# b) pd.read_table()
# c) pd.open_csv()
# d) pd.load_csv()

# 	14.	Verdadero o Falso: Pandas puede leer archivos de Excel sin necesidad de instalar librerías adicionales. Creo que sí.

# 	15.	¿Cómo se accede a una columna específica de un DataFrame?
# a) df.columna
# b) df['columna'] <----------
# c) df.loc[:, 'columna']
# d) Todas las anteriores

# 	16.	¿Cómo se selecciona la primera fila de un DataFrame usando iloc?
# a) df.iloc[0]
# b) df.iloc[:, 0]
# c) df.iloc[0, :] <----------
# d) a) y c) son correctas

# 	17.	¿Cuál es la diferencia entre loc e iloc en Pandas? No tengo ni idea
# a) loc usa etiquetas, iloc usa índices numéricos <---------- :D
# b) loc y iloc son equivalentes
# c) loc usa índices numéricos, iloc usa etiquetas
# d) iloc solo funciona con Series

# 	18.	Verdadero o Falso: Se puede modificar el índice de un DataFrame usando set_index(). Verdadero

# 	19.	¿Cómo se accede a múltiples columnas en un DataFrame? No estoy seguro de esta
# a) df[['col1', 'col2']]
# b) df.loc[:, ['col1', 'col2']]
# c) df.iloc[:, [0, 1]]
# d) Todas las anteriores <----------

# 	20.	¿Qué método se usa para obtener un subconjunto específico de filas y columnas en un DataFrame? No sé.
# a) df.select()
# b) df.loc[] <----------
# c) df.subset()
# d) df.query()

# 🔹 Sección 3: Operaciones Básicas con DataFrames (10 preguntas)

# 	21.	¿Cómo se filtran las filas donde la columna ‘edad’ sea mayor a 30? No sé.
# a) df['edad'] > 30
# b) df[df['edad'] > 30] <----------
# c) df.where(df['edad'] > 30)
# d) df.filter(df['edad'] > 30)

# 	22.	¿Cómo se ordena un DataFrame por la columna ‘salario’ en orden descendente? No sé.
# a) df.sort_values('salario')
# b) df.sort_values('salario', ascending=False) <----------
# c) df.order_by('salario', descending=True)
# d) df.sort('salario', reverse=True)

# 	23.	Verdadero o Falso: rename() permite cambiar los nombres de las columnas de un DataFrame. No sé.

# 	24.	¿Cómo se cambia el nombre de la columna ‘nombre’ a ‘full_name’? No sé.
# a) df.rename(columns={'nombre': 'full_name'})
# b) df.change_column('nombre', 'full_name')
# c) df.columns['nombre'] = 'full_name'
# d) df.rename({'nombre': 'full_name'})

# 	25.	¿Cómo se eliminan las filas con valores nulos en Pandas? No sé.
# a) df.dropna()
# b) df.remove_na()
# c) df.nulls_remove()
# d) df.clean_na()

# 	26.	¿Qué método devuelve un resumen estadístico de un DataFrame?
# a) df.describe() <----------
# b) df.stats()
# c) df.summary()
# d) df.mean()

# 	27.	¿Cómo se obtienen las últimas 5 filas de un DataFrame?
# a) df.tail(5) <----------
# b) df.bottom(5)
# c) df.end(5)
# d) df.last(5)

# 	28.	¿Qué devuelve df.dtypes?
# a) El tipo de dato de cada columna <----------
# b) Los valores únicos de cada columna
# c) Las dimensiones del DataFrame
# d) La memoria utilizada por cada columna

# 	29.	Verdadero o Falso: sort_values() permite ordenar por múltiples columnas. No sé.

# 	30.	¿Cómo se resetea el índice de un DataFrame? Ni idea. No sé ni para que sirve.
# a) df.reset_index()
# b) df.index_reset()
# c) df.drop_index()
# d) df.clear_index()


### Notebook
s1 = pd.Series(
    np.linspace(30, 50, 10), index=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
)
s2 = pd.Series(
    np.linspace(0, 40, 10), index=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
)

print(s1)

print("Diccionario", s1.to_dict())
print("DataFrame", s1.to_frame())
print("List", s1.to_list())
print("Numpy", s1.to_numpy())
print("Series", s1.to_latex())

df = pd.DataFrame(
    {"A": [1, 2, 3], "B": [4, 5, 6]}, index=["Columna 1", "Columna 2", "Columna 3"]
)
print(df)
print(df.describe(), "\n")
print(df.info(), "\n")
print("Shape", df.shape, "\n")
print("Size", df.size, "\n")
print("Ndim", df.ndim, "\n")
print("Columns", df.columns, "\n")
print("Index", df.index, "\n")
print("To Dict", df.to_dict(), "\n")


df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [pd.NA, pd.NA, 213]],
    # index=["Row 1", "Row 2", "Row 3"],
    columns=["Column I", "Column II", "Column III"],
)

print(df, "\n")
print(df.loc[0], "\n")
print(df.iloc[0], "\n")
print(df.iloc[0:1, 0:2], "\n")
print(df.iloc[[1, 2], [1, 2]], "\n")

df.rename(
    columns={"Column I": "Col I", "Column II": "Col II", "Column III": "Col III"},
    inplace=True,
)
print(df, "\n")

df.rename(
    columns={"Col I": "Column I", "Col II": "Column II", "Col III": "Column III"},
    inplace=True,
)
print(df, "\n")

df.dropna(inplace=True)
print(df, "\n")
