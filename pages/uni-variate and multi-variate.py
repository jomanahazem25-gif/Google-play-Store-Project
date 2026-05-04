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
# Chart 1: Category Distribution
# -----------------------------
with col1:
    fig1 = px.histogram(df, y="Category", title="Category Distribution")
    st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# Chart 2: Ratings Distribution
# -----------------------------
with col2:
    fig2 = px.histogram(df, x="Rating", title="Rating Distribution")
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Row 2
# -----------------------------

col3, col4 = st.columns(2)

# -----------------------------
# Chart 3: Rating vs Installs
# -----------------------------
with col3:
    fig3 = px.scatter(df, x="Rating", y="Installs",
                      title="Rating vs Installs",
                      hover_data=["App"])
    st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# Chart 4: Size vs Installs
# -----------------------------
with col4:
    fig4 = px.scatter(df, x="Size", y="Installs",
                      title="Size vs Installs")
    st.plotly_chart(fig4, use_container_width=True)

# -----------------------------
# Row 3
# -----------------------------

col5, col6 = st.columns(2)

# -----------------------------
# Chart 5: Free vs Paid
# -----------------------------
with col5:
    fig5 = px.pie(df, names="Type", title="Free vs Paid Apps")
    st.plotly_chart(fig5, use_container_width=True)

# -----------------------------
# Chart 6: Content Rating
# -----------------------------
with col6:
    fig6 = px.histogram(df, x="Content Rating",
                        title="Content Rating Distribution")
    st.plotly_chart(fig6, use_container_width=True)

# -----------------------------
# Insights Section
# -----------------------------

st.divider()

st.subheader("📌 Key Insights")

st.markdown("""
- Most apps belong to a few dominant categories like Family and Games  
- Ratings are generally high (around 4.0–4.5)  
- Higher ratings tend to relate to more installs  
- Most apps are free  
- App size has weak correlation with installs  
""")
