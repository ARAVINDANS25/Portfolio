import streamlit as st
from streamlit_option_menu import option_menu

# Configure the page layout to be wide
st.set_page_config(layout="wide")

# Add a spacer
st.write("##")

# Main heading and subheading
st.subheader("Hey Guys, I'm Aravindan S :wave:")
st.title("Welcome to My Portfolio Website")
st.subheader("About")

# About section description
st.write("""
As a passionate and dedicated entry-level data professional, 
I am eager to bring my skills in data analysis, cloud computing, and data management 
to real-world projects. With certification and five badges in Snowflake, I have developed 
a strong foundation in data warehousing, ETL processes, and data integration.
""")

# Separator line
st.write('---')

# Container for the navigation menu
with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Project', 'Contacts'],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )

# Add content for each menu option based on the selected option
if selected == 'About':

  with st.container():
    col1,col2 = st.columns(2)
    with col1:
      st.write("##")
      st.subheader("I am Aravindan S")
      st.title("PG at MCA")
    with col2:
      
