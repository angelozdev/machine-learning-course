import logging
import os
from typing import Tuple

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from pandas import DataFrame
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

# Configuración de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_data(file_path: str) -> DataFrame:
    """Carga el dataset desde un archivo CSV."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo {file_path} no existe.")

    logging.info(f"Cargando datos desde {file_path}")
    return pd.read_csv(file_path)


def preprocess_features(X: NDArray[np.object_]) -> NDArray[np.float64]:
    """Preprocesa las características: imputación, codificación y escalado."""

    logging.info("Aplicando preprocesamiento a las características")

    # Identificar columnas categóricas (suponiendo que la primera columna es categórica)
    categorical_features = [0]  # Posición de "Country"
    numerical_features = [1, 2]  # Posiciones de "Age" y "Salary"

    # Imputación solo para valores numéricos
    numerical_transformer = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="mean", missing_values=np.nan),
            ),  # Rellena valores faltantes con la media
            ("scaler", StandardScaler()),  # Escala los datos numéricos
        ]
    )

    # Codificación One-Hot para variables categóricas
    categorical_transformer = OneHotEncoder(
        sparse_output=False, handle_unknown="ignore"
    )

    # Aplicar transformaciones específicas a cada tipo de columna
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", categorical_transformer, categorical_features),
            ("num", numerical_transformer, numerical_features),
        ],
        remainder="passthrough",
    )

    # Aplicar preprocesamiento
    transformed_X = preprocessor.fit_transform(X)

    # Asegurar que la salida sea un ndarray de tipo float
    return np.asarray(transformed_X)


def preprocess_target(y: np.ndarray) -> np.ndarray:
    """Codifica la variable objetivo."""
    label_encoder = LabelEncoder()
    logging.info("Aplicando Label Encoding a la variable objetivo")
    transformed_y = label_encoder.fit_transform(y)

    assert transformed_y is not None, "Error: La codificación de y devolvió None"
    return transformed_y


def split_data(
    X: NDArray[np.float64],
    y: NDArray[np.int_],
    test_size: float = 0.2,
    random_state: int = 1997,
) -> Tuple[
    NDArray[np.float64], NDArray[np.float64], NDArray[np.int_], NDArray[np.int_]
]:
    """Divide los datos en conjuntos de entrenamiento y prueba."""
    logging.info("Dividiendo los datos en conjuntos de entrenamiento y prueba")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Convertir cada conjunto en un ndarray explícitamente
    return (
        np.asarray(X_train, dtype=np.float64),
        np.asarray(X_test, dtype=np.float64),
        np.asarray(y_train, dtype=np.int_),
        np.asarray(y_test, dtype=np.int_),
    )


def main():
    root = os.getcwd()
    file_path = os.path.join(root, "data.csv")

    dataset = load_data(file_path)

    X = dataset.iloc[:, :-1].values  # Todas las columnas menos la última
    y = dataset.iloc[:, -1:].values  # Solo la última columna

    X = preprocess_features(X)
    y = preprocess_target(y)

    X_train, X_test, y_train, y_test = split_data(X, y)

    logging.info(f"X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")
    logging.info(f"y_train shape: {y_train.shape}, y_test shape: {y_test.shape}")
    print(X_train)


if __name__ == "__main__":
    main()
