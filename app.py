import streamlit as st
import pandas as pd
import joblib
import os

st.title("Heart Disease Prediction App")

# Load model
model_path = os.path.join("models","heart_model.pkl")
clf = joblib.load(model_path)

# Load feature columns used during training
feature_cols_path = os.path.join("models","feature_columns.pkl")
feature_columns = joblib.load(feature_cols_path)

# --- User Inputs ---
age = st.number_input("Age", 1, 120, 50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", ["asymptomatic","non-anginal","atypical angina","typical angina"])
trestbps = st.number_input("Resting BP",50,250,120)
chol = st.number_input("Cholesterol",100,600,200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes","No"])
restecg = st.selectbox("Resting ECG", ["normal","ST-T wave abnormality","left ventricular hypertrophy"])
thalach = st.number_input("Max Heart Rate",50,250,150)
exang = st.selectbox("Exercise Induced Angina", ["Yes","No"])
oldpeak = st.number_input("ST Depression",0.0,10.0,1.0,0.1)
slope = st.selectbox("Slope", ["upsloping","flat","downsloping"])
thal = st.selectbox("Thalassemia", ["normal","fixed defect","reversible defect"])

# --- Encode binary/ordinal ---
sex = 1 if sex=="Male" else 0
fbs = 1 if fbs=="Yes" else 0
exang = 1 if exang=="Yes" else 0
cp_map = {'asymptomatic':0,'non-anginal':1,'atypical angina':2,'typical angina':3}
cp = cp_map[cp]

# --- Build input DataFrame ---
input_df = pd.DataFrame({
    'age':[age],
    'trestbps':[trestbps],
    'chol':[chol],
    'thalach':[thalach],
    'oldpeak':[oldpeak],
    'sex':[sex],
    'cp':[cp],
    'fbs':[fbs],
    'exang':[exang],
    'restecg':[restecg],
    'slope':[slope],
    'thal':[thal]
})

# --- Add missing columns with 0 ---
for col in feature_columns:
    if col not in input_df.columns:
        input_df[col] = 0

# --- Reorder columns to match training ---
input_df = input_df[feature_columns]

# --- Predict ---
if st.button("Predict"):
    pred = clf.predict(input_df)[0]
    prob = clf.predict_proba(input_df)[0][1]
    if pred == 1:
        st.error(f"⚠️ Patient HAS heart disease (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Patient does NOT have heart disease (Probability: {prob:.2f})")
