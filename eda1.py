import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("deep")
survey=pd.read_csv("cleaned_survey1.csv")
st.title("Data Analyis ,OBservations & Interferences")
st.divider()
st.header("Dataset Anomalies")
st.markdown("""
The dataset being the result of survey,\
clearly had alot of problems like the range problem \
for the numerical data and outliers . Also some Parameters like Age Gender \
have various errors and should be cleaned for proper data analysis\
For this data needs to  be cleaned
""")
st.markdown("""
**Checking for missing values**
Here we can get idea of what number of values are  missing in the data set 
            """)
st.table(
    pd.DataFrame(
        index=["state", "comments", "work_interfere","self_employed"],
        data={
            "Missing Count":[1095,515,264,18],
            "Missing Percentage":[86.973789, 40.905481,20.969023,1.429786],
        }
    )
)
st.markdown("""
**Checking for age after cleaning the age column**
Cleaned age data:
count    1251.000000
mean       32.076739
std         7.288272
min        18.000000
25%        27.000000
50%        31.000000
75%        36.000000
max        72.000000

**This shows that the average age of person suffering from illness is 32**
""")
st.markdown("""
**Making a new cleaned employees column b preprocessing the no_employee column**
cleaned _employees
count    1243.000000
mean      319.066774
std       401.999797
min         3.000000
25%        15.000000
50%        63.000000
75%       750.000000
max      1001.000000
            """)

            
st.subheader("Observations:")
st.markdown("""
* Need for range specification for numerical columns in future surveys,  
  specification of standard options with inclusive options accounting for  
  the diversity of the surveyee pool, and the models need to be fitted  
  with imputation capabilities for handling NaN values.  
* The features in the data have a fair amount of outliers.
  
""")
st.subheader("Gender Classification")

st.markdown("""
**Gender Categories in Dataset:**

- **Male**: 992  
- **Female**: 250  
- **Other**: 6  
- **Not specified**: 3  

**Total Records:** 1251
""")

st.header("Outlier Detection Summary")


st.markdown("""
**Numerical columns for outlier analysis:**  
`['Age', 'cleaned_employees']`

---

### **Column: Age**
- **Total values**: 1251  
- **Outlier Count**: 32 (**2.6%**)  
- **Bounds**: **13.50** to **49.50**  
- **Sample Outliers**: [50, 56, 60, 54, 55]...

---

### **Column: cleaned_employees**
- **Total values**: 1243  
- **Outlier Count**: 0 (**0.0%**)  
- **Bounds**: **-1087.50** to **1852.50**

---

**Dataset shape after outlier removal**: `(1251, 29)`  
**Original dataset shape**: `(1251, 29)`  
**Rows removed due to outliers**: **0**
""")
st.divider()

st.header("Univariate Feature Analysis")

st.image("images/univariate1.png")

cols = st.columns(3)

with cols[0]:
    st.markdown("""
    - **Average age of treatment seekers**: 32.6  
    - **Average age of non-treatment seekers**: 31.5
    """)

with cols[1]:
    st.markdown("""
    **Treatment rates by gender:**  
    - **Female**: 69.6%  
    - **Male**: 45.4%  
    - **Not Specified**: 100.0%  
    - **Other**: 86.8%
    """)

with cols[2]:
    st.markdown("""
    **Top 5 countries by treatment rate:**  
    - **Croatia**: 100.0%  
    - **Denmark**: 100.0%  
    - **Slovenia**: 100.0%  
    - **Moldova**: 100.0%  
    - **Iceland**: 100.0%
    """)

st.image("images/univariate2.png")
cols = st.columns(4)

with cols[0]:
    st.markdown("""
    **Treatment rates by benefits availability:**  
    - **No**: 48.2%  
    - **Unknown**: 37.1%  
    - **Yes**: 63.8%
    """)

with cols[1]:
    st.markdown("""
    **Treatment rates by remote work:**  
    - **No**: 49.7%  
    - **Yes**: 52.6%
    """)

with cols[2]:
    st.markdown("""
    **Treatment rates by company size:**  
    - **3.0**: 40.1%  
    - **5.0**: 50.0%  
    - **6.0**: 54.5%  
    - **500.0**: 46.3%  
    - **750.0**: 58.3%  
    - **1001.0**: 52.2%
    """)

with cols[3]:
    st.markdown("""
    **Treatment rates by work interference:**  
    - **Never**: 14.2%  
    - **Often**: 85.0%  
    - **Rarely**: 70.5%  
    - **Sometimes**: 49.7%
    """)


st.image("images/univariate3.png")
cols = st.columns(4)

with cols[0]:
    st.markdown("""
    **Treatment rates by family history:**  
    - **Family history No**: 35.4%  
    - **Family history Yes**: 74.6%
    """)

with cols[1]:
    st.markdown("""
    **Treatment rates by supervisor support:**  
    - **No**: 52.3%  
    - **Some of them**: 51.6%  
    - **Yes**: 48.4%
    """)
   

with cols[2]:
    st.markdown("""
    **Treatment rates by coworker support:**  
    - **No**: 45.3%  
    - **Some of them**: 50.5%  
    - **Yes**: 56.8%
    """)

with cols[3]:
    st.markdown("""
    **Treatment rates by anonymity protection:**  
    - **No**: 57.8%  
    - **Unknown**: 45.3%  
    - **Yes**: 60.8%
    """)

st.divider()
st.header("Bivariate Analysis")
st.image("images/bivariate1.png")
st.image("images/bvariate2.png")
st.image("images/bivariate3.png")
st.image("images/bivariate4.png")
st.divider()

st.image("images/bivariate5.png")
st.divider()
st.header("Multivariate Analysis")
st.image("images/multivariate.png")


st.divider()
st.header("Key Observations & Patterns")

cols = st.columns(2)

with cols[0]:
    st.markdown("""
    - **High-risk threshold**: 18.0  
    - **High-risk group size**: 369 (29.5%)  
    - **Treatment rate in high-risk group**: 44.7%  
    - **Overall treatment rate**: 50.5%  
    """)

with cols[1]:
    st.markdown("""
    **High-risk group characteristics:**  
    - Average age: 31.8  
    - Gender distribution:  
        - Male: 313 (84.8%)  
        - Female: 53 (14.4%)  
        - Not Specified: 2 (0.5%)  
        - Other: 1 (0.3%)  
    """)
st.header("Univariate insights")
st.markdown("""
        The univariate analysis reveals that the dataset is nearly evenly split between individuals 
        who have and have not sought mental health treatment with a slight lean toward not seeking help 
        Most respondents reported no family history of mental illness though about one third did indicating 
        a significant at risk group Mental health was most often reported to sometimes interfere with work 
        while remote work was uncommon among participants The majority work in technology companies and 
        although mental health benefits are relatively common many respondents were either unsure about 
         their availability or reported having none

                    

        """)
st.header("Bivariate analysis insights")
st.markdown("""
        • The bivariate analysis shows that females and those identifying as other genders are more likely 
          to seek mental health treatment compared to males Age trends indicate that individuals in their 
          late twenties to mid thirties are the most likely to seek treatment while younger and older 
          age groups have lower treatment rates Country wise treatment seeking varies with the Netherlands 
          showing notably lower rates and the United States showing higher rates Company size appears to 
          have less variation though smaller companies and certain mid sized firms show slightly higher 
          proportions of treatment seeking employees

 
        """)

