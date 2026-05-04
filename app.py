pythonimport streamlit as st

st.set_page_config(
    page_title="Google Play Store Dashboard",
    layout="wide"
)

st.title("📱 Google Play Store Dashboard")
st.write("Welcome! Use the sidebar to navigate between pages.")

st.markdown("""
### What you can explore:
- 🔍 *Data Explorer and Data Cleaning* — Search and browse the raw dataset
- 📊 *Univariate Analysis* — Category distribution, ratings, free vs paid
- 🔗 *Bivariate Analysis* — Price vs rating, installs correlations  
- 🏆 *Category Installs* — Which categories dominate downloads
""")
