import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

st.set_page_config(page_title="AI Data Quality Agent", layout="wide")

st.title("🤖 AI Data Quality Agent")
st.write("Upload your dataset and let the AI analyze and improve data quality automatically.")

uploaded_file = st.file_uploader("📤 Upload CSV or Excel file", type=["csv", "xlsx"])

# -------------------------------------------------------------
# Function: Outlier Removal using IQR
# -------------------------------------------------------------
def remove_outliers_iqr(df, columns):
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower) & (df[col] <= upper)]
    return df

if uploaded_file is not None:

    # Load data
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)

    st.subheader("📌 Uploaded Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    # Column insights
    st.subheader("📊 Column Summary & Data Types")
    st.write(df.dtypes)

    # Convert potential dates automatically
    for col in df.columns:
        try:
            df[col] = pd.to_datetime(df[col], errors="ignore")
        except:
            pass

    # Missing value report
    st.subheader("🧹 Missing Value Analysis")
    missing = df.isnull().sum().reset_index()
    missing.columns = ["Column", "Missing_Count"]
    st.dataframe(missing)

    # Cleaning options
    st.subheader("⚙ Cleaning Options")
    clean_option = st.multiselect(
        "Select cleaning operations",
        ["Fill Mean (Numeric)", "Fill Mode (Categorical)", "Drop Missing Rows", "Remove Duplicates", "Remove Outliers"],
    )

    if "Fill Mean (Numeric)" in clean_option:
        num_cols = df.select_dtypes(include=np.number).columns
        df[num_cols] = SimpleImputer(strategy="mean").fit_transform(df[num_cols])
        st.success("✔ Filled missing numeric values with MEAN")

    if "Fill Mode (Categorical)" in clean_option:
        cat_cols = df.select_dtypes(exclude=np.number).columns
        df[cat_cols] = SimpleImputer(strategy="most_frequent").fit_transform(df[cat_cols])
        st.success("✔ Filled missing categorical values with MODE")

    if "Drop Missing Rows" in clean_option:
        df = df.dropna()
        st.success("✔ Dropped rows containing missing values")

    if "Remove Duplicates" in clean_option:
        before = len(df)
        df = df.drop_duplicates()
        st.success(f"✔ Removed {before - len(df)} duplicate rows")

    if "Remove Outliers" in clean_option:
        numeric_cols = df.select_dtypes(include=np.number).columns
        df = remove_outliers_iqr(df, numeric_cols)
        st.success("✔ Removed outliers using IQR method")

    # Cleaned dataset preview
    st.subheader("📦 Cleaned Dataset Output")
    st.dataframe(df, use_container_width=True)



    # Correlation heatmap
    if st.checkbox("Show Correlation Heatmap"):
        st.subheader("📈 Correlation Heatmap")
        numeric_df = df.select_dtypes(include=np.number)
        fig, ax = plt.subplots()
        sns.heatmap(numeric_df.corr(), annot=True, ax=ax)
        st.pyplot(fig)

    # Download button
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇ Download Cleaned CSV", csv, "cleaned_data.csv", "text/csv")

else:
    st.info("📁 Please upload a dataset to begin analysis.")
