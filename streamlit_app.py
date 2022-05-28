import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from visualize_page import show_visualize_page

page = st.sidebar.selectbox(" Explore - Visualize - Predict", ( "Explore","Visualize", "Predict"))
if page == "Explore":
    show_explore_page()
elif page == "Visualize":
    show_visualize_page()
else:
    show_predict_page()

