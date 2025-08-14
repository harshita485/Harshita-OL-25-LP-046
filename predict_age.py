import streamlit as st
import numpy as np
import joblib 
import pandas as pd
st.header("📊 Age Prediction")
st.subheader(".")
tech_company=st.selectbox("Do you work in a tech company?",["Yes","No"]),
gender = st.selectbox("Gender", ['Male', 'Female', 'Other', 'Not specified'])
self_employed = st.selectbox('Are you self-employed?', [ 'Yes', 'No'])
family_history = st.selectbox("Do you have a family history of mental illness?", ['Yes', 'No'])
treatment = st.selectbox('Have you sought treatment for a mental health condition?', ['Yes', 'No'])
work_interfere = st.selectbox('If you have a mental health condition, do you feel that it interferes with your work?',
                                  ['Often', 'Rarely', 'Never', 'Sometimes'])
remote_work = st.selectbox('Do you work remotely (outside of an office) at least 50% of the time?', ['Yes', 'No'])
benefits = st.selectbox('Does your employer provide mental health benefits?', ['unknown', 'Yes', 'No'])
care_options = st.selectbox('Do you know the options for mental health care your employer provides?',
                                ['unknown', 'No', 'Yes'])
wellness_program = st.selectbox('Has your employer ever discussed mental health as part of a wellness program?',
                                    ['unknown', 'Yes', 'No'])
seek_help = st.selectbox('Does your employer provide resources to learn about mental health and seeking help?',
                             ['Yes', 'No','unknown'])
leave = st.selectbox('How easy is it for you to take mental health leave?',
                         ['Very easy', 'Somewhat easy', 'Somewhat difficult', 'Very difficult', 'unknown'])
mental_health_consequence = st.selectbox('Would discussing mental health with your employer have negative consequences?',
                                             ['No', 'uncertain', 'Yes'])
coworkers = st.selectbox('Would you discuss a mental health issue with your coworkers?',
                             ['Some of them', 'No', 'Yes'])
mental_health_interview = st.selectbox('Would you bring up a mental health issue in an interview?',
                                           [ 'No', 'Yes','Maybe'])
supervisor = st.selectbox('Would you discuss a mental health issue with your supervisor(s)?',
                              ['No', 'Some of them', 'Yes'])

phys_health_consequence = st.selectbox("Do you believe discussing a physical health issue at work would have negative consequences?", ["Yes", "No", "uncertain"])


obs_consequence = st.selectbox("Have you observed negative consequences for coworkers with mental health issues?", ["Yes", "No"])
phys_health_interview = st.selectbox("Would you feel comfortable discussing a physical health issue with your potential employer in an interview?", ["Yes", "No", "Maybe"])

anonymity = st.selectbox("Does your employer allow you to take an anonymous mental health treatment?", ["Yes", "No","unknown"])
mental_vs_physical = st.selectbox("Do you feel your employer treats mental health and physical health equally?", ["Yes", "No", "unknown"])

    
   
input_df = pd.DataFrame([{
    'Gender_clean': gender,
    'self_employed': self_employed,
    'family_history': family_history,
    'treatment': treatment,
    'work_interfere': work_interfere,
    'remote_work': remote_work,
    'benefits': benefits,
    'care_options': care_options,
    'wellness_program': wellness_program,
    'seek_help': seek_help,
    'leave': leave,
    'mental_health_consequence': mental_health_consequence,
    'coworkers': coworkers,
    'mental_health_interview': mental_health_interview,
    'supervisor': supervisor,
    'phys_health_consequence': phys_health_consequence,
    'tech_company': tech_company,
    
    
    'obs_consequence': obs_consequence,
    'phys_health_interview':phys_health_interview ,
    
    'anonymity': anonymity,
    'mental_vs_physical': mental_vs_physical,
    







}])
   
    
if st.button('Predict'):
        model = joblib.load('regression_pipeline_log_n.pkl')
        predicted_age = model.predict(input_df)
        st.write(f"Predicted Age: {np.expm1(predicted_age)} years")
