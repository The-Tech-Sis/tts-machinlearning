import streamlit as st
import pandas as pd
import numpy as np
from scikitlearn import 
st.title('🎈 Machine Learning Project')

st.info('This app is for a machine learning deployed model')

with st.explander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv['https://raw.githubusercontent.com/dataprofessor/streamlit_freecodecamp/refs/heads/main/app_8_classification_penguins/penguins_cleaned.csv']
  df

  st.write('**x**')
  x = df.drop('species', asix=1)
  x

  st.write('**y**')
  y = df.species
  y
