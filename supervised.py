import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
st.title("Supervised Task")
st.divider()
st.title("Classifiaction Task")
st.markdown("""
## **Classification Task Overview**

The goal of the classification task is to **predict whether an employee is likely to seek treatment** for mental health issues based on survey responses.  
This is a **supervised learning problem**, where the target variable is categorical (**Yes** or **No**).

---
 **Model Selection**
   We experimented with multiple classification algorithms:
   - Logistic Regression
   - Random Forest Classifier
   - Support Vector Classifier (SVC)
   - XGBoost Classifier

            """)
st.divider()
st.subheader('Logistic Regression')
st.markdown("""
In order to train a good Logistic Regression model, the following hyperparameters 
    are tuned using `GridSearchCV` with 3-fold Cross Validation:
    - **C**: Penalty coefficient  
    - **penalty**: Type of penalty (`l1` or `l2`)  
    - **solver**: Optimization algorithm for training
"""
)
st.code("""
Classification Report:
               precision    recall  f1-score   support

          No       0.67      0.76      0.71       113
         Yes       0.78      0.69      0.73       138

    accuracy                           0.72       251
   macro avg       0.72      0.72      0.72       251
weighted avg       0.73      0.72      0.72       251

ROC-AUC Score: 0.7641400538668719
        """)
st.subheader("Random Forest Classifier")
st.markdown("""
### **Random Forest Classification**

The **RandomForestClassifier** model has a lot of hyperparameters and for this dataset, these can be tuned for the highest score, while looking out for overfitting using cross-validation.

---

#### **The hyperparameters are tuned as:**
- **max_depth**: Maximum tree depth before it is cut off → `10`
- **min_samples_leaf**: Minimum number of leaf nodes the decision trees need to have → `1`
- **min_samples_split**: Minimum number of samples to consider for each split → `5`
- **n_estimators**: Number of ensemble decision trees to use for modelling the data → `200`

---

#### **The classification report and ROC-AUC score for the RFC model are:**
            """)
st.code("""
Classification Report for Random Forest:
               precision    recall  f1-score   support

          No       0.67      0.73      0.70       113
         Yes       0.77      0.71      0.74       138

    accuracy                           0.72       251
   macro avg       0.72      0.72      0.72       251
weighted avg       0.72      0.72      0.72       251

ROC-AUC Score for Random Forest: 0.7854944209311274
        """)
st.subheader("Support Vector Classifier")
st.markdown("""
### **Support Vector Classifier (SVM)**

The **Support Vector Classifier (SVC)** is a supervised learning model that classifies data by finding the optimal hyperplane that separates classes.  
It is effective in high-dimensional spaces and is robust to overfitting, especially in cases where the number of dimensions exceeds the number of samples.

---

#### **The hyperparameters are tuned as:**
- **C**: Regularization parameter → `1`
- **kernel**: Specifies the kernel type to be used in the algorithm → `'rbf'`

---

            """)
st.code("""
Classification Report for SVM:
               precision    recall  f1-score   support

           0       0.67      0.76      0.71       113
           1       0.78      0.70      0.74       138

    accuracy                           0.73       251
   macro avg       0.73      0.73      0.72       251
weighted avg       0.73      0.73      0.73       251

ROC-AUC Score for SVM: 0.7819674233679619
        """)
st.subheader("XGBoost_CLASSIFIER")
st.markdown("""
### **XGBoost Classification**

The **XGBoost Classifier** is an optimized gradient boosting algorithm that is highly efficient, flexible, and portable.  
It works by building an ensemble of weak learners (decision trees) in a sequential manner, where each tree attempts to correct the errors made by the previous ones.  
XGBoost is known for its speed, accuracy, and ability to handle missing values effectively.

---

            """)
st.code("""
Classification Report
               precision    recall  f1-score   support

           0       0.71      0.69      0.70       113
           1       0.75      0.77      0.76       138

    accuracy                           0.73       251
   macro avg       0.73      0.73      0.73       251
weighted avg       0.73      0.73      0.73       251

ROC-AUC Score 0.7790816980890086
        """)
st.divider()
st.image("images/roc_curve.png")
st.markdown("Roc analyis of each classification model")
st.divider()
st.title("Regression Task")
st.markdown("""
### **Regression Task**

For the regression part of this project, the goal is to predict a continuous variable (**Age**) 
based on the available features in the dataset.
regression algorithms can be used for this task: 
**Linear Regression**
 **Random Forest Regressor**
            """)
st.subheader("linear regression")
st.markdown("""
The **Linear Regression** model is one of the simplest and most interpretable algorithms for regression tasks.  
It assumes a linear relationship between the independent variables (features) and the dependent variable (target).

            """)
st.code("""
Linear Regression Results:
Mean Absolute Error: 5.1217315858955885
Mean Squared Error: 42.73968358624385
R-squared: 0.09493857820393281
        """)

st.subheader("Random Forest Regressor")
st.markdown("""
### **Interpretation**
The Random Forest model highlights that factors related to workplace conditions (e.g., work interference, care options) significantly impact the target variable.  
This can help prioritize interventions or policy changes in workplace mental health programs.
""")
st.code("""
Random Forest Regression Results:
Mean Absolute Error: 5.276066004942017
Mean Squared Error: 45.79278460783229
R-squared: 0.03028569077883203
        """)
st.subheader("Logarithmic Linear Regression")
st.markdown("""
Logarithmic Linear Regression is a type of regression where either the dependent variable, independent variables, or both are transformed using the logarithm function (log). This is often done to:

Reduce skewness in the data

Linearize relationships that are otherwise exponential or multiplicative

Stabilize variance (reduce heteroscedasticity)
            """)
st.code("""
Linear Regression Results:
Mean Absolute Error: 0.15649716034174355
Mean Squared Error: 0.03766015901040848
R-squared: 0.09700012145081804
        """)
st.subheader("Logarithmic Random Forest Regressor")
st.markdown("""
A Random Forest model can benefit from logarithmic transformation when input features (or the target variable) are highly skewed.
Log transformation helps:

Reduce skewness

Make patterns more linear and easier to detect

Improve prediction stability
            """)
st.code("""
Random Forest Regression Results:
Mean Absolute Error: 0.16030870224935087
Mean Squared Error: 0.04011175052329034
R-squared: 0.03821686358478826
        """)

