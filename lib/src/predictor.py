import joblib
from pandas import DataFrame
from sklearn.calibration import LabelEncoder
from sklearn.ensemble import RandomForestClassifier


class Predictor:
    _decoder: LabelEncoder
    _model: RandomForestClassifier
    
    def start(self):
        self._decoder = joblib.load("label_encoder_acoes.pkl")
        self._model = joblib.load("modelo_random_forest_acoes.pkl")

    def predict(self, values: dict[str, float]) -> str:
        result = self._model.predict(DataFrame([values]))
        return self._decoder.inverse_transform(result).item()
