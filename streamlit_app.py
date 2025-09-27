#Imports
import streamlit as st
import pandas as pd
import numpy as np
#from scikitlearn import 

st.title('🎈 Machine Learning Project')
st.info('This app is for a machine learning deployed model')


with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/streamlit_freecodecamp/refs/heads/main/app_8_classification_penguins/penguins_cleaned.csv')
  df

  st.write('**x**')
  x = df.drop('species', axis=1)
  x

  st.write('**y**')
  y = df.species
  y

#Data Visualization
with st.expander('Data Visualization'):
#"species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')


#Data Preparation
with st.expander('Data Preparation'):
