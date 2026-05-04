import streamlit as st
import pandas as pd

st.title("📊 Data Overview")

df = pd.read_csv("googleplaystore 2.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Basic Info")
st.write(df.shape)
st.write(df.dtypes)
