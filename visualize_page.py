import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    df = pd.read_csv("iris.csv")
    return df

def show_visualize_page():
    df = load_data()
    df = df.rename(columns={'Sepal.Length':'Sepal_Length',
                              'Sepal.Width':'Sepal_Width',
                              'Petal.Length': 'Petal_Length',
                              'Petal.Width': 'Petal_Width'})
    st.title("Data Visualization")

# pie chart
    st.write(""" #### Pie Plot of Species Distribution """)
    data = df["Species"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

# Bar Chart

    st.write(
        """
    #### Petal_Length By Species
    """
    )
    st.write(""" #### Bar Chart """)
    data = df.groupby(["Species"])["Petal_Length"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(""" #### Line Graph""")

    data = df.groupby(["Species"])["Petal_Length"].mean().sort_values(ascending=True)
    st.line_chart(data)

    # Bar and line Charts using Petal_Width

    st.write(
        """
    #### Petal_Width By Species
    """
    )
    st.write(""" #### Bar Chart """)
    data = df.groupby(["Species"])["Petal_Width"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(""" #### Line Graph""")

    data = df.groupby(["Species"])["Petal_Width"].mean().sort_values(ascending=True)
    st.line_chart(data)
