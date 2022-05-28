import streamlit as st

import pickle
import warnings
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)
#show_predict_page()
def show_predict_page():

    st.title('Prediction')
    st.subheader("This app uses 4 inputs to predict the species of IRIS flowers "
             )
    rf_pickle = open('random_forest_iris.pickle', 'rb')
    map_pickle = open('output_iris.pickle', 'rb')
    rfc = pickle.load(rf_pickle)
    unique_iris_mapping = pickle.load(map_pickle)

    st.write(f"#####   Using:  {rfc} ")
    #st.write(rfc)

    rf_pickle.close()

    map_pickle.close()


    sepal_length = st.number_input('Sepal_Length', min_value=0.0)

    sepal_width = st.number_input('Sepal_Width', min_value=0.0)

    petal_length = st.number_input('Petal_Length', min_value=0.0)
    
    petal_width = st.number_input('Petal_Width', min_value=0.0)



    st.write('User inputs are {}'.format(
        [sepal_length, sepal_width, petal_length, petal_width]))

    new_prediction = rfc.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    prediction_species = unique_iris_mapping[new_prediction][0]

    st.write('Prediction: IRIS is of the {} species'.format(prediction_species))



