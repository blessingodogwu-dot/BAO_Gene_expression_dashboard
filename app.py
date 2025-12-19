# Streamlit app will go here
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Gene Expression Mini-Dashboard")

st.title("Gene Expression Mini-Dashboard")

st.write("Upload a CSV file with genes in rows and samples in columns.")

uploaded_file = st.file_uploader("Upload gene expression CSV", type=["csv"])

if uploaded_file is None:
    st.info("Please upload a CSV file to begin.")
else:
    try:
        df = pd.read_csv(uploaded_file)

        if df.shape[1] < 2:
            st.error("CSV must contain at least one gene column and one sample column.")
        else:
            df.set_index(df.columns[0], inplace=True)

            st.subheader("Data Preview")
            st.dataframe(df)

            st.subheader("Mean Expression Bar Plot")
            fig1, ax1 = plt.subplots()
            df.mean(axis=1).plot(kind="bar", ax=ax1)
            ax1.set_ylabel("Mean Expression")
            st.pyplot(fig1)

            st.subheader("Expression Heatmap")
            fig2, ax2 = plt.subplots()
            sns.heatmap(df, cmap="viridis", ax=ax2)
            st.pyplot(fig2)

    except Exception as e:
        st.error("An error occurred while processing the file.")
        st.exception(e)

