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
# 🎯 PAGE 1: LANDING PAGE (NATIVE BUTTONS TRANSFORMED TO GLOWING ROW CIRCLES)
# ==============================================================================
if st.session_state.page == "landing":
    
    # Super strong CSS selectors to force native Streamlit buttons into glowing row circles
    st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMainSpaceBlockContainer"] {
        max-height: 100vh !important;
        overflow: hidden !important;
    }
    
    .block-container {
        padding-top: 3.5rem !important;
        padding-bottom: 0rem !important;
    }

    /* Centered Header Layout Setup */
    .portal-header-box {
        text-align: center;
        margin-bottom: 55px !important;
        width: 100%;
    }
    
    .portal-main-heading {
        background: linear-gradient(45deg, #1c83e1, #2e7d32, #ef6c00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 46px;
        font-weight: 800;
        margin: 0;
    }
    
    .portal-sub-heading {
        color: #666;
        font-size: 18px;
        font-weight: 500;
        margin-top: 6px;
    }

    /* Force Streamlit horizontal block layout to behave like a strict aligned row */
    [data-testid="stHorizontalBlock"] {
        max-width: 900px !important;
        margin: 0 auto !important;
        gap: 50px !important;
        display: flex !important;
        flex-direction: row !important;
        justify-content: center !important;
        align-items: center !important;
    }

    [data-testid="column"] {
        width: 180px !important;
        flex: none !important;
    }

    /* Custom Unique Key Wrapper styling to host spinning neon borders and inside fill glows */
    .circle-node-blue, .circle-node-green, .circle-node-orange {
        position: relative;
        width: 170px;
        height: 170px;
        border-radius: 50%;
        margin: 0 auto !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* Specific continuous background tinting animations */
    .circle-node-blue { background: rgba(28, 131, 225, 0.12) !important; box-shadow: inset 0 0 20px rgba(28, 131, 225, 0.2); }
    .circle-node-green { background: rgba(46, 125, 50, 0.12) !important; box-shadow: inset 0 0 20px rgba(46, 125, 50, 0.2); }
    .circle-node-orange { background: rgba(239, 108, 0, 0.12) !important; box-shadow: inset 0 0 20px rgba(239, 108, 0, 0.2); }

    /* Ring Generators targeting outer layout bounds */
    .circle-node-blue::before, .circle-node-green::before, .circle-node-orange::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        border-radius: 50%;
        padding: 3.5px;
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        animation: spinFullCircle 2.5s linear infinite;
        pointer-events: none;
    }

    .circle-node-blue::before { background: linear-gradient(0deg, transparent, transparent, #1c83e1); }
    .circle-node-green::before { background: linear-gradient(0deg, transparent, transparent, #2e7d32); }
    .circle-node-orange::before { background: linear-gradient(0deg, transparent, transparent, #ef6c00); }

    @keyframes spinFullCircle {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* Target native Streamlit Button inside our wrappers to completely fit and go circular */
    div[class^="circle-node-"] div.stButton {
        width: 100% !important;
        height: 100% !important;
        margin: 0px !important;
        padding: 0px !important;
    }

    div[class^="circle-node-"] div.stButton > button {
        width: 100% !important;
        height: 100% !important;
        border-radius: 50% !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: #222 !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        line-height: 1.4 !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: pre-line !important;
        cursor: pointer !important;
        margin: 0 !important;
        transition: transform 0.2s ease;
    }

    div[class^="circle-node-"] div.stButton > button:hover {
        transform: scale(1.05);
    }

    div[class^="circle-node-"] div.stButton > button:active,
    div[class^="circle-node-"] div.stButton > button:focus {
        background: transparent !important;
        box-shadow: none !important;
        border: none !important;
    }

    @media (prefers-color-scheme: dark) {
        div[class^="circle-node-"] div.stButton > button { color: #ffffff !important; }
    }
    </style>
    """, unsafe_allow_html=True)

    # Header Construction
    st.markdown("""
    <div class="portal-header-box">
        <div class="portal-main-heading">⚡ WAPDA Smart Complaint Portal</div>
        <div class="portal-sub-heading">AI Powered Electricity Complaint System</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 3-Column Layout execution
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="circle-node-blue">', unsafe_allow_html=True)
        if st.button("📝\n\nEasy\nComplaint", key="native_btn_dash"):
            switch_page("dashboard")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="circle-node-green">', unsafe_allow_html=True)
        if st.button("👤\n\nAbout\nMe", key="native_btn_me"):
            switch_page("aboutme")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="circle-node-orange">', unsafe_allow_html=True)
        if st.button("🌐\n\nAbout\nWebsite", key="native_btn_web"):
            switch_page("aboutweb")
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
