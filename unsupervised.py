import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
st.title("📊 Clustering Analysis")
st.divider()
st.markdown("""
The objective of this task is to make clusters and group tech workers according to their mental health 
personas. Below are some of the techniques and algorithms applied for the same.""")
st.write("""
Firstly we have  cleaned the data and encoded all the parameters  . After that we select the features for clustering.

         """)
st.code("""
features= [
    'family_history',# Personal risk factors
    'treatment',
    'work_interfere',
    'remote_work',
    'tech_company',
    'benefits',
    'care_options',
    'wellness_program',
    'seek_help',
    'anonymity',
    'leave',
    'mental_health_consequence',
    'phys_health_consequence',
    'coworkers',
    'supervisor',
    'mental_health_interview',
    'phys_health_interview',
    'mental_vs_physical',
    'obs_consequence'
]

        """)
st.markdown("""
###Selected 19 features for analysis.
Dataset shape: (1251, 19)
""")
st.header("*")
st.title("Clustering Techniques")
st.markdown("""
Now for dimensionality reduction we will use various  clustering techniques that are as follows:
#1.PCA(Principle component analysis)
#2.t-SNE(t-distributed Stochastic Neigbour Embedding)
#3.UMAP ( uniform manifold approximation and projection)
            """)
st.subheader("Visulaisation of  data after applying dimensionality reduction")
st.image("images/dim_r.png")
st.divider()
st.title("Clustering Analyisis")
st.markdown("""
applying clustering analysis to find distinct personas in our data 
#We will determine the optimal number of clusters using silhouette analysis
#compare multiple clustering algorithems :
   **1.k means**
   **2.agglomerative hierarchial clustering**
   **3.DBSCAN- density based clustering**

            """)
st.header("silhouette Scores of differnt Algorithems")
st.code("""
Clustering performance evaluation
K-means Silhouette  Score:0.4685
K-means clusters :18
agglomerative Silhouette  Score:0.4288
agglomerative clusters :18
DBSCAN Silhouette Score:0.3638
DBSCAN Clusters :3
DBSCAN NOISE:0
        """)
st.divider()
st.subheader("Comprehensive Clustering Visualization")
st.image("images/clustering_analysis.png")
st.divider()
st.subheader("KMeans Clusters (27 columns) Visualized with UMAP")
st.image("images/k-means_cluster.png")
st.divider()
st.markdown(""" 
Trying other technique to get better clusters and good silhouette score
            """)
st.markdown("""The columns `Age`, `Country`, `Gender`, `no_employees`, `wellness_program`, `care_options`, `mental_health_consequence`,
             `benefits` were dropped due to their less contribution to the overall cluster making. These features somewhere
             get covered in the rest of the questionnaire filled by the respondents , Also combining some other parameters into one and dropping 
            them to get processed data with less numner of columns so as to  MAKE GOOd clusters and get better Silhouette score
            """)
st.divider()
st.title("Silhouette scores for scaled Data")
st.code("""
numerical_features=[
    'family_history',
    'treatment',
    'work_interfere',
    'remote_work',
    'coworkers',
    'supervisor',
    'phys_health_interview',
    'obs_consequence',
    'employer_score',
    'op_employer'
]
        """)
st.code("""
Best Silhouette Score:0.7045
Best n_neighbors:20
Best k: 5
        """)
st.divider()
st.title("Clusters with k=5")
st.image("images/Best_clustering.png")
st.markdown("""
various cluster analysis :
**Cluster Count**
cluster
0    321
2    290
3    153
1    137
4    124
           """)
st.subheader("Numeric SUMMARY")
st.code("""
 family_history  treatment  work_interfere  remote_work  coworkers  \
cluster                                                                      
0              0.174455   0.006231        0.444444     0.000000   0.470405   
1              0.525547   0.642336        0.615572     0.313869   0.467153   
2              0.372414   0.496552        0.544828     1.000000   0.537931   
3              1.000000   0.993464        0.629630     0.000000   0.490196   
4              0.000000   1.000000        0.602151     0.000000   0.504032   

         supervisor  phys_health_interview  obs_consequence  employer_score  \
cluster                                                                       
0          0.601246               0.387850              1.0        0.355441   
1          0.445255               0.408759              0.0        0.332473   
2          0.596552               0.398276              1.0        0.382574   
3          0.532680               0.316993              1.0        0.424276   
4          0.516129               0.379032              1.0        0.419748   

         op_employer  
cluster               
0           0.340343  
1           0.164234  
2           0.337069  
3           0.218954  
4           0.233871
        """)
st.divider()
st.title("various interpretations")
st.image("images/cluster_profiles.png")
st.image("images/xa.png")


st.divider()

