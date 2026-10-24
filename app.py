
import streamlit as st
import pandas as pd
from pathlib import Path
import joblib

st.set_page_config(
    page_title="AI Voltage Prediction",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ AI-Based Overvoltage and Undervoltage Prediction System")
st.write("Machine learning-based voltage condition prediction demo.")

data_path = Path("data/voltage_data.csv")
model_path = Path("models/voltage_model.pkl")

st.subheader("Voltage Prediction")

voltage = st.number_input(
    "Enter voltage value (V)",
    min_value=0.0,
    max_value=500.0,
    value=230.0,
    step=1.0
)

if st.button("Predict Voltage Status"):
    if voltage < 207:
        st.error("Undervoltage Detected")
    elif voltage > 253:
        st.error("Overvoltage Detected")
    else:
        st.success("Normal Voltage")

st.divider()
st.subheader("Dataset Preview")

if data_path.exists():
    df = pd.read_csv(data_path)
    st.write(f"Dataset rows: {len(df)}")
    st.dataframe(df.head(10), use_container_width=True)
else:
    st.warning("Dataset not found. Check data/voltage_data.csv.")

st.caption(
    "Educational demo using illustrative voltage thresholds. "
    "Not certified for real electrical protection."
)
