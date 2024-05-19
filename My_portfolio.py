import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

# Configure the page layout to be wide
st.set_page_config(layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_UBiAADPga8.json")

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
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Aravindan S")
            st.subheader("Postgraduate at SASTRA Deemed University")
        with col2:
            st_lottie(lottie_coder)
    st.write("---")
  
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Education")
            st.write("""
            - **SASTRA Deemed University**
              - Master of Computer Applications (MCA)
              - Grade: 8.3 CGPA
            - **M.I.E.T. Arts College, Gundur, Tiruchirappalli**
              - Bachelor's degree in Mathematics
              - Grade: 8.5 CGPA
            - **Khajamian Hr. Sec School, Trichy**
              - 12th Grade
              - Grade: 57.8%
            - **A.M.R.C Hr. Sec School, Trichy**
              - 10th Grade
              - Grade: 78.8%
            """)

        with col4:
            st.subheader("Certifications")
            certifications = [
                {"name": "Hands-On Essentials: Data Warehousing Workshop", "link": "https://achieve.snowflake.com/8527c457-c00e-4f42-afc1-10bd73c02780"},
                {"name": "Hands-On Essentials: Data Application Builders Workshop", "link": "https://achieve.snowflake.com/d65b1299-a94b-4a1c-a9bf-a6c1f4eede2f"},
                {"name": "Hands-On Essentials: Collaboration, Marketplace & Cost Estimation Workshop", "link": "https://achieve.snowflake.com/9674e7cb-57db-4778-b3ab-5d915d338765"},
                {"name": "Hands-On Essentials: Data Lake Workshop", "link": "https://achieve.snowflake.com/d8889d6b-286d-4820-8fca-e5d5bf4a3093"},
                {"name": "Hands-On Essentials: Data Engineering Workshop", "link": "https://achieve.snowflake.com/4be693b6-7348-4966-bca9-d3be704b8ade"},
                {"name": "SQL- The Complete Introduction to SQL programming", "link": "https://udemy-certificate.s3.amazonaws.com/image/UC-05e4994c-688a-4280-9ed7-d3d5e023cb5a.jpg"},
                {"name": "Python Programming - From Basics to Advanced level [2024]", "link": "https://udemy-certificate.s3.amazonaws.com/image/UC-9e0966de-64ba-4b83-8be8-d678411ae789.jpg"}
            ]
            for cert in certifications:
                st.write(f"[{cert['name']}]({cert['link']})")

if selected == 'Project':
    st.header("My Projects")
    with st.container():
        col5, col6 = st.columns((1, 2))
        with col5:
            st.image("https://a.storyblok.com//f/106061/2560x1446/2fa10839b7/into-the-metaverse-how-ar-vr-are-revolutionising-gaming.jpg/m/3840x0/filters:quality(75)")
        with col6:
            st.subheader("VIRTUAL ARMORY: IMMERSIVE EXPLORING MILITARY OBJECT IN VR")
            st.write("""
            Description: The project aiming to enhance the educational experience for pupils in 
            the National Cadet Corps (NCC) is a multifaceted initiative designed to immerse students in a comprehensive virtual learning environment.

            Technologies Used:
            - Unity Development
            - 3D Modeling and Design
            - C# Programming
            - Interactive Mechanics 

            [Project Link](https://drive.google.com/drive/folders/1P7An94aq0jkz_1BdhNpQyFtMpM9IGMGu?usp=drive_link)
            """)

    with st.container():
        st.write("##")
        col7, col8 = st.columns((1, 2))
        with col7:
            st.image("https://www.collidu.com/media/catalog/product/img/2/6/264daf6f89210308410d11c868f172f22a5368509e816157d95fb4ce3d6fc4f9/hospital-management-system-slide1.png")
        with col8:
            st.subheader("Hospital Management System")
            st.write("""
            Description: This project involves creating a comprehensive hospital management system 
            that can handle patient records.
            
            Technologies Used:
            - Python
            - Tkinter
            - MySQL
            
            [Project Link](https://github.com/ARAVINDANS25/Python_and_SQL-project/blob/main/Hospital%20Management%20System.ipynb)
            """)
    st.write("---")

    with st.container():
        col9, col10 = st.columns((1, 2))
        with col9:
            st.image("https://emeritus.org/in/wp-content/uploads/sites/3/2023/01/What-is-machine-learning-Definition-types.jpg.optimal.jpg")
        with col10:
            st.subheader("Diverse Machine Learning Approaches for Effective Malware Detection")
            st.write("""
            Description: This project involves developing a machine learning model to detect Android malware based on permissions and API calls.

            Technologies Used:
            - Python
            - Machine Learning (Random Forest, Decision Trees, Logistic Regression, SVM, KNN)
            - Frequent Pattern Growth (FP-growth) Algorithm
            - Association Rule Mining
            - Datasets: Drebin and Malgenome

            [Project Link](https://github.com/ARAVINDANS25/Data-science-and-ML/blob/main/Android%20Malware%20Detection.ipynb)
            """)

if selected == 'Contacts':
    with st.container():
        st.header("Contact Me")
        st.write("""
        Feel free to reach out to me through any of the following platforms:
        
        - [LinkedIn](https://www.linkedin.com/in/aravindan-s25/)
        - [GitHub](https://github.com/ARAVINDANS25)
        - [Email](mailto:aravindans2503@gmail.com)
        """)

        st.write("##")
        st.subheader("Or send me a message directly:")
        
        contact_form = """
        <form action="https://formsubmit.co/aravindans2503@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
