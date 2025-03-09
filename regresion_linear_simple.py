import logging
from pathlib import Path
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Configuración de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class SalaryPredictionModel:
    """Clase para manejar el modelo de predicción de salarios basado en regresión lineal."""

    def __init__(self):
        self.model = LinearRegression()

    def load_data(self, file_path: str) -> pd.DataFrame:
        """Carga los datos desde un archivo CSV y verifica su existencia."""
        path = Path(file_path)
        if not path.exists():
            logging.error(f"Archivo no encontrado: {file_path}")
            raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

        logging.info(f"Cargando datos desde {file_path}")
        return pd.read_csv(file_path)

    def prepare_data(
        self, df: pd.DataFrame
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Prepara los datos para el entrenamiento."""
        if "YearsExperience" not in df.columns or "Salary" not in df.columns:
            logging.error("El dataset no contiene las columnas requeridas.")
            raise ValueError("El dataset debe contener 'YearsExperience' y 'Salary'.")

        X = df["YearsExperience"].values.reshape(-1, 1)
        y = df["Salary"].values
        labels = df["Name"].values if "Name" in df.columns else np.array([""] * len(y))
        return X, y, labels

    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> None:
        """Entrena el modelo de regresión lineal."""
        self.model.fit(X_train, y_train)
        logging.info("Modelo entrenado correctamente.")

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Genera predicciones para los datos de entrada."""
        return self.model.predict(X)

    def evaluate(self, y_true: np.ndarray, y_pred: np.ndarray) -> None:
        """Evalúa el modelo con métricas estándar de regresión."""
        mse = mean_squared_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        logging.info(f"MSE: {mse:.4f} | R² Score: {r2:.4f}")

    def plot_data(
        self, X: np.ndarray, y: np.ndarray, labels: np.ndarray, salary_pred: np.ndarray
    ) -> None:
        """Genera un gráfico de dispersión con la regresión lineal."""
        plt.figure(figsize=(10, 6))
        plt.scatter(X, y, color="blue", label="Datos reales")
        plt.plot(X, salary_pred, "r--o", label="Línea de regresión")

        for i, label in enumerate(labels):
            plt.annotate(
                label,
                (X[i], y[i]),
                textcoords="offset points",
                xytext=(0, 5),
                ha="center",
            )

        plt.xlabel("Años de experiencia")
        plt.ylabel("Salario")
        plt.title("Salario vs Años de experiencia")
        plt.legend()
        plt.grid(visible=True)
        plt.show()


def main():
    try:
        model = SalaryPredictionModel()

        # Cargar datos
        data = model.load_data("salaries.csv")
        X, y, labels = model.prepare_data(data)

        # Dividir datos en entrenamiento y prueba
        X_train, X_test, y_train, y_test, labels_train, labels_test = train_test_split(
            X, y, labels, test_size=0.2, random_state=0
        )

        # Entrenar modelo
        model.train(X_train, y_train)

        # Predicciones
        salary_pred_train = model.predict(X_train)
        salary_pred_test = model.predict(X_test)

        # Evaluación
        model.evaluate(y_test, salary_pred_test)

        # Gráficos
        # model.plot_data(X_train, y_train, labels_train, salary_pred_train)
        model.plot_data(X_test, y_test, labels_test, salary_pred_test)

    except Exception as e:
        logging.error(f"Error en la ejecución: {str(e)}")


if __name__ == "__main__":
    main()
