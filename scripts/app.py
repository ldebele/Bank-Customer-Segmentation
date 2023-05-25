import streamlit as st




def user_input():

    # Radio Button
    trimmed = st.sidebar.radio("**Variance**", 
                options= ["Trimmed", "Not Trimmed"]
        )
    st.sidebar.write(trimmed)

    # Choice Number of cluster
    st.sidebar.header("**K-Means Clustering**")
    k = st.sidebar.slider("**Number of clusters (k)**", min_value=2, max_value=12, step=1)




st.header("Survey of Consumer Finances")
st.write("**High Variance Features**")

user_input()