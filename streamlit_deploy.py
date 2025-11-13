import streamlit as st
from prediction import predict

import numpy as np



def main():

    st.title ('Temperature Prediction')
    Prep_type = st.selectbox('Precip type',[0,1])
    Apparent_temperature = st.text_input('Apparent temperature','0')

    if st.button('predit'):
        result=predict(np.array([[Prep_type,Apparent_temperature]]))
        st.text(result)

if __name__=='__main__':  
    main()     