# ANN-Classification
🎯 Model Info The model is a Neural Network trained on 10,000 customer records.  Target: Exited column (1 = churned, 0 = retained)  Training dataset includes features like Credit Score, Age, Geography, etc.
# 🧠 Customer Churn Prediction Web App (Streamlit + TensorFlow)

This project is a **Customer Churn Prediction** app built with **Streamlit**, **TensorFlow**, and **scikit-learn**. It predicts the likelihood of a customer leaving (churning) based on input data such as geography, age, balance, salary, etc.

---

## 🚀 Demo

<img src="https://img.shields.io/badge/Status-Live-green" alt="Live Demo Badge" />  
You can run this app locally using Streamlit. See instructions below.

---

## 📦 Features

- ✅ User-friendly web interface via Streamlit  
- ✅ Predicts churn probability using a trained **Artificial Neural Network (ANN)**
- ✅ Encodes categorical features (`Gender`, `Geography`) using LabelEncoder & OneHotEncoder
- ✅ Scales numeric features using `StandardScaler`
- ✅ Provides churn probability as output

---

## 🧰 Tech Stack

- **Frontend**: Streamlit  
- **Backend/ML**: TensorFlow (Keras), scikit-learn  
- **Model**: ANN (trained and saved as `model.h5`)  
- **Encoders & Scaler**: Serialized using `pickle`

---

## 📁 Project Structure

