import streamlit as st
from prediction import predict

import numpy as np
import sklearn


def main():

    st.title ('Temperature Prediction')
    Prep_type = st.selectbox('Precip type',[0,1])
    Apparent_temperature = st.text_input('Apparent temperature','0')

    if st.button('predit'):
        result=predict(np.array([[int(Prep_type),int(Apparent_temperature)]]))
        st.text(f'the temperature prediction is :{result[0]}')

if __name__=='__main__':  
    main()     