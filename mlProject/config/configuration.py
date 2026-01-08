from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig,
                                            ModelTrainerConfig, ModelEvaluationConfig)

class ConfigurationManager:
    # pull yaml file paths from constants
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        # read yaml files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # create a list of directories
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        # create root directory
        create_directories([config.root_dir])

        # create a config for Data Ingestion
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        # config file
        config = self.config.data_validation

        # schema file
        schema = self.schema.COLUMNS

        # create data validation directory
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            # config
            root_dir = config.root_dir,
            unzip_data_dir = config.unzip_data_dir,
            STATUS_FILE = config.STATUS_FILE,

            # schema
            all_schema = schema
        )
        
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        schema = self.schema.TARGET

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            target_column = schema.name
        )
        
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.RandomForestRegressor

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            X_train_transformed_path = config.X_train_transformed_path,
            y_train_path = config.y_train_path,
            model_name = config.model_name,
            n_estimators = params.n_estimators,
            random_state = params.random_state
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.RandomForestRegressor
        schema = self.schema.TARGET

        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            X_test_transformed_path = config.X_test_transformed_path,
            y_test_path = config.y_test_path,
            model_path = config.model_path,
            metric_file = config.metric_file,
            target_column = schema.name,
            all_params = params,
            mlflow_uri = "https://dagshub.com/CodeWithCharan/Diamond-Price-Prediction.mlflow"
        )

        return model_evaluation_config