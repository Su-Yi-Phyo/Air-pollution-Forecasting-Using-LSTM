import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler


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

    st.write("<p>The Equity Explorer is a set of Arup-designed analyses to identify vulnerable and historically under-served geographies at the census tract level. The tool provides a transparent, Arup-approved framework for approaching equity and allows users to compare indicators and explore the data for census tracts across the US. Users can also customize a transportation vulnerability index for their specific planning purposes to best understand which areas have the biggest gaps in accessibility and demand.</p>",unsafe_allow_html=True)
    st.image('https://cdn.corporatefinanceinstitute.com/assets/line-graph.jpg')

    st.write("<p>The Equity Explorer is a set of Arup-designed analyses to identify vulnerable and historically under-served geographies at the census tract level. The tool provides a transparent, Arup-approved framework for approaching equity and allows users to compare indicators and explore the data for census tracts across the US. Users can also customize a transportation vulnerability index for their specific planning purposes to best understand which areas have the biggest gaps in accessibility and demand.</p>",unsafe_allow_html=True)
    st.image('https://sites.google.com/a/stu.ximb.ac.in/pfc-fra/_/rsrc/1404573351589/share-price/line-graph/pfc%201.jpg')

    st.write("<p>The Equity Explorer is a set of Arup-designed analyses to identify vulnerable and historically under-served geographies at the census tract level. The tool provides a transparent, Arup-approved framework for approaching equity and allows users to compare indicators and explore the data for census tracts across the US. Users can also customize a transportation vulnerability index for their specific planning purposes to best understand which areas have the biggest gaps in accessibility and demand.</p>",unsafe_allow_html=True)
    st.image('https://www.perkinselearning.org/sites/elearning.perkinsdev1.org/files/Amazon_1.png')

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
          scaled

#           test_x = scaled
#           test_x = test_x.reshape((test_x.shape[0], 1, test_x.shape[1]))

#           #predicting
#           result=model.predict(test_x)
#           result=result.ravel()

#           poll=np.array(csv_file['pollution'])
#           mean_op=poll.mean()
#           std_op=poll.std()
#           result=result*std_op + mean_op

#           print(result)

elif selected == "Contact":
  st.markdown("""
    <div class="row">
    <h1 style="">Meet Our Team</h1>
  <div class="column">
    <div class="card">
      <img src="https://i.pinimg.com/originals/e5/71/4a/e5714a28c71efc5235c89db3cb2fa801.jpg">
      <div class="container">
        <h2>Nyein Thiha Zaw</h2>
        <p class="title">Team Leader</p>
        <p>Some text that describes me lorem ipsum ipsum lorem.</p>
        <p>example@example.com</p>
        <p><button class="button">Contact</button></p>
      </div>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <img src="https://i.pinimg.com/originals/e5/71/4a/e5714a28c71efc5235c89db3cb2fa801.jpg">
      <div class="container">
        <h2>Mike Ross</h2>
        <p class="title">Art Director</p>
        <p>Some text that describes me lorem ipsum ipsum lorem.</p>
        <p>example@example.com</p>
        <p><button class="button">Contact</button></p>
      </div>
    </div>
  </div>
  """, unsafe_allow_html=True)
