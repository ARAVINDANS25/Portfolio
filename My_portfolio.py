import streamlit as st
import streamlit_option_menu as option_menu

st.set_page_config(layout="wide")

st.write("##")
st.subheader("Hey Guys , I'm  Aravindan S :wave:")
st.title("Welcome to My Portfolio Website")
st.subheader("About")
st.write("""As a passionate and dedicated entry-level data professional, 
I am eager to bring my skills in data analysis, cloud computing, and data management 
to real-world projects. With certification and five badges in Snowflake, I have developed 
a strong foundation in data warehousing, ETL processes, and data integration.""")

st.write('---')

with st.container():
  selected = option_menu(
    menu_title  = None
    options = ['About','Project','Contacts'],
    icons = ['person','code-slash','chat-left-text-fill']
    orientation = 'horizontal'
  )
