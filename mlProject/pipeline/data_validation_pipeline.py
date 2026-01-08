from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValiadtion

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)

        data_validation.validate_all_columns()