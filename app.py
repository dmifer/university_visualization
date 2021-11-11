import streamlit as st
import os
import pandas as pd



working_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(working_dir, "data")

df = pd.DataFrame()

for data in os.listdir(data_dir):
    try:
        tmp_df = pd.read_csv(os.path.join(data_dir, data), delimiter=";")
        df = df.append(tmp_df)
    except Exception as e:
        print(e)

print(df.head())


st.write("Initial commit")