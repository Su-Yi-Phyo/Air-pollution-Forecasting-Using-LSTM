import streamlit as st
#from streamlit_option_menu import option_menu

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
    st.image('https://www.perkinselearning.org/sites/elearning.perkinsdev1.org/files/Amazon_1.png')


elif selected == "Contact":
  st.markdown("""
    <div class="row">
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
