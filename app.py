{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "54d0a19c-d934-4232-a351-9318c0b43884",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-25 14:47:27.005 WARNING streamlit.runtime.state.session_state_proxy: Session state does not function when running a script without `streamlit run`\n",
      "2025-06-25 14:47:28.104 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\lenovo\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "pregnancies = st.number_input(\"عدد مرات الحمل\", min_value=0, max_value=20, value=1)\n",
    "glucose = st.number_input(\"مستوى الجلوكوز\", min_value=0, max_value=200, value=100)\n",
    "blood_pressure = st.number_input(\"ضغط الدم\", min_value=0, max_value=140, value=70)\n",
    "skin_thickness = st.number_input(\"سماكة الجلد\", min_value=0, max_value=100, value=20)\n",
    "insulin = st.number_input(\"مستوى الإنسولين\", min_value=0, max_value=900, value=80)\n",
    "bmi = st.number_input(\"مؤشر كتلة الجسم (BMI)\", min_value=0.0, max_value=70.0, value=25.0)\n",
    "dpf = st.number_input(\"عامل التاريخ العائلي للسكري\", min_value=0.0, max_value=2.5, value=0.5)\n",
    "age = st.number_input(\"العمر\", min_value=1, max_value=100, value=30)\n",
    "\n",
    "if st.button(\" تنبؤ\"):\n",
    "    user_dia = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])\n",
    "    prediction = model.predict(user_dia)\n",
    "\n",
    "    if prediction[0] == 1:\n",
    "        st.error(\" نتيجة التنبؤ: مصاب بالسكري.\")\n",
    "    else:\n",
    "        st.success(\"نتيجة التنبؤ: غير مصاب بالسكري.\")\n",
    "\n",
    "if st.checkbox(\"عرض بيانات التدريب\"):\n",
    "    st.write(dia.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3929c384-9f14-4156-81b5-f9bef9bcdc98",
   "metadata": {},
   "outputs": [],
   "source": []
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
