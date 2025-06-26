import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

@st.cache_data
def load_data():
    return pd.read_csv("diabetes.csv")

@st.cache_resource
def train_model(data):
    X = data.drop("Outcome", axis=1)
    y = data["Outcome"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    return model, scaler

def main():
    st.title("🩺 تطبيق التنبؤ بمرض السكري باستخدام Logistic Regression")

    st.write("أدخل البيانات التالية:")
    pregnancies = st.number_input("عدد مرات الحمل", 0, 20, 1)
    glucose = st.number_input("مستوى الجلوكوز", 0, 200, 100)
    blood_pressure = st.number_input("ضغط الدم", 0, 150, 70)
    skin_thickness = st.number_input("سمك الجلد", 0, 100, 20)
    insulin = st.number_input("مستوى الأنسولين", 0, 900, 80)
    bmi = st.number_input("مؤشر كتلة الجسم", 0.0, 70.0, 25.0)
    dpf = st.number_input("عامل الوراثة (DPF)", 0.0, 3.0, 0.5)
    age = st.number_input("العمر", 1, 120, 30)

    data = load_data()
    model, scaler = train_model(data)

    if st.button("توقع"):
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)

        if prediction[0] == 1:
            st.error("⚠ من المرجح أنك مصاب بمرض السكري.")
        else:
            st.success("✅ من غير المرجح أنك مصاب بمرض السكري.")

if __name__ == "__main__":
    main()