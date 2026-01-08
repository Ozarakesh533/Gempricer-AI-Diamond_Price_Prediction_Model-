from dataclasses import dataclass
from pathlib import Path

# Data Ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

# Data Validation
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: Path
    all_schema: dict

# Data Transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    target_column: str

# Model Trainer
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    X_train_transformed_path: Path
    y_train_path: Path
    model_name: str
    n_estimators: int
    random_state: int

# Model Evaluation
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    X_test_transformed_path: Path
    y_test_path: Path
    model_path: Path
    metric_file: str
    target_column: str
    all_params: dict
    mlflow_uri: str