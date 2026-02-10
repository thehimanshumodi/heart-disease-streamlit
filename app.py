import streamlit as st
import pandas as pd
import joblib


# Load trained artifacts
model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("columns.pkl")  # MUST be 15 features


# Streamlit UI
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️")
st.title("❤️ Heart Disease Prediction")
st.write("Enter patient details to assess heart disease risk.")

# User Inputs
age = st.slider("Age", 18, 100, 45)
resting_bp = st.number_input("Resting Blood Pressure", 80, 200, 120)
cholesterol = st.number_input("Cholesterol", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
max_hr = st.number_input("Maximum Heart Rate", 60, 220, 150)
oldpeak = st.slider("Oldpeak (ST depression)", 0.0, 6.0, 1.0)

sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
rest_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
exercise_angina = st.selectbox("Exercise Induced Angina", ["Y", "N"])
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])


# Prediction
if st.button("Predict"):
    # Create empty input dataframe with EXACT training columns
    input_df = pd.DataFrame(0, index=[0], columns=feature_columns)

    # Numerical features
    input_df["Age"] = age
    input_df["RestingBP"] = resting_bp
    input_df["Cholesterol"] = cholesterol
    input_df["FastingBS"] = fasting_bs
    input_df["MaxHR"] = max_hr
    input_df["Oldpeak"] = oldpeak

    # Categorical → One-hot encoding (MATCH TRAINING)
    if sex == "M":
        input_df["Sex_M"] = 1

    if chest_pain == "ATA":
        input_df["ChestPainType_ATA"] = 1
    elif chest_pain == "NAP":
        input_df["ChestPainType_NAP"] = 1
    elif chest_pain == "TA":
        input_df["ChestPainType_TA"] = 1
    # ASY = baseline (all zeros)

    if rest_ecg == "Normal":
        input_df["RestingECG_Normal"] = 1
    elif rest_ecg == "ST":
        input_df["RestingECG_ST"] = 1
    # LVH = baseline

    if exercise_angina == "Y":
        input_df["ExerciseAngina_Y"] = 1

    if st_slope == "Flat":
        input_df["ST_Slope_Flat"] = 1
    elif st_slope == "Up":
        input_df["ST_Slope_Up"] = 1
    # Down = baseline

  
    # Scale & Predict
    scaled_input = scaler.transform(input_df.values)
    probability = model.predict_proba(scaled_input)[0][1]


    # Medical decision threshold
    if probability >= 0.4:
        st.error(
            f"⚠️ High risk of heart disease\n\n"
            f"Prediction probability: **{probability:.2f}**\n\n"
            f"Please consult a cardiologist."
        )
    else:
        st.success(
            f"✅ Low risk of heart disease\n\n"
            f"Prediction probability: **{probability:.2f}**\n\n"
            f"Maintain a healthy lifestyle."
        )