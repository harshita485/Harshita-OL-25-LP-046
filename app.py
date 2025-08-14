import streamlit as st

def home():
    st.title("Openlearn 1.0 ML Capstone project")
    st.header("Dataset Overview")
    st.markdown(""" 
    ### Dataset Source:[Mental Health in Tech survey](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey)
    ### Collected by OSMI(Open Sourcing Mental Illness)
    *Demographic details (age, gender, country)
    *Workplace environment (mental health benefits, leave policies)
    *Personal experiences (mental illness, family history)
    *Attitudes towards mental health 
                """)
    st.header("Problem Statement")
    st.markdown("""
    As a Machine Learning Engineer at NeuronInsights Analytics, you’ve been contracted by a coalition of
    leading tech companies including CodeLab, QuantumEdge, and SynapseWorks. Alarmed by rising burnout,
    disengagement, and attrition linked to mental health, the consortium seeks data-driven strategies to
    proactively identify and support at-risk employees. Your role is to analyze survey data from over 1,500 tech
    professionals, covering workplace policies, personal mental health history, openness to seeking help, and
    perceived employer support.
    ### Project Objectives:
    * **Exploratory Data Analysis** *
    * **Supervised Learnings** *
        * *Classification task*: Predict whether a person is likely to seek mental health treatment (treatment column: yes/no)
        *  *Regressor Task* :Predict the respondent's age
    * **Unsupervised Learnings**:Cluster tech workers into mental health personas
    * **StreamLit App Deployment**
                """)
app=st.navigation(
    [
        st.Page(home, title="Project Details", icon="🏠"),
        st.Page("eda1.py", title="Data Analysis",icon="🧮"),
        st.Page(
            "supervised.py",
            title="Supervised learning",
            icon="🎯",
        ),
        st.Page("predict_age.py", title="Age prediction",icon="📊"),
        st.Page("treatment.py",title="Treatment Classification", icon="📉"),
        st.Page("unsupervised.py", title="Unsupervised Learning", icon="💻")
    ]
)
app.run()