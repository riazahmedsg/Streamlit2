import streamlit as st
import pandas as pd

@st.cache
def load_data():
    df = pd.read_csv("iris.csv")
    return df

def show_explore_page():
    df = load_data()
    df = df.rename(columns={'Sepal.Length':'Sepal_Length',
                              'Sepal.Width':'Sepal_Width',
                              'Petal.Length': 'Petal_Length',
                              'Petal.Width': 'Petal_Width'})
    df = df.dropna()
    st.title('Data Exploration')
    data = "iris.csv"
    st.write(' ### Dataset Name:', data)
    st.write('Shape of dataset:', df.shape)
    c = df['Species'].nunique()
    st.write('number of classes:', c)
    s = df['Species'].unique()
    st.write(
        """
     Name of Classes : 
    """
    )
    st.write(f"{s} ")

    des = df.describe()
    st.write(' ### Description of data:', des)

    rows = df.head()
    st.write(' ### First five rows of data:')
    st.write(rows)

    rows = df.tail()
    st.write(' ### Last five rows of data:')
    st.write(rows)





