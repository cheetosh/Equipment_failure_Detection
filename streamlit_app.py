import streamlit as st
import joblib
import numpy as np

model = joblib.load("models/equip_failure_rf.joblib")
st.title("Equipment Failure Prediction App")

inputs = []
cols = ["temp_mean","temp_std","temp_max","vib_mean","vib_std","vib_max",
        "press_mean","press_std","rpm_mean","rpm_std","hours_running"]

for col in cols:
    value = st.number_input(col, value=1.0)
    inputs.append(value)

if st.button("Predict"):
    inputs = np.array([inputs])
    prob = model.predict_proba(inputs)[0][1]
    pred = int(prob > 0.5)

    st.write("Failure Probability:", round(prob,3))
    st.success("⚠️ Failure Expected" if pred==1 else "✅ Machine Healthy")
