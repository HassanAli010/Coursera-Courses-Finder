import streamlit as st
import pickle
from recommendation_page import recommendation
# Home Page
def home():
    st.title("Welcome to the Coursera Courses Recommendation System")
    st.write("Discover courses tailored to your interests and needs.")
    st.image("CRS.png", caption="Content Based", use_column_width=True)  # Adjust the path and caption accordingly
    
    if st.button('Read More'):
        st.markdown("## Type or Search Any Course Name:")
        st.image("part2.png", caption="How To Use Recommendations", use_column_width=True)  # Adjust the path and caption accordingly
        st.markdown("## Results of Recommendations:")
        st.image("part1.png", caption="Get Similar Courses", use_column_width=True)  # Adjust the path and caption accordingly
def features():
    st.title("Features")
    st.write("""
    - Personalized course recommendations
    - Easy-to-use interface
    - Efficient and accurate filtering using Content-Based Filtering
    """)
    st.subheader("Content-Based Filtering Algorithm")
    st.write("The algorithm analyzes course content and user preferences to provide relevant recommendations.")
    st.subheader("Benefits")
    st.write("""
    - Enhanced learning experience
    - Time-saving by finding the right courses quickly
    - Increased user satisfaction
    """)
# About Page
def about():
    st.title("About Us")
    st.write("We are a group of dedicated students passionate about machine learning and educational technology.")
    st.subheader("Project Goals")
    st.write("Our goal is to create a robust recommendation system that enhances the learning experience by providing personalized course suggestions.")
    st.subheader("Technology Stack")
    st.write("""
    - Python
    - Machine Learning (Content-Based Filtering)
    - Streamlit for web interface
    """)
# Contact Page
def contact():
    st.title("Contact")
    st.write("Have questions or feedback? Reach out to us!")
    st.write("Email: hassan7538216@gmail.com")
    st.write("Phone: +923478672004")
# FAQs Page
def faqs():
    st.title("FAQs")
    st.subheader("Frequently Asked Questions")
    faq_list = {
        "How does the recommendation system work?": "The system uses Content-Based Filtering to analyze course content and user preferences, providing personalized recommendations.",
        "What data is required to generate recommendations?": "The system requires information on user preferences, past course enrollments, and course descriptions.",
        "Is the recommendation system free to use?": "Yes, our system is completely free to use for all Coursera users.",
        "Who can I contact for support?": "If you need assistance, please reach out to us through the contact form on the Contact page."
    }
    for question, answer in faq_list.items():
        st.subheader(question)
        st.write(answer)
# Sidebar navigation
page = st.sidebar.selectbox("Navigate", ["Home", "Features", "About",  "Recommendation","Contact", "FAQs"])

# Render selected page
if page == "Home":
    home()
elif page == "Features":
    features()
elif page == "About":
    about()
elif page == "Recommendation":
    recommendation()
elif page == "Contact":
    contact()
elif page == "FAQs":
    faqs()
# Additional recommendation for layout
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            # background-color: #f4f4f4;
            background-color: #fff;
            
            padding: 10px;
            font-size: 12px;
            color: #888;
            border-top: 1px solid #ddd;
        }
    </style>
""", unsafe_allow_html=True)
