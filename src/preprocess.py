import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def calculate_rul(df):
    # Compute remaining useful life sequence mapping per engine ID
    max_cycles = df.groupby('engine_id')['cycle'].transform('max')
    df['RUL'] = max_cycles - df['cycle']
    return df

def engineer_features(df, scaler=None, is_training=True):
    feature_cols = [f'sensor_{i}' for i in range(1, 22)]
    
    if is_training:
        scaler = StandardScaler()
        df[feature_cols] = scaler.fit_transform(df[feature_cols])
        return df, scaler
    else:
        df[feature_cols] = scaler.transform(df[feature_cols])
        return df
      
