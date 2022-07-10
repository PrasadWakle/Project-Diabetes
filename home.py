import streamlit as st
import numpy as np
import pandas as pd

def main():
    st.title('Diabetes Prediction Web App')
    st.header('Welcome to my project!')

    st.markdown("""The aim of this project is to analyze the **PIMA Indian Diabetes Dataset** and use Support Vector Machine for prediction.""")

    df=pd.read_csv(r'C:/Users/prasa/OneDrive/Desktop/Diabetes/diabetesdataset.csv')

    st.subheader('Training Data')
    st.write(df.describe())

   