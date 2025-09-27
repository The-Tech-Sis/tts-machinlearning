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

# To use the st.area_chart function in Streamlit, you can create an area chart to visualize data trends over time or across categories. Here's a concise guide:
# Basic Usage
# The st.area_chart function is straightforward and works well with pandas DataFrames, NumPy arrays, or dictionaries. Here's an example:

# Create sample data
with st.expander('Data Preparation'):
  data = pd.DataFrame(
      np.random.randn(20, 3),  # 20 rows, 3 columns of random data
      columns=['Category A', 'Category B', 'Category C']
  )

# Display the area chart
st.area_chart(data)

# Key Points

# Input Data: The data should be in a tabular format (e.g., DataFrame) where rows represent data points and columns represent categories.
# Automatic Indexing: If no index is provided, Streamlit uses the DataFrame's index for the x-axis.
# Customization: While st.area_chart is simple, for advanced customization, you can use st.altair_chart with Altair specifications.

# Example with Time-Series Data

# Generate time-series data
with st.expander('Data Preparation'):
  dates = pd.date_range('2023-01-01', periods=30)
  data = pd.DataFrame(
      np.random.randn(30, 2).cumsum(axis=0),  # Cumulative sum for smoother trends
      index=dates,
      columns=['Sales', 'Revenue']
  )

# Display the area chart
st.area_chart(data)

# This will create an area chart with dates on the x-axis and the cumulative values for "Sales" and "Revenue" on the y-axis.
# When to Use

# To visualize trends over time.
# To compare multiple categories with overlapping areas.
