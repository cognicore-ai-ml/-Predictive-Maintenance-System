import joblib
import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from src.preprocess import calculate_rul, engineer_features

def run_training_pipeline(train_path):
    # Load production data stream
    df = pd.read_csv(train_path)
    df = calculate_rul(df)
    
    processed_df, scaler = engineer_features(df, is_training=True)
    
    features = [f'sensor_{i}' for i in range(1, 22)]
    X = processed_df[features]
    y = processed_df['RUL']
    
    model = XGBRegressor(n_estimators=100, max_depth=5, learning_rate=0.05)
    model.fit(X, y)
    
    # Serialize models to local artifact directory
    joblib.dump(model, 'models/predictive_model.pkl')
    joblib.dump(scaler, 'models/feature_scaler.pkl')
    print("Model training complete. Check /models directory.")
  
