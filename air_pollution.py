import streamlit as st
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from streamlit_option_menu import option_menu

st.set_page_config(
     page_title="Air Pollution Forecasting App",
     page_icon="https://github.com/Su-Yi-Phyo/Air-pollution-Forecasting-Using-LSTM/blob/main/icons8-pollution-16.png",
     layout="wide")

model = load_model('AirPollutionModel.h5')

with st.sidebar:
  selected = option_menu(None, ["Home", "Test",  "Contact"], 
    icons=['house', 'cloud-upload', "person-lines-fill"], 
    menu_icon="cast", default_index=0,
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "#0F2080", "font-size": "25px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px"},
        "nav-link-selected": {"background-color": "#85C0F9"},
    }
)
   
if selected == "Home":
  with st.container():
    st.title('Air Pollution Forecasting')

    st.markdown("""
      <p style="text-align:justify;">With the advance of technology, it is increasingly exhaust emissions that have caused air pollution. In particular, PM2.5 (Particulate Matter) has been proven that it has a great correlation with human health. Therefore, the detection and prediction of PM 2.5 air pollution is an important issue. Countries around the world have built a variety of sensing devices for monitoring PM2.5 concentrations. There were also many studies constructed to predict and forecast various air pollution. Therefore, how to accurately forecast PM2.5 has become an important issue in recent years.In this project, we propose an approach to forecast PM2.5 concentration using RNN (Recurrent Neural Network) with LSTM (Long Short-Term Memory).</p>
      <p style="text-align: justify;">The training data used in the network is retrieved from Kaggle which is a dataset that reports on the weather and the level of pollution each hour for five years at the US embassy in Beijing, China for the years 2010 to 2014.The data includes the date-time, the pollution called PM2.5 concentration, and the weather information including dew point, temperature, pressure, wind direction, wind speed and the cumulative number of hours of snow and rain.</p>
    """,unsafe_allow_html = True)
    st.image('Data Understanding .png',caption='Data Understanding')
    st.image('Model loss History .png',caption='Model loss History')
    st.image('Accuracy.png',caption='Accuracy')
    st.image('RMSE_MAE.png')
    
elif selected == "Test":
      with st.container():
        st.header("Testing")
        #file upload
        st.write("Upload your csv file:")
        uploaded_file = st.file_uploader("Choose a file...")

        if uploaded_file is not None:
          csv_file= pd.read_csv(uploaded_file)

          #change wind_dir and del previous one
          def func(s):
              if s == "SE":
                  return 1
              elif s == "NE":
                  return 2
              elif s == "NW":
                  return 3
              else:
                  return 4

          csv_file["wind_dir"] = csv_file["wnd_dir"].apply(func)
          del csv_file["wnd_dir"]

          #scaling
          dataset = csv_file
          values = dataset.values

          values = values.astype('float32')

          scaler = MinMaxScaler(feature_range=(0, 1))
          scaled = scaler.fit_transform(values)

          test_x = scaled
          test_x = test_x.reshape((test_x.shape[0], 1, test_x.shape[1]))

          #predicting
          result=model.predict(test_x)
          result=result.ravel()

          poll=np.array(csv_file['pollution'])
          mean_op=poll.mean()
          std_op=poll.std()
          print(mean_op,std_op)
          result=result*std_op + mean_op

          #graph output
#           chart_data = pd.DataFrame(result,colums=['Air Pollution Prediction'])
          st.line_chart(result)
#           from bokeh.plotting import figure

#           x = []
#           y = result
#           for i in range(0,len(result)):
#             x.append[i]

#           p = figure(
#                title='simple line example',
#                x_axis_label='x',
#                y_axis_label='y')

#           p.line(x, y, legend_label='Trend', line_width=2)

#           st.bokeh_chart(p, use_container_width=True)

elif selected == "Contact":
  st.markdown("""
     <h1 style="color: #0F2080; text-align: center;"> Meet Our Team </h1>
  """,unsafe_allow_html = True)

  st.image("Nyein Thiha Zaw.jpg")
  st.markdown("""
     <div class="container", >
        <h2>Nyein Thiha Zaw</h2>
        <p class="title">Team Leader</p>
        <a href='https://github.com/nyeinthihazaw'>
        <button class="hover-item" style="border-radius: 8px; border: none; width: 10%; background-color: #85C0F9; color: white;">
            Contact
        </button>
        </a>
  """, unsafe_allow_html = True)
  st.markdown("""""", unsafe_allow_html = True)

  st.image("syp.jpg")
  st.markdown("""
     <div class="container">
        <h2>Su Yi Phyo</h2>
        <p class="title">Team Member</p>
        <a href='https://github.com/Su-Yi-Phyo'>
        <button class="hover-item" style="border-radius: 8px; border: none; width: 10%; background-color: #85C0F9; color: white;">
            Contact
        </button>
        </a>
  """, unsafe_allow_html = True)
  st.markdown("""""", unsafe_allow_html = True)

  st.image("Nyein Thiha Zaw.jpg")
  st.markdown("""
     <div class="container">
        <h2>Si Thu Aung</h2>
        <p class="title">Team Member</p>
        <a href='https://github.com/sithuaung4c'>
        <button class="hover-item" style="border-radius: 8px; border: none; width: 10%; background-color: #85C0F9; color: white;">
            Contact
        </button>
        </a>
  """, unsafe_allow_html = True)
  st.markdown("""""", unsafe_allow_html = True)

  st.image("Nyein Thiha Zaw.jpg")
  st.markdown("""
     <div class="container">
        <h2>Hsu Ei</h2>
        <p class="title">Team Member</p>
        <a href='hsueieinu@gmail.com '>
        <button class="hover-item" style="border-radius: 8px; border: none; width: 10%; background-color: #85C0F9; color: white;">
            Contact
        </button>
        </a>
  """, unsafe_allow_html = True)
