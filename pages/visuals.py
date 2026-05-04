import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⭐ App Insights")

df = pd.read_csv("googleplaystore 2.csv")

# Clean installs
df["Installs"] = df["Installs"].astype(str).str.replace(",", "").str.replace("+", "")
df["Installs"] = pd.to_numeric(df["Installs"], errors="coerce")

# Rating vs installs
fig = px.scatter(df, x="Rating", y="Installs",
                 title="Rating vs Installs",
                 hover_data=["App"])
st.plotly_chart(fig, use_container_width=True)

# Size vs installs
df["Size"] = df["Size"].replace("Varies with device", None)
df["Size"] = df["Size"].str.replace("M", "").str.replace("k", "")
df["Size"] = pd.to_numeric(df["Size"], errors="coerce")

fig2 = px.scatter(df, x="Size", y="Installs",
                  title="Size vs Installs")
st.plotly_chart(fig2, use_container_width=True)

# Visual 5: Rating Distribution
# -----------------------------
st.subheader("⭐ Rating Distribution")

fig5 = px.histogram(df, x="Rating")
st.plotly_chart(fig5)

# -----------------------------
# Visual 6: Content Rating
# -----------------------------
st.subheader("👶 Content Rating")

fig6 = px.histogram(df, x="Content Rating")
st.plotly_chart(fig6)

# -----------------------------
# Top Apps Table
# -----------------------------
st.subheader("🔥 Top Apps by Installs")

top_apps = df.sort_values(by="Installs", ascending=False).head(10)
st.dataframe(top_apps[["App", "Category", "Rating", "Installs"]])

# -----------------------------
# Insights
# -----------------------------
