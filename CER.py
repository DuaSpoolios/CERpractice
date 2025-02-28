import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Hispanic Career & Education Hub", page_icon="🌍", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f8f9fa;
    }
    .main {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #0073e6;
        color: white;
        padding: 10px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #005bb5;
    }
    .header {
        color: #0073e6;
        font-weight: bold;
        font-size: 24px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Language selection
lang = st.radio("🌐 Choose Language / Elige el idioma", ["English", "Español"])

# Content dictionary
content = {
    "English": {
        "title": "🌍 Welcome to the Hispanic Career & Education Hub",
        "intro": "Find free resources for jobs, education, and legal support in Atlanta.",
        "job_title": "🔹 Job & Career Help",
        "edu_title": "📚 Education Resources",
        "legal_title": "⚖️ Legal & Immigration Help",
        "button_text": "Visit Resource",
    },
    "Español": {
        "title": "🌍 Bienvenido al Centro de Carreras y Educación Hispano",
        "intro": "Encuentra recursos gratuitos para empleos, educación y apoyo legal en Atlanta.",
        "job_title": "🔹 Ayuda para el empleo y la carrera",
        "edu_title": "📚 Recursos educativos",
        "legal_title": "⚖️ Ayuda legal e inmigración",
        "button_text": "Visitar Recurso",
    }
}

# Display main content inside a styled container
st.markdown('<div class="main">', unsafe_allow_html=True)

st.title(content[lang]["title"])
st.write(content[lang]["intro"])

# Organizing content into three columns
col1, col2, col3 = st.columns(3)

# Job & Career Section
with col1:
    st.markdown(f'<p class="header">{content[lang]["job_title"]}</p>', unsafe_allow_html=True)
    if st.button("🔹 Goodwill Job Training"):
        st.markdown("[Goodwill Job Training](https://www.goodwillng.org/job-training)", unsafe_allow_html=True)
    if st.button("🔹 Georgia WorkSource"):
        st.markdown("[Georgia WorkSource](https://www.worksourceatlanta.org/)", unsafe_allow_html=True)
    if st.button("🔹 Resume Templates (Canva)"):
        st.markdown("[Resume Templates](https://www.canva.com/resumes/templates/)", unsafe_allow_html=True)
    if st.button("🔹 Latino Jobs Network"):
        st.markdown("[Latino Jobs Network](https://latinojobsnetwork.com/)", unsafe_allow_html=True)

# Education Section
with col2:
    st.markdown(f'<p class="header">{content[lang]["edu_title"]}</p>', unsafe_allow_html=True)
    if st.button("📚 Atlanta Technical College ESL"):
        st.markdown("[Atlanta Technical College ESL](https://www.atlantatech.edu/)", unsafe_allow_html=True)
    if st.button("📚 GED Classes in Atlanta"):
        st.markdown("[GED Classes](https://www.ged.com/)", unsafe_allow_html=True)
    if st.button("📚 Free English Classes in GA"):
        st.markdown("[Free English Classes](https://www.esl.com/resources/georgia/)", unsafe_allow_html=True)

# Legal & Immigration Help Section
with col3:
    st.markdown(f'<p class="header">{content[lang]["legal_title"]}</p>', unsafe_allow_html=True)
    if st.button("⚖️ Georgia Latino Alliance for Human Rights"):
        st.markdown("[GLAHR](https://glahr.org/)", unsafe_allow_html=True)
    if st.button("⚖️ Atlanta Legal Aid"):
        st.markdown("[Atlanta Legal Aid](https://atlantalegalaid.org/)", unsafe_allow_html=True)
    if st.button("⚖️ USCIS Work Authorization"):
        st.markdown("[USCIS Work Authorization](https://www.uscis.gov/working-in-the-united-states)", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Closing main container
