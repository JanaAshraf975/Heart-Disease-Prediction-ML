# Heart-Disease-Prediction-ML
Predict heart disease using ML models with full preprocessing, evaluation, and feature importance analysis.
# Heart Disease Prediction App

This is a **Machine Learning project** that predicts whether a patient has heart disease or not using the **Heart Disease UCI dataset**. The project includes a trained model and a **Streamlit web app** for interactive predictions.

---

## 🧰 Features

- Predicts the presence of heart disease based on patient health metrics.
- Uses a **Random Forest Classifier** with preprocessing (scaling and one-hot encoding) inside a **Pipeline**.
- Handles **binary, ordinal, and categorical features** correctly.
- Streamlit app for **easy, interactive predictions**.

---

## 💾 Dataset

The dataset used is the [Heart Disease UCI dataset](https://www.kaggle.com/datasets/cherngs/heart-disease-uci) from Kaggle. It includes features such as:

- Age
- Sex
- Chest pain type (CP)
- Resting blood pressure (trestbps)
- Cholesterol (chol)
- Fasting blood sugar (fbs)
- Resting ECG results (restecg)
- Maximum heart rate achieved (thalach)
- Exercise induced angina (exang)
- ST depression (oldpeak)
- Slope of ST segment (slope)
- Thalassemia (thal)

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Heart-Disease-Prediction-ML.git
cd Heart-Disease-Prediction-ML

``` 
2. Install dependencies:

```
pip install -r requirements.txt

```
3. Run the Streamlit App🚀
   
```
streamlit run app.py
```

5. Enter the patient data in the input fields.

6. Click Predict to see if the patient has heart disease and the prediction probability.


## 🗂 Project Structure

bash
Copy
Edit
Heart-Disease-Prediction-ML/
│
├─ app.py                     # Streamlit application
├─ data/
│   └─ heart_disease_uci.csv  # Dataset
├─ models/
│   ├─ heart_model.pkl         # Trained ML model pipeline
│   └─ feature_columns.pkl    # Feature columns used in training
├─ train_pipeline.ipynb       # Notebook for training the model
├─ requirements.txt           # Project libraries
├─ README.md                 # Project description

## 📈 Model Performance
The trained model achieves high accuracy and AUC on the test set.
Uses Random Forest Classifier for robust predictions.

## 🔄 Retraining the Model

Open notebooks/train_pipeline.ipynb.

Preprocess the dataset.

Train the Random Forest pipeline.

Save heart_model.pkl and feature_columns.pkl in the models/ folder.

## ⚡ Notes
Make sure the models folder contains both heart_model.pkl and feature_columns.pkl.

The app handles unseen categorical values using One-Hot Encoder with handle_unknown='ignore'.

## 📫 Author
Jana Ashraf Salah Eldin
Email: ganashraf79@gmail.com

git clone https://github.com/your-username/Heart-Disease-Prediction-ML.git
cd Heart-Disease-Prediction-ML
