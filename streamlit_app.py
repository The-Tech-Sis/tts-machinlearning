#Imports
import streamlit as st
import pandas as pd
import numpy as np
from numpy.random import default_rng as rng
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
with st.expander('Data Visualization 1'):
#"species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')
  #st.area_chart(data=df, x='species', y='island', stack='True',color='species')
  df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=['species', 'island'])
  st.area_chart(df)
#Data Preparation
#with st.expander('Data Preparation'):
  

#df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

#st.area_chart(df)
