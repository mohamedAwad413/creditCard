import streamlit as st
import pandas as pd
import pickle

# تحميل الموديل
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Credit Card Fraud Detection")

# إدخال البيانات من المستخدم
Time = st.number_input("Time")
V1 = st.number_input("V1")
V2 = st.number_input("V2")
V3 = st.number_input("V3")
V4 = st.number_input("V4")
V5 = st.number_input("V5")
V6 = st.number_input("V6")
V7 = st.number_input("V7")
V8 = st.number_input("V8")
V9 = st.number_input("V9")
V10 = st.number_input("V10")
V11 = st.number_input("V11")
V12 = st.number_input("V12")
V13 = st.number_input("V13")
V14 = st.number_input("V14")
V15 = st.number_input("V15")
V16 = st.number_input("V16")
V17 = st.number_input("V17")
V18 = st.number_input("V18")
V19 = st.number_input("V19")
V20 = st.number_input("V20")
V21 = st.number_input("V21")
V22 = st.number_input("V22")
V23 = st.number_input("V23")
V24 = st.number_input("V24")
V25 = st.number_input("V25")
V26 = st.number_input("V26")
V27 = st.number_input("V27")
V28 = st.number_input("V28")
Amount = st.number_input("Amount")

if st.button("Predict"):
    # تجهيز الداتا (لازم نفس الترتيب اللي اتدرب عليه الموديل)
    input_data = pd.DataFrame([[Time, V1, V2, V3,V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23,
                                V24, V25, V26, V27, V28, Amount]], 
                              columns=["Time", "V1", "V2", "V3","V4", "V5","V6", "V7", "V8", "V9", "V10", "V11", "V12", "V13", 'V14', "V15", "V16", "V17",
                                        "V18", "V19", "V20", "V21", "V22", "V23",'V24', 'V25', 'V26', 'V27', 'V28', "Amount"])
    
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ Fraud Transaction Detected!")
    else:
        st.success("✅ Normal Transaction")
