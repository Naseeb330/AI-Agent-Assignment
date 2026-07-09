from google import genai
import os
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="WAPDA Smart Complaint Portal", page_icon="⚡", layout="wide")

# --- SESSION STATE (Page Router) ---
if "page" not in st.session_state:
    st.session_state.page = "landing"

def switch_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# ==============================================================================
# 🎯 PAGE 1: STYLISH CENTRALIZED LANDING PAGE (3 CIRCLE BUTTONS)
# ==============================================================================
if st.session_state.page == "landing":
    
    # Custom CSS for perfect center alignment and grid layout
    st.markdown("""
    <style>
    .landing-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 75vh;
        text-align: center;
        width: 100%;
    }
    .main-heading {
        color: #1c83e1;
        font-size: 45px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-heading {
        color: #555;
        font-size: 20px;
        margin-bottom: 50px;
    }
    /* Dynamic Styling for the 3 Circle Buttons */
    div.stButton > button {
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 50% !important; /* Perfect Circle */
        width: 180px !important;
        height: 180px !important;
        border: 4px solid #fff !important;
        transition: all 0.3s ease-in-out !important;
        cursor: pointer !important;
        display: block;
        margin: 0 auto;
        line-height: 1.2 !important;
    }
    /* Har button ka apna alag unique color aur glow */
    /* 1. Easy Complaint (Blue) */
    .complaint-btn div.stButton > button {
        background-color: #1c83e1 !important;
        box-shadow: 0px 0px 20px rgba(28, 131, 225, 0.5) !important;
    }
    .complaint-btn div.stButton > button:hover {
        transform: scale(1.1) !important;
        box-shadow: 0px 0px 30px rgba(28, 131, 225, 0.8) !important;
        background-color: #1565c0 !important;
    }
    /* 2. About Me (Green) */
    .about-me-btn div.stButton > button {
        background-color: #2e7d32 !important;
        box-shadow: 0px 0px 20px rgba(46, 125, 50, 0.5) !important;
    }
    .about-me-btn div.stButton > button:hover {
        transform: scale(1.1) !important;
        box-shadow: 0px 0px 30px rgba(46, 125, 50, 0.8) !important;
        background-color: #1b5e20 !important;
    }
    /* 3. About Website (Orange/Amber) */
    .about-web-btn div.stButton > button {
        background-color: #ef6c00 !important;
        box-shadow: 0px 0px 20px rgba(239, 108, 0, 0.5) !important;
    }
    .about-web-btn div.stButton > button:hover {
        transform: scale(1.1) !important;
        box-shadow: 0px 0px 30px rgba(239, 108, 0, 0.8) !important;
        background-color: #e65100 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Wrapping everything in a centralized container
    st.markdown('<div class="landing-container">', unsafe_allow_html=True)
    st.markdown('<div class="main-heading">⚡ WAPDA Smart Complaint Portal</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-heading">AI Powered Electricity Complaint System</div>', unsafe_allow_html=True)
    
    # 3-Column Layout for the Circles to appear side-by-side in center
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="complaint-btn">', unsafe_allow_html=True)
        if st.button("📝\nEasy\nComplaint"):
            switch_page("dashboard")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="about-me-btn">', unsafe_allow_html=True)
        if st.button("👤\nAbout\nMe"):
            switch_page("aboutme")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="about-web-btn">', unsafe_allow_html=True)
        if st.button("🌐\nAbout\nWebsite"):
            switch_page("aboutweb")
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)


# ==============================================================================
# 💻 PAGE 2: THE ACTUAL SMART COMPLAINT DASHBOARD
# ==============================================================================
elif st.session_state.page == "dashboard":
    top_col1, top_col2 = st.columns([8, 2])
    with top_col1:
        st.markdown("<h2 style='margin:0; color:#1c83e1;'>⚡ Dashboard Control Panel</h2>", unsafe_allow_html=True)
    with top_col2:
        if st.button("🏠 Go Back Home", use_container_width=True):
            switch_page("landing")
    st.markdown("<hr style='margin-top:5px; margin-bottom:20px;'>", unsafe_allow_html=True)

    def register_complaint(name, consumer_id, phone, city, complaint_type, complaint):
        api_key_fresh = os.environ.get("GEMINI_API_KEY")
        if not api_key_fresh: return "Error: Streamlit secrets mein GEMINI_API_KEY nahi mili!"
        try:
            client_fresh = genai.Client(api_key=api_key_fresh)
            prompt = f"You are an AI assistant for Pakistan's electricity complaint system. Customer Details: Name: {name}, ID: {consumer_id}, Phone: {phone}, City: {city}. Type: {complaint_type}. Complaint: {complaint}. Reply professionally. Heading and description text on SAME line. Double spacing BETWEEN sections. Sincerely, AI Assistant, By: Naseeb U Rahman"
            response = client_fresh.models.generate_content(model="gemini-2.5-flash", contents=prompt)
            return response.text
        except Exception as e: return f"Maazrat: {str(e)}"

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📋 Consumer Form")
        name_input = st.text_input("👤 Consumer Name")
        consumer_id_input = st.text_input("🆔 Consumer ID")
        phone_input = st.text_input("📞 Mobile Number")
        city_input = st.selectbox("City", options=["Quetta", "Lahore", "Islamabad", "Karachi"])
        complaint_type_input = st.selectbox("Type", options=["Power Outage", "Low Voltage", "High Voltage"])
        complaint_input = st.text_area("Complaint", height=150)
        submit = st.button("📤 Register Complaint", use_container_width=True)

    with col2:
        st.subheader("📋 Complaint Status")
        if submit:
            if name_input.strip() == "" or consumer_id_input.strip() == "": st.error("Name & ID are required.")
            else:
                with st.spinner("Processing..."): result = register_complaint(name_input, consumer_id_input, phone_input, city_input, complaint_type_input, complaint_input)
                st.markdown(result)


# ==============================================================================
# 👤 PAGE 3: ABOUT ME (Naseeb Marri Details)
# ==============================================================================
elif st.session_state.page == "aboutme":
    top_col1, top_col2 = st.columns([8, 2])
    with top_col1:
        st.markdown("<h2 style='margin:0; color:#2e7d32;'>👤 About the Developer</h2>", unsafe_allow_html=True)
    with top_col2:
        if st.button("🏠 Go Back Home", use_container_width=True): switch_page("landing")
    st.markdown("<hr style='margin-top:5px;'>", unsafe_allow_html=True)
    
    # Grid/Card design for About Me Section
    st.info("""
    ### 👨‍💻 Developer Profile
    * **Name:** Naseeb Marri (Naseeb U Rahman)
    * **Role:** AI Assistant Core Developer 
    * **Department:** Student of Electrical Engineering Department
    * **Domain Interest:** Smart Grid Systems, Power Engineering, and Artificial Intelligence (AI) Integrations.
    
    *“Combining the principles of Electrical Engineering with modern Artificial Intelligence to build smart utilities for Pakistan.”*
    """)


# ==============================================================================
# 🌐 PAGE 4: ABOUT WEBSITE (Project Mission)
# ==============================================================================
elif st.session_state.page == "aboutweb":
    top_col1, top_col2 = st.columns([8, 2])
    with top_col1:
        st.markdown("<h2 style='margin:0; color:#ef6c00;'>🌐 About this Project</h2>", unsafe_allow_html=True)
    with top_col2:
        if st.button("🏠 Go Back Home", use_container_width=True): switch_page("landing")
    st.markdown("<hr style='margin-top:5px;'>", unsafe_allow_html=True)
    
    st.warning("""
    ### ⚡ WAPDA Smart Complaint Portal
    * **Purpose:** This web portal is an **Educational Project** designed to demonstrate how Large Language Models (LLMs) like Google Gemini can automate and optimize utility customer support systems.
    * **Core Feature:** It dynamically analyzes power complaints (like low voltage, billing issues, faults) and generates high-priority actionable solutions instantly based on Pakistani electric supply companies (like QESCO, LESCO, etc.).
    * **Tech Stack:** Python, Streamlit UI framework, Google GenAI SDK, and Custom CSS Injection.
    """)


# ==============================================================================
# 👣 FOOTER
# ==============================================================================
st.markdown("""
<br><br><br>
<hr>
<div style="text-align:center; color:#555; padding:10px;">
    <p style="font-size:14px; font-weight:bold; margin:0;">
        ⚡ AI Assistant: Pakistan's Electricity Complaint System
    </p>
    <p style="font-size:12px; font-style:italic; margin:5px 0 0 0; color:#1c83e1;">
        Developed by: Naseeb Marri • Educational Purpose Only
    </p>
</div>
""", unsafe_allow_html=True)
