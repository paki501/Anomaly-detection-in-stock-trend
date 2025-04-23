import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

def calculate_indicators(df):
    df['SMA_20'] = df['Adj Close**'].rolling(window=20).mean()
    df['EMA_20'] = df['Adj Close**'].ewm(span=20).mean()
    delta = df['Adj Close**'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    df['BB_upper'] = df['SMA_20'] + 2 * df['Adj Close**'].rolling(window=20).std()
    df['BB_lower'] = df['SMA_20'] - 2 * df['Adj Close**'].rolling(window=20).std()
    df.dropna(inplace=True)
    return df

def detect_anomalies(df):
    iso_model = IsolationForest(contamination=0.01, random_state=42)
    df['anomaly_iforest'] = iso_model.fit_predict(df[['Adj Close**', 'SMA_20', 'RSI']])

    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[['Adj Close**', 'SMA_20', 'RSI']])
    dbscan = DBSCAN(eps=1.5, min_samples=5)
    df['anomaly_dbscan'] = dbscan.fit_predict(scaled)

    return df
