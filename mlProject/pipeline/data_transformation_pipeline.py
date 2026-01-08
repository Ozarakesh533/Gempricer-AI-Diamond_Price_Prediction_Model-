from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)

        data_transformation.remove_outliers()
        data_transformation.data_segregation()
        data_transformation.get_train_test_split()
        data_transformation.get_transformed()