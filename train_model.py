import os
import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from pathlib import Path

# Create necessary directories
artifacts_dir = "artifacts"
model_dir = os.path.join(artifacts_dir, "model_trainer")
transform_dir = os.path.join(artifacts_dir, "data_transformation")
os.makedirs(model_dir, exist_ok=True)
os.makedirs(transform_dir, exist_ok=True)

# Load the data
data_path = os.path.join("artifacts", "data_ingestion", "diamonds.csv")
df = pd.read_csv(data_path)

# Define features and target
X = df.drop(['price'], axis=1)
y = df['price']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the test data for later use
X_test.to_csv(os.path.join(transform_dir, "X_test.csv"), index=False)
y_test.to_csv(os.path.join(transform_dir, "y_test.csv"), index=False)

# Define categorical and numerical columns
categorical_cols = ['cut', 'color', 'clarity']
numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']

# Initialize transformers
scaler = StandardScaler()
encoder = OrdinalEncoder(categories=[
    ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'],  # cut
    ['J', 'I', 'H', 'G', 'F', 'E', 'D'],  # color
    ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']  # clarity
])

# Apply transformations
X_train_num = X_train[numerical_cols]
X_train_cat = X_train[categorical_cols]

X_test_num = X_test[numerical_cols]
X_test_cat = X_test[categorical_cols]

# Fit and transform the data
X_train_num_scaled = scaler.fit_transform(X_train_num)
X_train_cat_encoded = encoder.fit_transform(X_train_cat)

# Transform test data
X_test_num_scaled = scaler.transform(X_test_num)
X_test_cat_encoded = encoder.transform(X_test_cat)

# Combine numerical and categorical features
X_train_processed = np.hstack((X_train_num_scaled, X_train_cat_encoded))
X_test_processed = np.hstack((X_test_num_scaled, X_test_cat_encoded))

# Save the transformed data
pd.DataFrame(X_train_processed).to_csv(os.path.join(transform_dir, "X_train_transformed.csv"), index=False)
pd.DataFrame(X_test_processed).to_csv(os.path.join(transform_dir, "X_test_transformed.csv"), index=False)
y_train.to_csv(os.path.join(transform_dir, "y_train.csv"), index=False)
y_test.to_csv(os.path.join(transform_dir, "y_test.csv"), index=False)

# Save the transformers
joblib.dump(scaler, os.path.join(transform_dir, "scaler.pkl"))
joblib.dump(encoder, os.path.join(transform_dir, "encoder.pkl"))

# Train the model
print("Training the model...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_processed, y_train)

# Save the model
model_path = os.path.join(model_dir, "model.joblib")
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")

# Print model performance
train_score = model.score(X_train_processed, y_train)
test_score = model.score(X_test_processed, y_test)
print(f"Training R² score: {train_score:.4f}")
print(f"Testing R² score: {test_score:.4f}")

print("\nModel training and data transformation completed successfully!")
