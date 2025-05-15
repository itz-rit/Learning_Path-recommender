import streamlit as st
from recommender import get_recommendations

st.title("🎯 AI-Powered Learning Path Recommender")
st.write("Get skills and course suggestions based on your career interest")

user_input = st.text_input("Enter your career interest (e.g., Data Scientist, Web Developer)")

if st.button("Show Path"):
    result = get_recommendations(user_input)
    if result:
        st.success(f"Recommended path for {result['Career']}")
        st.write("**Skills to Learn:**")
        for skill in result['Skills']:
            st.markdown(f"- {skill}")
        st.write("**Courses to Take:**")
        for course in result['Courses']:
            st.markdown(f"- {course}")
    else:
        st.error("Sorry, no matching career found. Try another one.")
