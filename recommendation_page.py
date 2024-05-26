import pickle
import streamlit as st

def recommendation():
    courses_list = pickle.load(open('courses.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    def recommend(course):
        index = courses_list[courses_list['course_name'] == course].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_course_names = []
        for i in distances[1:7]:
            course_name = courses_list.iloc[i[0]].course_name
            recommended_course_names.append(course_name)
        return recommended_course_names

    course_list = courses_list['course_name'].values
    selected_course = st.selectbox(
        "Type or select a course you like:",
        course_list
    )

    if st.button('Show Recommended Courses'):
        st.write("Recommended Courses based on your interests are:")
        recommended_course_names = recommend(selected_course)
        for course_name in recommended_course_names:
            st.text(course_name)
        st.text(" ")
        st.markdown("<h6 style='text-align: center; color: red; background-color:white'>Prepared By Hassan Ali & FYP Team Members (Ahmed Kamal & Sheryar)</h6>", unsafe_allow_html=True)
