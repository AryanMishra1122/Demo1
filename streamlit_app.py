import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.express as px
st.title('IRIS FLOWER DASHBOARD')
st.divider()

with st.sidebar:
 st.subheader('Description')
 st.write('The Iris dataset was used in R.A. Fisher classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems, and can also be found on the UCI Machine Learning Repository.It includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.The columns in this dataset are:IdSepalLength,CmSepalWidth,CmPetalLength,CmPetalWidth,CmSpecies')

 df=pd.read_csv('C:/Users/Admin/Downloads/iris.csv')
df
c1,c2=st.columns(2)
with c1:
 a=df['Species'].unique()
 a
 b=df['Species'].value_counts()
 b
 st.bar_chart(b)
with c2:
 fig,ax=plt.subplot()
 ax.pie(b,labels=a,autopct='%1.1f%%',startangle=90)
ax.axis=('equal')

 




