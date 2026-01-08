import os
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from mlProject import logger

class PredictionPipeline:
    def __init__(self):
        try:
            # Define base paths
            base_dir = os.path.join(os.getcwd(), 'artifacts')
            model_path = os.path.join(base_dir, 'model_trainer', 'model.joblib')
            scaler_path = os.path.join(base_dir, 'data_transformation', 'scaler.pkl')
            encoder_path = os.path.join(base_dir, 'data_transformation', 'encoder.pkl')
            
            # Check if files exist
            for path in [model_path, scaler_path, encoder_path]:
                if not os.path.exists(path):
                    raise FileNotFoundError(f"Required file not found: {path}")
            
            # Load artifacts
            self.model = joblib.load(model_path)
            self.scaler = joblib.load(scaler_path)
            self.encoder = joblib.load(encoder_path)
            
            logger.info("Successfully loaded all model artifacts")
            
        except Exception as e:
            logger.error(f"Error initializing PredictionPipeline: {str(e)}")
            raise

    def data_transform(self, data):
        try:
            logger.info("Starting data transformation")
            
            # Define expected columns
            numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']
            categorical_cols = ['cut', 'color', 'clarity']
            
            # Check if all required columns are present
            missing_cols = [col for col in numerical_cols + categorical_cols 
                          if col not in data.columns]
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")

            # Apply scaler to numerical columns
            num_data = data[numerical_cols].copy()
            num_data_transformed = pd.DataFrame(
                self.scaler.transform(num_data),
                columns=numerical_cols,
                index=data.index
            )
            
            # Encode categorical variables
            cat_data = data[categorical_cols].copy()
            
            try:
                # Try to transform and handle different encoder output types
                cat_encoded = self.encoder.transform(cat_data)
                
                # Handle different types of encoder outputs
                if hasattr(cat_encoded, 'toarray'):
                    # Sparse matrix (from OneHotEncoder)
                    cat_data_encoded = cat_encoded.toarray()
                elif isinstance(cat_encoded, np.ndarray):
                    # Already a numpy array (from LabelEncoder or OrdinalEncoder)
                    cat_data_encoded = cat_encoded
                else:
                    # Convert to numpy array
                    cat_data_encoded = np.array(cat_encoded)
                
                # Ensure it's 2D for concatenation
                if cat_data_encoded.ndim == 1:
                    cat_data_encoded = cat_data_encoded.reshape(-1, 1)
                    
            except Exception as e:
                logger.error(f"Error encoding categorical data: {str(e)}")
                raise
            
            # Combine numerical and categorical features
            X_transformed = np.hstack([num_data_transformed.values, cat_data_encoded])
            
            logger.info(f"Data transformation completed. Shape: {X_transformed.shape}")
            return X_transformed
            
        except Exception as e:
            logger.error(f"Error in data transformation: {str(e)}")
            raise

    def predict(self, X):
        try:
            logger.info("Making prediction")
            
            # Make predictions
            predictions = self.model.predict(X)
            
            logger.info(f"Prediction completed. Result: {predictions}")
            return predictions
            
        except Exception as e:
            logger.error(f"Error making predictions: {str(e)}")
            raise