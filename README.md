# ❤️ Heart Disease Prediction Web App

A machine learning–based web application that predicts the risk of heart disease using patient medical data.  
The application is built with **Streamlit** and uses a **Logistic Regression** model for prediction.

---

## 🌐 Live Application

🔗 **Deployed App:**  
https://heart-disease-app-bpalffvqzj8edbseijd58v.streamlit.app

---

## 📌 Project Description

Heart disease is one of the leading causes of death worldwide.  
This project aims to predict the **risk of heart disease** based on various medical parameters provided by the user.

The model outputs:
- ✅ Low Risk of Heart Disease  
- ⚠️ High Risk of Heart Disease  

along with a **probability score** for better interpretation.

---

## 🧠 Machine Learning Model

- **Algorithm:** Logistic Regression  
- **Why Logistic Regression?**
  - Well-suited for binary classification
  - Interpretable results (important for medical applications)
- **Preprocessing Techniques:**
  - One-hot encoding for categorical variables
  - Feature scaling using `StandardScaler`
- **Class Imbalance Handling:** `class_weight="balanced"`
- **Decision Threshold:** 0.4

---

## 🧾 Input Features

The following patient attributes are used for prediction:

- Age  
- Resting Blood Pressure  
- Cholesterol  
- Fasting Blood Sugar  
- Maximum Heart Rate  
- Oldpeak (ST depression)  
- Sex  
- Chest Pain Type  
- Resting ECG  
- Exercise Induced Angina  
- ST Slope  

---

## 🖥️ Web Application

The Streamlit web interface allows users to:
- Enter patient health details
- Get real-time heart disease risk prediction
- View probability score for better understanding

---

## 🧪 Example Test Inputs

### ✅ Low-Risk Sample Input
Use the following values to test a low-risk prediction:

- Age: 30  
- Resting Blood Pressure: 100  
- Cholesterol: 160  
- Fasting Blood Sugar: 0  
- Maximum Heart Rate: 170  
- Oldpeak: 0.5  
- Sex: F  
- Chest Pain Type: ATA  
- Resting ECG: Normal  
- Exercise Induced Angina: N  
- ST Slope: Up  

**Expected Output:**  
✅ Low risk of heart disease

---

### ⚠️ High-Risk Sample Input
Use the following values to test a high-risk prediction:

- Age: 76  
- Resting Blood Pressure: 190  
- Cholesterol: 520  
- Fasting Blood Sugar: 1  
- Maximum Heart Rate: 85  
- Oldpeak: 5.8  
- Sex: M  
- Chest Pain Type: ASY  
- Resting ECG: ST  
- Exercise Induced Angina: Y  
- ST Slope: Flat  

**Expected Output:**  
⚠️ High risk of heart disease

---

## 📈 Model Output Explanation

The model returns a **probability score** between 0 and 1.

- Probability **< 0.4** → Low risk of heart disease  
- Probability **≥ 0.4** → High risk of heart disease  

A lower threshold is used to improve sensitivity, which is important for medical risk prediction.

---

## ⚠️ Disclaimer

This application is developed **for educational purposes only**.  
It is not intended to replace professional medical diagnosis or treatment.
