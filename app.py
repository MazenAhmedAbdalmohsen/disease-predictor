# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022
@author: siddhardhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', '0')
    with col2:
        Glucose = st.text_input('Glucose Level', '0')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value', '0')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value', '0')
    with col2:
        Insulin = st.text_input('Insulin Level', '0')
    with col3:
        BMI = st.text_input('BMI value', '0')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', '0')
    with col2:
        Age = st.text_input('Age of the Person', '0')
    
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict([[
                float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)
            ]])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        except ValueError:
            diab_diagnosis = 'Please enter valid numerical values'
        
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age', '0')
    with col2:
        sex = st.text_input('Sex', '0')
    with col3:
        cp = st.text_input('Chest Pain types', '0')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', '0')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', '0')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', '0')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', '0')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', '0')
    with col3:
        exang = st.text_input('Exercise Induced Angina', '0')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', '0')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', '0')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy', '0')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', '0')
    
    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        try:
            heart_prediction = heart_disease_model.predict([[
                float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
                float(ca), float(thal)
            ]])
            heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        except ValueError:
            heart_diagnosis = 'Please enter valid numerical values'
        
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', '0')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', '0')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', '0')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', '0')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', '0')
    with col1:
        RAP = st.text_input('MDVP:RAP', '0')
    with col2:
        PPQ = st.text_input('MDVP:PPQ', '0')
    with col3:
        DDP = st.text_input('Jitter:DDP', '0')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer', '0')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', '0')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3', '0')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5', '0')
    with col3:
        APQ = st.text_input('MDVP:APQ', '0')
    with col4:
        DDA = st.text_input('Shimmer:DDA', '0')
    with col5:
        NHR = st.text_input('NHR', '0')
    with col1:
        HNR = st.text_input('HNR', '0')
    with col2:
        RPDE = st.text_input('RPDE', '0')
    with col3:
        DFA = st.text_input('DFA', '0')
    with col4:
        spread1 = st.text_input('spread1', '0')
    with col5:
        spread2 = st.text_input('spread2', '0')
    with col1:
        D2 = st.text_input('D2', '0')
    with col2:
        PPE = st.text_input('PPE', '0')
    
    parkinsons_diagnosis = ''
    
    if st.button("Parkinson's Test Result"):
        try:
            parkinsons_prediction = parkinsons_model.predict([[
                float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
                float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR),
                float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)
            ]])
            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        except ValueError:
            parkinsons_diagnosis = 'Please enter valid numerical values'
        
    st.success(parkinsons_diagnosis)