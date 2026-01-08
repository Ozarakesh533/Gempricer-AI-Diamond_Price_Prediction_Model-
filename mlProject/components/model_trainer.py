import os
from mlProject import logger
from mlProject.config.configuration import ModelTrainerConfig

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        X_train_transformed = pd.read_csv(self.config.X_train_transformed_path)
        y_train = pd.read_csv(self.config.y_train_path)

        model = RandomForestRegressor(n_estimators=self.config.n_estimators, random_state=self.config.random_state)

        # train the model
        model.fit(X_train_transformed, y_train.values.ravel())

        # save the model
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))