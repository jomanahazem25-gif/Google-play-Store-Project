import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📂 Category Analysis")

df = pd.read_csv("googleplaystore 2.csv")

# Category distribution
fig = px.histogram(df, y="Category", title="App Categories Distribution")
st.plotly_chart(fig, use_container_width=True)

# Content rating vs category
fig2 = px.histogram(df, x="Category", color="Content Rating",
                    title="Category vs Content Rating")
st.plotly_chart(fig2, use_container_width=True)
