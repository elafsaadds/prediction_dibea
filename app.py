{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "1964f568-3454-4093-9a10-747e4db4fd4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import joblib  # أو pickle حسب طريقة الحفظ\n",
    "# تحميل النموذج\n",
    "model = joblib.load(\"model.pkl\")  # تأكد من اسم الملف\n",
    "\n",
    "# إدخالات المستخدم\n",
    "pregnancies = st.number_input(\"عدد مرات الحمل\", min_value=0, max_value=20, value=1)\n",
    "glucose = st.number_input(\"مستوى الجلوكوز\", min_value=0, max_value=200, value=100)\n",
    "blood_pressure = st.number_input(\"ضغط الدم\", min_value=0, max_value=140, value=70)\n",
    "skin_thickness = st.number_input(\"سماكة الجلد\", min_value=0, max_value=100, value=20)\n",
    "insulin = st.number_input(\"مستوى الإنسولين\", min_value=0, max_value=900, value=80)\n",
    "bmi = st.number_input(\"مؤشر كتلة الجسم (BMI)\", min_value=0.0, max_value=70.0, value=25.0)\n",
    "dpf = st.number_input(\"عامل التاريخ العائلي للسكري\", min_value=0.0, max_value=2.5, value=0.5)\n",
    "age = st.number_input(\"العمر\", min_value=1, max_value=100, value=30)\n",
    "\n",
    "# زر التنبؤ\n",
    "if st.button(\"تنبؤ\"):\n",
    "    user_dia = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])\n",
    "    prediction = model.predict(user_dia)\n",
    "    \n",
    "    if prediction[0] == 1:\n",
    "        st.error(\"نتيجة التنبؤ: مصاب بالسكري.\")\n",
    "    else:\n",
    "        st.success(\"نتيجة التنبؤ: غير مصاب بالسكري.\")\n",
    "\n",
    "# زر عرض البيانات\n",
    "if st.checkbox(\"عرض بيانات التدريب\"):\n",
    "    dia = pd.read_csv(\"diabetes.csv\")  # عدل المسار حسب ملف البيانات\n",
    "    st.write(dia.head())\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
