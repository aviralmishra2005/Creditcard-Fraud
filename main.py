import streamlit as st
import pandas as pd
import joblib

pipeline = joblib.load("model.joblib")

st.title("Credit Card Fraud Detection")

st.write("""
Upload a CSV file with transactions to detect potential frauds.  
The CSV should have columns like TransactionID, TransactionDate, Amount, MerchantID, TransactionType, Location.
""")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    if 'TransactionDate' in df.columns:
        df['TransactionHour'] = pd.to_datetime(df['TransactionDate']).dt.hour

    df_features = df.drop(['TransactionID', 'TransactionDate', 'IsFraud'], axis=1, errors='ignore')

    preds = pipeline.predict(df_features)
    probs = pipeline.predict_proba(df_features)[:,1]

    results = df.copy()
    results['Prediction (1=Fraud)'] = preds
    results['Fraud Probability'] = probs

    st.subheader("Predictions")
    st.dataframe(results)
    st.download_button("Download Predictions", results.to_csv(index=False).encode('utf-8'), "predictions.csv")
