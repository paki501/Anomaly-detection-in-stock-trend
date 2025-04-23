import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model_utils import calculate_indicators, detect_anomalies

st.set_page_config(layout="wide", page_title="📈 Stock Anomaly Detector")

st.title("📊 Stock Price Anomaly Detection Tool")
st.markdown("Upload Yahoo Finance historical data to detect unusual price activity.")

uploaded_file = st.file_uploader("Upload CSV or Excel File", type=['csv', 'xlsx'])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values('Date', inplace=True)

    with st.spinner("Calculating technical indicators..."):
        df = calculate_indicators(df)
        df = detect_anomalies(df)

    st.success("Analysis Complete! See results below 👇")

    # Line chart
    st.subheader("📈 Adjusted Close Price with Anomalies")
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df['Date'], df['Adj Close**'], label='Adj Close', color='blue')
    ax.scatter(df[df['anomaly_iforest'] == -1]['Date'],
               df[df['anomaly_iforest'] == -1]['Adj Close**'],
               color='red', label='Anomaly (Isolation Forest)')
    ax.set_title("Price with Anomalies")
    ax.legend()
    st.pyplot(fig)

    # Show table of anomalies
    st.subheader("🚨 Detected Anomalies (Isolation Forest)")
    st.dataframe(df[df['anomaly_iforest'] == -1][['Date', 'Adj Close**']].tail(10))

    # Optional: Save results
    st.download_button("📥 Download Results", data=df.to_csv(index=False).encode(),
                       file_name="anomaly_results.csv", mime="text/csv")

