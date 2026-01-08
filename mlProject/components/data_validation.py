import os
from mlProject import logger
import pandas as pd

from mlProject.entity.config_entity import DataValidationConfig

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            # status
            validation_status = True # assume

            # read csv file
            data = pd.read_csv(self.config.unzip_data_dir)

            # save columns in a list
            all_cols = list(data.columns)

            # schema columns
            all_schema = self.config.all_schema

            for col in all_cols:
                # Check if column exists
                if col not in all_schema:
                    validation_status = False
                    logger.info(f"Column '{col}' is missing")
                    break
                
                # Check if data type matches the schema
                elif str(data[col].dtype) != all_schema[col]:
                    validation_status = False
                    logger.info(f"Data type mismatch. Column: {col}\nExpected: {all_schema[col]}, Got: {data[col].dtype}")
                    break
            
            # Save the validation result
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation Status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e