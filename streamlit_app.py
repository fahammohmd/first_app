import streamlit as st
import pandas as pd

st.title('Machine Learning App 🦾')

st.info('This app builds machine learning models')

df = pd.read_csv('https://github.com/fahammohmd/data/blob/main/Indian%20Urban%20Air%20Quality%20and%20Health%20Impact%202019-2024.csv')
df.columns
