from google import genai
import os
import streamlit as st

# --- PAGE CONFIG (Absolute Fullscreen, No Scrolls) ---
st.set_page_config(page_title="WAPDA Smart Complaint Portal", page_icon="⚡", layout="wide")

# --- SESSION STATE (Page Router) ---
if "page" not in st.session_state:
    st.session_state.page = "landing"

def switch_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# ==============================================================================
# 🎯 PAGE 1: ULTIMATE FIXED LANDING PAGE (TRANSPARENT CENTERS & FUNCTIONAL)
# ==============================================================================
if st.session_state.page == "landing":
    
    # Powerful CSS layout overrides to ensure text fits inside spinning objects natively
    st.markdown("""
    <style>
    /* Complete scroll bar elimination */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMainSpaceBlockContainer"] {
        max-height: 100vh !important;
        overflow: hidden !important;
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
    }

    /* Master Container to Force absolute centering of Title + Elements */
    .master-center-layout {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin: 0 auto;
    }
    
    /* Clean Centered Header Block */
    .header-block {
        margin-bottom: 30px;
    }
    
    .main-heading {
        background: linear-gradient(45deg, #1c83e1, #2e7d32, #ef6c00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 48px;
        font-weight: 800;
        margin: 0px 0px 5px 0px;
        display: inline-block;
    }
    
    .sub-heading {
        color: #666;
        font-size: 19px;
        font-weight: 500;
        margin: 0;
    }

    /* Absolute Native Custom Dynamic Core Button Overwrite */
    div.stButton > button {
        position: relative !important;
        width: 170px !important;
        height: 170px !important;
        border-radius: 50% !important;
        background: transparent !important; /* NO SOLID COLORS INSIDE */
        border: none !important;
        box-shadow: none !important;
        color: inherit !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        cursor: pointer !important;
        margin: 0 auto !important;
        z-index: 5 !important;
        transition: transform 0.2s ease;
    }
    
    div.stButton > button:hover {
        transform: scale(1.05);
        background: transparent !important;
        border: none !important;
    }

    /* Custom Wrapper frame to hold spinning glowing ring behind the native button */
    .spinning-frame-wrapper {
        position: relative;
        width: 170px;
        height: 170px;
        margin: 0 auto;
    }

    .spinning-glow-ring {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: linear-gradient(0deg, transparent, transparent, var(--neon-color));
        animation: spinObject 2s linear infinite;
        z-index: 1;
        pointer-events: none; /* Let clicks pass straight to the button */
    }

    @keyframes spinObject {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* Custom Text Overlay content that will sit beautifully inside the button area */
    .button-content-wrapper {
        pointer-events: none;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .button-content-wrapper .emoji {
        font-size: 32px;
        margin-bottom: 4px;
    }

    .button-content-wrapper .label {
        font-size: 15px;
        font-weight: bold;
        color: #333; /* Clean dark text visible over light backgrounds */
        line-height: 1.2;
    }
    
    /* Dark mode support if user has a dark theme enabled */
    @media (prefers-color-scheme: dark) {
        .button-content-wrapper .label {
            color: #fff;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Building Centered Layout Framework
    st.markdown('<div class="master-center-layout">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="header-block">
        <div class="main-heading">⚡ WAPDA Smart Complaint Portal</div>
        <div class="sub-heading">AI Powered Electricity Complaint System</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="spinning-frame-wrapper">', unsafe_allow_html=True)
        # Soft Blue Spinning Ring Background (No Solid Center)
        st.markdown('<div class="spinning-glow-ring" style="--neon-color: #1c83e1;"></div>', unsafe_allow_html=True)
        # Native Interactive Button
        if st.button("📝\nEasy\nComplaint", key="native_dash_btn"):
            switch_page("dashboard")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="spinning-frame-wrapper">', unsafe_allow_html=True)
        # Soft Green Spinning Ring Background (No Solid Center)
        st.markdown('<div class="spinning-glow-ring" style="--neon-color: #2e7d32;"></div>', unsafe_allow_html=True)
        # Native Interactive Button
        if st.button("👤\nAbout\nMe", key="native_me_btn"):
            switch_page("aboutme")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="spinning-frame-wrapper">', unsafe_allow_html=True)
        # Soft Orange Spinning Ring Background (No Solid Center)
        st.markdown('<div class="spinning-glow-ring" style="--neon-color: #ef6c00;"></div>', unsafe_allow_html=True)
        # Native Interactive Button
        if st.button("🌐\nAbout\nWebsite", key="native_web_btn"):
            switch_page("aboutweb")
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)


# ==============================================================================
# 💻 PAGE 2: MAIN COMPLAINT DASHBOARD
# ==============================================================================
elif st.session_state.page == "dashboard":
    top_col1, top_col2 = st.columns([8, 2])
    with top_col1:
        st.markdown("<h2 style='margin:0; color:#1c83e1;'>⚡ Dashboard Control Panel</h2>", unsafe_allow_html=True)
    with top_col2:
        if st.button("🏠 Go Back Home", use_container_width=True): switch_page("landing")
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
# 👤 PAGE 3: CENTRALIZED ABOUT ME
# ==============================================================================
elif st.session_state.page == "aboutme":
    top_col1, top_col2 = st.columns([8, 2])
    with top_col1:
        st.markdown("<h2 style='margin:0; color:#2e7d32;'>👤 Profile Dashboard</h2>", unsafe_allow_html=True)
    with top_col2:
        if st.button("🏠 Go Back Home", use_container_width=True): switch_page("landing")
    st.markdown("<hr style='margin-top:5px; margin-bottom:30px;'>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #11141a; border: 2px solid #2e7d32; padding: 35px; border-radius: 20px; text-align: center; max-width: 700px; margin: 0 auto; box-shadow: 0px 0px 25px rgba(46,125,50,0.3);">
        <h1 style="color: #2e7d32; margin-bottom: 5px; font-weight: bold;">👨‍💻 About the Developer</h1>
        <p style="color: #888; font-size: 18px; font-style: italic; margin-bottom: 25px;">"Engineering Smarter Infrastructure with AI"</p>
        <hr style="border-color: #2e7d32; width: 50%; margin: 0 auto 25px auto;">
        <table style="width: 100%; font-size: 18px; color: white; border-collapse: collapse; text-align: left;">
            <tr style="border-bottom: 1px solid #222;"><td style="padding: 12px; font-weight: bold; color: #2e7d32; width: 35%;">Name:</td><td style="padding: 12px; color: #ddd;">Naseeb Marri (Naseeb U Rahman)</td></tr>
            <tr style="border-bottom: 1px solid #222;"><td style="padding: 12px; font-weight: bold; color: #2e7d32;">Role:</td><td style="padding: 12px; color: #ddd;">AI Assistant Core Developer</td></tr>
            <tr style="border-bottom: 1px solid #222;"><td style="padding: 12px; font-weight: bold; color: #2e7d32;">Department:</td><td style="padding: 12px; color: #ddd;">Student of Electrical Engineering Department</td></tr>
            <tr><td style="padding: 12px; font-weight: bold; color: #2e7d32;">Domain Interest:</td><td style="padding: 12px; color: #ddd;">Smart Grid Systems, Automation, Power Engineering & AI Integrations</td></tr>
        </table>
        <br>
        <p style="background: rgba(46,125,50,0.1); color: #4caf50; padding: 15px; border-radius: 10px; font-size: 16px; font-weight: 500; border-left: 5px solid #2e7d32; margin-top: 15px;">
            ⚡ Combining the core principles of Electrical Engineering with modern Artificial Intelligence to build automated utility solutions for Pakistan.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ==============================================================================
# 🌐 PAGE 4: ABOUT WEBSITE
# ==============================================================================
elif st.session_state.page == "aboutweb":
    top_col1, top_col2 = st.columns([8, 2])
    with top_col1:
        st.markdown("<h2 style='margin:0; color:#ef6c00;'>🌐 Portal Specifications</h2>", unsafe_allow_html=True)
    with top_col2:
        if st.button("🏠 Go Back Home", use_container_width=True): switch_page("landing")
    st.markdown("<hr style='margin-top:5px; margin-bottom:30px;'>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #11141a; border: 2px solid #ef6c00; padding: 35px; border-radius: 20px; text-align: center; max-width: 700px; margin: 0 auto; box-shadow: 0px 0px 25px rgba(239,108,0,0.3);">
        <h1 style="color: #ef6c00; margin-bottom: 5px; font-weight: bold;">🌐 About this Project</h1>
        <p style="color: #888; font-size: 18px; font-style: italic; margin-bottom: 25px;">"AI Engine Optimization for Utility Frameworks"</p>
        <hr style="border-color: #ef6c00; width: 50%; margin: 0 auto 25px auto;">
        <div style="text-align: justify; color: #ddd; font-size: 17px; line-height: 1.6; padding: 0 10px;">
            <p><strong>🎯 Educational Mission:</strong> This web portal is built as a state-of-the-art educational project demonstrating the deployment capability of Large Language Models (LLMs) in automating critical utility support services.</p>
            <p><strong>⚡ Actionable Insight Generation:</strong> The integration with Google Gemini ensures that multi-faceted complaints (such as transformer breakdowns, voltage drops, and meter defects) are evaluated instantly, returning safe procedures, realistic ETAs, and assigned priorities based on local distribution frameworks (like QESCO).</p>
            <p><strong>🛠️ Stack Integration:</strong> Engineered natively using Python, customized CSS transitions for interface scaling, and Streamlit state-routing variables.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ==============================================================================
# 👣 FOOTER
# ==============================================================================
st.markdown("""
<br><br>
<hr>
<div style="text-align:center; color:#555; padding:5px;">
    <p style="font-size:14px; font-weight:bold; margin:0;">
        ⚡ AI Assistant: Pakistan's Electricity Complaint System
    </p>
    <p style="font-size:12px; font-style:italic; margin:5px 0 0 0; color:#1c83e1;">
        Developed by: Naseeb Marri • Educational Purpose Only
    </p>
</div>
""", unsafe_allow_html=True)
