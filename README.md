# 💳 Credit Card Fraud Detection

This project applies **Machine Learning algorithms** to detect fraudulent credit card transactions.  
An interactive interface is built using **Streamlit** for easy experimentation.

---

## 📊 Dataset
- **Source**: Credit Card Fraud Detection Dataset (Kaggle)  
- **Description**:
  - Features `V1...V28` are obtained using **PCA** for confidentiality.
  - `Amount` represents the transaction value.
  - Target column `Class`:
    - `0` → Normal transaction
    - `1` → Fraudulent transaction

---

## 🧠 Model
- Algorithm: **Random Forest Classifier**
- Number of trees: `100`
- Class imbalance handled using:
  - `class_weight="balanced"`
  - or **SMOTE** oversampling

---

## 🖥️ Application
- A **Streamlit app** allows interactive testing of the model.
- Users can input feature values (`V1...V28 + Amount`) and get predictions:
  - ✅ Normal transaction  
  - ⚠️ Fraudulent transaction  

---

## 📌 Notes
- Performance is evaluated using metrics such as:
  - Precision  
  - Recall  
  - F1-score  
  - ROC-AUC  
- Possible improvements:
  - Deep Learning models (Neural Networks, Autoencoders)  
  - More advanced algorithms (XGBoost, LightGBM)  
  - Deployment on **Streamlit Cloud** or **Hugging Face Spaces**  

---
**Data Science & Machine Learning**.
