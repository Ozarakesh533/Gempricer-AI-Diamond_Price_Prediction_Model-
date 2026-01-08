from mlProject import logger
from mlProject.utils.common import save_json
from mlProject.entity.config_entity import ModelEvaluationConfig

import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from urllib.parse import urlparse

import mlflow
import mlflow.sklearn

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def get_eval_metric(self, actual, pred):
        mae = mean_absolute_error(actual, pred)
        mse = mean_squared_error(actual, pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(actual, pred)

        return mae, mse, rmse, r2
    
    def mlflow_experiments(self):
        X_test_transformed = pd.read_csv(self.config.X_test_transformed_path)
        y_test = pd.read_csv(self.config.y_test_path)

        model = joblib.load(self.config.model_path)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            pred = model.predict(X_test_transformed)
            (mae, mse, rmse, r2) = self.get_eval_metric(y_test, pred)

            # metrics directory
            metrics_dir = Path(self.config.metric_file).parent
            metrics_dir.mkdir(parents=True, exist_ok=True)

            # Save metrics to local JSON file
            scores = {"mae": mae, "mse": mse, "rmse": rmse, "r2": r2}
            save_json(path=Path(self.config.metric_file), data=scores)

            # mlflow log params
            mlflow.log_params(self.config.all_params)

            # mlflow log metrics
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("mse", mse)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)

            # In DAGsHub, if model name exists
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="RandomForestRegressor")
            else:
                mlflow.sklearn.load_model(model, "model")