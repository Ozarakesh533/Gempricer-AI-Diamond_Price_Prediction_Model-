import os
import joblib
from mlProject import logger
import pandas as pd
from sklearn.model_selection import train_test_split
# for numerical data
from sklearn.preprocessing import StandardScaler
# for categorical data
from sklearn.preprocessing import OrdinalEncoder
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # outlier handling method
    def remove_outliers(self):
        df = pd.read_csv(self.config.data_path)

        # acc to experiments, these are the outliers
        df = df.loc[df['x'] > 3]
        df = df.loc[df['y'] < 15]
        df = df.loc[df['z'] < 10]
        df = df.loc[df['z'] > 2]

        return df
    
    # Segregate method
    def data_segregation(self):
        df = self.remove_outliers()

        # inputs (x)
        X = df.drop([self.config.target_column], axis=1)

        # output (y), squeezing it to ensure 1D Series
        y = df[self.config.target_column].squeeze()

        return X, y
    
    # train test split method
    def get_train_test_split(self):
        X, y = self.data_segregation()

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

        return X_train, X_test, y_train, y_test
    
    # Transformation method
    def get_transformed(self):
        X_train, X_test, y_train, y_test = self.get_train_test_split()

        # diamond quality, low to high (ordinals)
        cut_categories = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
        color_categories = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
        clarity_categories = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
        
        # adjust Scaler and Encoder
        std_scaler = StandardScaler()
        ordinal_encoder = OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories],  
                                 handle_unknown="use_encoded_value",
                                 unknown_value=-1, 
                                 encoded_missing_value=-5)
        
        # train transformation
        X_train_num = X_train.select_dtypes(include=['int64', 'float64'])
        X_train_cat = X_train.select_dtypes(include=['object'])

        X_train_num_transformed = pd.DataFrame(std_scaler.fit_transform(X_train_num),
                                      columns = std_scaler.get_feature_names_out(),
                                      index = X_train_num.index)
        
        X_train_cat_transformed = pd.DataFrame(ordinal_encoder.fit_transform(X_train_cat),
                                      columns = ordinal_encoder.get_feature_names_out(),
                                      index = X_train_cat.index)
        
        # Concatenate
        X_train_transformed = pd.concat([X_train_num_transformed, X_train_cat_transformed], axis=1)

        # test transformation
        X_test_num = X_test.select_dtypes(include=['int64', 'float64'])
        X_test_cat = X_test.select_dtypes(include=['object'])

        X_test_num_transformed = pd.DataFrame(std_scaler.transform(X_test_num), 
                                   columns = std_scaler.get_feature_names_out(), 
                                   index = X_test_num.index)

        X_test_cat_transformed = pd.DataFrame(ordinal_encoder.transform(X_test_cat), 
                                   columns = ordinal_encoder.get_feature_names_out(), 
                                   index = X_test_cat.index)
        
        # Concatenate
        X_test_transformed = pd.concat([X_test_num_transformed, X_test_cat_transformed], axis=1)

        # save csv
        X_train_transformed.to_csv(os.path.join(self.config.root_dir, "X_train_transformed.csv"), index=False)
        y_train.to_csv(os.path.join(self.config.root_dir, "y_train.csv"), index=False)

        X_test_transformed.to_csv(os.path.join(self.config.root_dir, "X_test_transformed.csv"), index=False)
        y_test.to_csv(os.path.join(self.config.root_dir, "y_test.csv"), index=False)

        # Save the fitted scaler and encoder for future use (e.g., during prediction)
        joblib.dump(std_scaler, os.path.join(self.config.root_dir, 'scaler.pkl'))
        joblib.dump(ordinal_encoder, os.path.join(self.config.root_dir, 'encoder.pkl'))

        logger.info(f"X train transformed size: {X_train_transformed.shape}, y train size:{y_train.shape}")
        logger.info(f"X test transformed size: {X_test_transformed.shape}, y test size: {y_test.shape}")