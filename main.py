import pickle
import streamlit as st
import pandas as pd

# ===== Load Models =====
courses_list = pickle.load(open('models/courses.pkl', 'rb'))
similarity = pickle.load(open('models/similarity.pkl', 'rb'))

# ===== Recommendation Function =====
def recommend(course):
    index = courses_list[courses_list['course_name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_course_names = []
    for i in distances[1:7]:
        course_name = courses_list.iloc[i[0]].course_name
        recommended_course_names.append(course_name)
    return recommended_course_names


# ===== Page Configuration =====
st.set_page_config(
    page_title="EduPath 🇮🇳 - Course Recommendation System",
    page_icon="🎓",
    layout="wide"
)

# ===== Full Background + Dark Theme =====
st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"] {
            height: 100%;
            min-height: 100vh;
        }

        /* Full-screen background image with dark overlay */
        [data-testid="stAppViewContainer"] {
            background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),
                              url("https://bookuradmission.com/college_banner/Lovely%20Professional%20University%20(LPU)_banner211112102119.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center;
            background-attachment: fixed;
            color: white;
        }

        /* Fix body & layout height */
        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }

        /* Content container */
        .block-container {
            background: rgba(18, 18, 18, 0.9);
            padding: 2rem;
            border-radius: 12px;
            color: #e0e0e0;
        }

        /* Header styling */
        .title {
            color: #90caf9;
            text-align: center;
            font-size: 46px;
            font-family: 'Poppins', sans-serif;
            margin-bottom: 0;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #bdbdbd;
            margin-top: -10px;
            font-family: 'Poppins', sans-serif;
        }

        /* Course cards */
        .course-card {
            background: rgba(33, 33, 33, 0.9);
            border-radius: 12px;
            padding: 20px;
            margin: 12px 0;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
            transition: all 0.3s ease;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .course-card:hover {
            transform: scale(1.02);
            background-color: rgba(50, 50, 50, 0.95);
            box-shadow: 0px 8px 20px rgba(0,0,0,0.6);
        }
        .course-card h4 {
            color: #ffffff;
            margin-bottom: 8px;
        }
        .course-card p {
            color: #b0bec5;
            margin-top: 0;
        }

        /* Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #3949ab, #1e88e5);
            color: white;
            border-radius: 8px;
            padding: 10px 25px;
            border: none;
            font-size: 16px;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #5c6bc0, #42a5f5);
            transform: scale(1.05);
        }

        /* Footer */
        .footer {
            text-align: center;
            font-size: 13px;
            color: #9e9e9e;
            margin-top: 40px;
        }

        /* Divider line */
        hr {
            border: 1px solid rgba(255,255,255,0.2);
        }
    </style>
""", unsafe_allow_html=True)


# ===== Header Section =====
st.markdown("<h1 class='title'>🎓 EduPath – Course Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Discover the best courses from our curated Coursera dataset</p>", unsafe_allow_html=True)
st.write("<hr>", unsafe_allow_html=True)

# ===== Input Section =====
course_list = courses_list['course_name'].values
selected_course = st.selectbox("📘 Select or search for a course you like:", course_list)

# ===== Show Recommendations =====
if st.button('🔍 Show Recommended Courses'):
    st.markdown("### 📚 Recommended Courses Based on Your Interests:")
    recommended_courses = recommend(selected_course)
    for idx, course in enumerate(recommended_courses):
        st.markdown(f"""
        <div class='course-card'>
            <h4>#{idx+1} {course}</h4>
            <p>Explore similar programs offered on Coursera and related universities.</p>
        </div>
        """, unsafe_allow_html=True)

# ===== Footer =====
st.write("<hr>", unsafe_allow_html=True)
st.markdown("<p class='footer'>Made with ❤️ | EduPath © 2025 | Powered by Coursera Data</p>", unsafe_allow_html=True)
