import os
import streamlit as st
from google import genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="WAPDA Smart Complaint Portal", page_icon="⚡", layout="wide")

# --- SESSION STATE (Page Router) ---
if "page" not in st.session_state:
    st.session_state.page = "landing"

# URL Query Parameter Router
query_params = st.query_params
if "nav" in query_params:
    target_page = query_params["nav"]
    st.query_params.clear()
    st.session_state.page = target_page
    st.rerun()

def switch_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# ==============================================================================
# 🎯 PAGE 1: LANDING PAGE (PERFECT CIRCLES WITH SPINNING NEON RINGS & CSS FIXES)
# ==============================================================================
if st.session_state.page == "landing":
    
# CRITICAL: No spaces at the start of any line inside st.markdown to prevent code-block escaping
    st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"], [data-testid="stMainSpaceBlockContainer"] {
    max-height: 100vh !important;
    overflow: hidden !important;
}

/* --- COMPLAINT INPUT FIELDS & LABELS COLOR VISIBILITY FIX --- */
.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] div {
    color: #ffffff !important;
    background-color: #1c83e1 !important;
    border: 1px solid #1c83e1 !important;
}
.stTextInput label, .stTextArea label, .stSelectbox label {
    color: #ffffff !important;
    font-weight: 600 !important;
}

.block-container {
    padding-top: 3.5rem !important;
    padding-bottom: 0rem !important;
}

.portal-header-box {
    text-align: center;
    margin-bottom: 60px !important;
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

.custom-circles-row {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 60px;
    width: 100%;
    max-width: 1000px;
    margin: 0 auto !important;
}

.glowing-circle-btn {
    position: relative;
    width: 180px;
    height: 180px;
    border-radius: 50%;
    background: var(--bg-fill-color) !important;
    box-shadow: inset 0 0 25px var(--bg-fill-color), 0 0 15px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-decoration: none !important;
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* Base style for the spinning animated outer border */
.glowing-circle-btn::before {
    content: '';
    position: absolute;
    top: -4px; left: -4px; right: -4px; bottom: -4px;
    border-radius: 50%;
    padding: 4px;
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    animation: spinOuterRing 3s linear infinite;
    pointer-events: none;
}

/* Explicit color mapping for the spinning rings */
.blue-ring::before { background: linear-gradient(0deg, transparent, transparent, #1c83e1); }
.green-ring::before { background: linear-gradient(0deg, transparent, transparent, #2e7d32); }
.orange-ring::before { background: linear-gradient(0deg, transparent, transparent, #ef6c00); }

@keyframes spinOuterRing {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.glowing-circle-btn:hover {
    transform: scale(1.06);
    box-shadow: inset 0 0 35px var(--bg-fill-color), 0 0 25px var(--bg-fill-color);
}

.inner-circle-icon {
    font-size: 32px;
    margin-bottom: 8px;
}

.inner-circle-text {
    font-size: 16px;
    font-weight: 700;
    line-height: 1.3;
    text-align: center;
    color: #11111 !important;
}
</style>
""", unsafe_allow_html=True)

    # Header Render
    st.markdown("""
<div class="portal-header-box">
    <div class="portal-main-heading">⚡ WAPDA Smart Complaint Portal</div>
    <div class="portal-sub-heading">AI Powered Electricity Complaint System</div>
</div>
""", unsafe_allow_html=True)
    
    # Circles Interface Row Render
    st.markdown("""
<div class="custom-circles-row">
    <a href="?nav=dashboard" target="_self" class="glowing-circle-btn blue-ring" style="--bg-fill-color: rgba(28, 131, 225, 0.12);">
        <div class="inner-circle-icon">📝</div>
        <div class="inner-circle-text">Easy<br>Complaint</div>
    </a>
    <a href="?nav=aboutme" target="_self" class="glowing-circle-btn green-ring" style="--bg-fill-color: rgba(46, 125, 50, 0.12);">
        <div class="inner-circle-icon">👤</div>
        <div class="inner-circle-text">About<br>Me</div>
    </a>
    <a href="?nav=aboutweb" target="_self" class="glowing-circle-btn orange-ring" style="--bg-fill-color: rgba(239, 108, 0, 0.12);">
        <div class="inner-circle-icon">🌐</div>
        <div class="inner-circle-text">About<br>Website</div>
    </a>
</div>
""", unsafe_allow_html=True)


# ==============================================================================
# 💻 PAGE 2: MAIN COMPLAINT DASHBOARD (ALL EXTENDED OPTIONS INCLUDED)
# ==============================================================================
elif st.session_state.page == "dashboard":
    # CSS injection for dashboard sub-page background and input visibility
    st.markdown("""
<style>
.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] div {
    color: #ffffff !important;
    background-color: #1c83e1 !important;
    border: 1px solid #1c83e1 !important;
}
.stTextInput label, .stTextArea label, .stSelectbox label {
    color: #111111 !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

    top_col1, top_col2 = st.columns([8, 2])
    with top_col1:
        st.markdown("<h2 style='margin:0; color:#111111;'>⚡ Dashboard Control Panel</h2>", unsafe_allow_html=True)
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
        
        # 🌟 NEW EXPANDED WAPDA COMPLAINT OPTIONS
        complaint_type_input = st.selectbox("Type", options=[
            "Power Outage (Load Shedding / Line Fault)", 
            "Low Voltage / High Voltage Fluctuations",
            "Transformer Breakdown / Oil Leakage / Sparking", 
            "Defective Meter / Fast Running Meter / Screen Blank", 
            "Billing Issues (Wrong Reading / Double Charging / Installments Request)",
            "Power Theft Reporting (Kunda system / Illegal bypass)",
            "New Connection Delay / Pole Installation Request"
        ])
        
        complaint_input = st.text_area("Complaint Details", height=150)
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

    image_filename = "my_picture.jpg"

    # Profile Card Card Container
    st.markdown('<div style="background-color: #11141a; border: 2px solid #2e7d32; padding: 35px; border-radius: 20px; max-width: 700px; margin: 0 auto; box-shadow: 0px 0px 25px rgba(46,125,50,0.3);">', unsafe_allow_html=True)

    # Image column layout without breaking markdown strings
    img_col1, img_col2, img_col3 = st.columns([3, 2, 3])
    with img_col2:
        if os.path.exists(image_filename):
            st.image(image_filename, use_container_width=True)
        else:
            st.markdown('<div style="text-align:center; font-size:60px; background:#222; border-radius:50%; width:120px; height:120px; line-height:120px; margin:0 auto; border:3px solid #2e7d32; color:#2e7d32;">👤</div>', unsafe_allow_html=True)

    # Text content combined tightly inside one single block to avoid raw code printing
    st.markdown("""<div style="text-align: center; margin-top: 15px;">
<h1 style="color: #2e7d32; margin-bottom: 5px; font-weight: bold; font-size: 32px;">👨‍💻 About the Developer</h1>
<p style="color: #888; font-size: 18px; font-style: italic; margin-bottom: 25px;">"Engineering Smarter Infrastructure with AI"</p>
<hr style="border-color: #2e7d32; width: 50%; margin: 0 auto 25px auto;">
</div>
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
</div>""", unsafe_allow_html=True)
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
