import streamlit as st

st.set_page_config(page_title="Google Play Store Dashboard", layout="wide")

st.title("📱 Google Play Store Dashboard")

st.write("Welcome! This dashboard analyzes Google Play Store apps.")

st.markdown("""
### What you can explore:
- 📊 Data Overview
- 📂 Category Analysis
- ⭐ App Insights

👉 Use the sidebar to navigate between pages
""")
# Cell 1: Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# Cell 2: Page Configuration
st.set_page_config(page_title="Google Play Store Dashboard", layout="wide")

st.title("Google Play Store EDA Dashboard")
st.markdown("Interactive dashboard based on your notebook analysis")


# Cell 3: Load and Clean Data
@st.cache_data
def load_data():
    df = pd.read_csv("googleplaystore 2.csv")

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Clean Installs
    df["Installs"] = df["Installs"].astype(str)
    df["Installs"] = df["Installs"].str.replace(",", "", regex=False)
    df["Installs"] = df["Installs"].str.replace("+", "", regex=False)
    df["Installs"] = pd.to_numeric(df["Installs"], errors="coerce")

    # Clean Price
    df["Price"] = df["Price"].astype(str).str.replace("$", "", regex=False)
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

    # Clean Reviews
    df["Reviews"] = df["Reviews"].astype(str)
    df["Reviews"] = pd.to_numeric(df["Reviews"], errors="coerce")

    # Android Version
    df["Android_Ver_Num"] = df["Android Ver"].astype(str).str.extract(r"(\\d+\\.\\d+)")
    df["Android_Ver_Num"] = pd.to_numeric(df["Android_Ver_Num"], errors="coerce")

    # Fill missing values
    df["Rating"] = df["Rating"].fillna(df["Rating"].median())
    df["Type"] = df["Type"].fillna("Free")

    # Clean Size
    def clean_size(x):
        if isinstance(x, str):
            x = x.strip()
            if "M" in x:
                return float(x.replace("M", ""))
            elif "k" in x:
                return float(x.replace("k", "")) / 1024
            else:
                return np.nan
        return np.nan

    df["Size"] = df["Size"].replace("Varies with device", np.nan)
    df["Size"] = df["Size"].apply(clean_size)
    df["Size"] = df["Size"].fillna(df["Size"].median())

    return df


# Cell 4: Load Dataset
df = load_data()


# Cell 5: Sidebar Filters
st.sidebar.header("Filters")

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(df["Category"].dropna().unique().tolist())
)

if selected_category != "All":
    filtered_df = df[df["Category"] == selected_category]
else:
    filtered_df = df.copy()


# Cell 6: KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Apps", len(filtered_df))

with col2:
    st.metric("Average Rating", round(filtered_df["Rating"].mean(), 2))

with col3:
    st.metric("Average Installs", int(filtered_df["Installs"].mean()))

st.divider()


# Cell 7: Chart 1 - Category Distribution
fig1 = px.histogram(
    filtered_df,
    y="Category",
    title="Distribution of App Categories"
)
st.plotly_chart(fig1, use_container_width=True)


# Cell 8: Chart 2 - Price vs Rating
fig2 = px.scatter(
    filtered_df,
    x="Price",
    y="Rating",
    title="Price vs Rating",
    hover_data=["App"]
)
st.plotly_chart(fig2, use_container_width=True)


# Cell 9: Chart 3 - Free vs Paid Apps
fig3 = px.pie(
    filtered_df,
    names="Type",
    title="Free vs Paid Apps"
)
st.plotly_chart(fig3, use_container_width=True)


# Cell 10: Chart 4 - Rating vs Installs
fig4 = px.scatter(
    filtered_df,
    x="Rating",
    y="Installs",
    title="Rating vs Installs"
)
st.plotly_chart(fig4, use_container_width=True)


# Cell 11: Chart 5 - Size vs Installs
fig5 = px.scatter(
    filtered_df,
    x="Size",
    y="Installs",
    title="Size vs Installs"
)
st.plotly_chart(fig5, use_container_width=True)


# Cell 12: Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(filtered_df.head(20))
