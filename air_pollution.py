import streamlit as st
import pandas as pd
import numpy as np
import joblib

model =  joblib.load('AirPollutionModel.h5')

#Sidebar
with st.sidebar:
    st.write('This is the first sentence')
    st.number_input('Temperature:')
    st.number_input('Wind Speed:')
    st.number_input('Rain:')
    st.number_input('Snow:')
    st.number_input('Dew:')
    st.number_input('Wind Direction:')
    st.text_input('Pressure:')
    st.markdown('This is last sentence')
    st.write('Output:')

st.title('Air Pollution Forecasting')

st.write("<p>The Equity Explorer is a set of Arup-designed analyses to identify vulnerable and historically under-served geographies at the census tract level. The tool provides a transparent, Arup-approved framework for approaching equity and allows users to compare indicators and explore the data for census tracts across the US. Users can also customize a transportation vulnerability index for their specific planning purposes to best understand which areas have the biggest gaps in accessibility and demand.</p>",unsafe_allow_html=True)
st.image('https://www.planetware.com/wpimages/2020/08/japan-best-cities-tokyo.jpg')

st.write("<p>The Equity Explorer is a set of Arup-designed analyses to identify vulnerable and historically under-served geographies at the census tract level. The tool provides a transparent, Arup-approved framework for approaching equity and allows users to compare indicators and explore the data for census tracts across the US. Users can also customize a transportation vulnerability index for their specific planning purposes to best understand which areas have the biggest gaps in accessibility and demand.</p>",unsafe_allow_html=True)
st.image('https://www.planetware.com/wpimages/2020/08/japan-best-cities-tokyo.jpg')

st.write("<p>The Equity Explorer is a set of Arup-designed analyses to identify vulnerable and historically under-served geographies at the census tract level. The tool provides a transparent, Arup-approved framework for approaching equity and allows users to compare indicators and explore the data for census tracts across the US. Users can also customize a transportation vulnerability index for their specific planning purposes to best understand which areas have the biggest gaps in accessibility and demand.</p>",unsafe_allow_html=True)
st.image('https://www.planetware.com/wpimages/2020/08/japan-best-cities-tokyo.jpg')