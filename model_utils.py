import joblib
import numpy as np
import pandas as pd

scaler = joblib.load("saved_models/scaler.pkl")
iso_forest = joblib.load("saved_models/iso_forest.pkl")
dbscan = joblib.load("saved_models/dbscan.pkl")
ocsvm = joblib.load("saved_models/ocsvm.pkl")
label_encoder = joblib.load("saved_models/label_encoder.pkl")

def predict_ensemble(input_df):
    # Feature engineering like hour, day, weekend...
    input_df['Hour'] = input_df['TransactionDate'].dt.hour
    input_df['DayOfWeek'] = input_df['TransactionDate'].dt.dayofweek
    input_df['Weekend'] = input_df['DayOfWeek'].apply(lambda x: 1 if x >= 5 else 0)
    input_df['Month'] = input_df['TransactionDate'].dt.month
    
    avg_tx_amount = input_df.groupby('TransactionType')['TransactionAmount'].transform('mean')
    input_df['Amount_to_AvgByType_Ratio'] = input_df['TransactionAmount'] / avg_tx_amount

    # Label encode
    for col in input_df.select_dtypes(include=['object']).columns:
        input_df[col] = label_encoder.fit_transform(input_df[col])

    # Scale
    scaled = scaler.transform(input_df)

    # Predict using models
    pred_if = iso_forest.predict(scaled)
    pred_db = dbscan.fit_predict(scaled)
    pred_oc = ocsvm.predict(scaled)

    pred_if = np.where(pred_if == -1, 1, 0)
    pred_db = np.where(pred_db == -1, 1, 0)
    pred_oc = np.where(pred_oc == -1, 1, 0)

    # Ensemble (majority vote)
    ensemble = (pred_if + pred_db + pred_oc >= 2).astype(int)
    return ensemble[0], pred_if[0], pred_db[0], pred_oc[0]
