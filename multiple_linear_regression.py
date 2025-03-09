import logging
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer, OneHotEncoder, StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor

logging.basicConfig(level=logging.INFO)


class MultipleLinearRegression:
    def __init__(self):
        self.model = LinearRegression()

    def load_data(self, file_path: str) -> pd.DataFrame:
        path = Path(file_path)
        if not path.exists():
            logging.error(f"Archivo no encontrado: {file_path}")
            raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

        logging.info(f"Cargando datos desde {file_path}")
        return pd.read_csv(file_path)

    def preprocess_data(self, df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
        X = df.drop(columns=["Profit"])
        y = df["Profit"]

        numeric_features = X.select_dtypes(include=[np.number]).columns.to_list()
        categorical_features = ["State"]

        scaler = StandardScaler()
        one_hot_encoder = OneHotEncoder(drop="first", handle_unknown="ignore")

        preprocessor = ColumnTransformer(
            [
                ("num", scaler, numeric_features),
                ("cat", one_hot_encoder, categorical_features),
            ],
            remainder="passthrough",
        )

        X_transformed = preprocessor.fit_transform(X)
        categorical_feature_names = (
            preprocessor.named_transformers_["cat"].get_feature_names_out().tolist()
        )
        feature_names = numeric_features + categorical_feature_names

        X_transformed = pd.DataFrame(X_transformed, columns=feature_names)

        return X_transformed, y

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        self.model.fit(X, y)


    def split_data(self, X: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        return train_test_split(X, y, test_size=0.2, random_state=1997)

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.predict(X)
        

    def plot_residuals(self, y_pred: np.ndarray, y_test: np.ndarray) -> None:
        residuals = y_test - y_pred

        plt.figure(figsize=(8, 5))
        plt.scatter(y_pred, residuals, alpha=0.4)
        plt.xlabel("Predicciones")
        plt.ylabel("Residuales")
        plt.axhline(y=0, color="red", linestyle="--", linewidth=2)
        plt.title("Análisis de Residuales - Regresión Múltiple")
        plt.grid(True)
        plt.show()

    def evaluate_model(self, y_pred: np.ndarray, y_test: np.ndarray) -> None:
        a = mean_squared_error(y_test, y_pred)
        print(f"Error cuadrático medio: {a}")
        print(f"Error absoluto medio: {mean_absolute_error(y_test, y_pred)}")
        print(f"R2 score: {r2_score(y_test, y_pred)}")
        print(f"Coeficiente de determinación: {self.model.score(X_test, y_test)}")

    def backward_elimination(self, X: np.ndarray, y: np.ndarray) -> None:
        pass


if __name__ == "__main__":
    model = MultipleLinearRegression()
    df = model.load_data("data/50_Startups.csv")
    X, y = model.preprocess_data(df)
    X_train, X_test, y_train, y_test = model.split_data(X, y)
    model.train(X_train, y_train)

    y_pred = model.predict(X_test)
    # model.plot_residuals(y_pred, y_test)
    model.evaluate_model(y_pred, y_test)

    # Backward Elimination
        
