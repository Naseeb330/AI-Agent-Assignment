from google import genai
import os
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="WAPDA Smart Complaint Portal", page_icon="⚡", layout="wide")

# --- SESSION STATE (Page Router) ---
# Agar session state mein 'page' nahi hai, to pehla page 'landing' set karein
if "page" not in st.session_state:
    st.session_state.page = "landing"

# Function: Page badalne ke liye
def switch_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# ==============================================================================
# 🎯 PAGE 1: STYLISH LANDING PAGE (GOAL CIRCLE BUTTON)
# ==============================================================================
if st.session_state.page == "landing":
    
    # CSS for Stylish Centralized Glow Circle Button
    st.markdown("""
    <style>
    .landing-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 70vh;
        text-align: center;
    }
    .main-heading {
        color: #1c83e1;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sub-heading {
        color: #555;
        font-size: 18px;
        margin-bottom: 40px;
    }
    /* Invisible Streamlit Button Layer for Click Functionality */
    div.stButton > button {
        background-color: #1c83e1 !important;
        color: white !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 50% !important; /* Makes it a perfect circle */
        width: 220px !important;
        height: 220px !important;
        border: 4px solid #fff !important;
        box-shadow: 0px 0px 25px rgba(28, 131, 225, 0.6) !important;
        transition: all 0.3s ease-in-out !important;
        cursor: pointer !important;
        display: block;
        margin: 0 auto;
    }
    div.stButton > button:hover {
        transform: scale(1.1) !important;
        box-shadow: 0px 0px 35px rgba(28, 131, 225, 0.9) !important;
        background-color: #1565c0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # UI Elements inside a structured layout
    st.markdown('<div class="landing-container">', unsafe_allow_html=True)
    st.markdown('<div class="main-heading">⚡ WAPDA Smart Complaint Portal</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-heading">AI Powered Electricity Complaint System • By Naseeb U Rahman</div>', unsafe_allow_html=True)
    
    # The actual functional Circle Button
    if st.button("Easy\nComplaint"):
        switch_page("dashboard")
        
    st.markdown('</div>', unsafe_allow_html=True)


# ==============================================================================
# 💻 PAGE 2: THE ACTUAL SMART COMPLAINT DASHBOARD
# ==============================================================================
elif st.session_state.page == "dashboard":
    
    # Top Bar with a Back/Home Button
    top_col1, top_col2 = st.columns([8, 2])
    with top_col1:
        st.markdown("<h2 style='margin:0; color:#1c83e1;'>⚡ Dashboard Control Panel</h2>", unsafe_allow_html=True)
    with top_col2:
        if st.button("🏠 Go Back Home", use_container_width=True):
            switch_page("landing")
            
    st.markdown("<hr style='margin-top:5px; margin-bottom:20px;'>", unsafe_allow_html=True)

    # Shikayat darj karne ka core function (Gemini integration)
    def register_complaint(name, consumer_id, phone, city, complaint_type, complaint):
        api_key_fresh = os.environ.get("GEMINI_API_KEY")
        if not api_key_fresh:
            return "Error: Streamlit secrets mein GEMINI_API_KEY nahi mili!"
            
        try:
            client_fresh = genai.Client(api_key=api_key_fresh)
            prompt = f"""
You are an AI assistant for Pakistan's electricity complaint system.
Customer Details: Name: {name}, ID: {consumer_id}, Phone: {phone}, City: {city}
Complaint Type: {complaint_type}
Complaint: {complaint}

Reply professionally based on the specific complaint type. 
CRITICAL: Description text MUST start immediately on the same line as the bold heading. Double line breaks BETWEEN sections.

Format exactly like this:
**Complaint Status:** [Description]

**Concerned Company:** [Description]

**Priority:** [Description]

**Estimated Time:** [Description]

**Recommendation:** [Description]

Sincerely,
AI Assistant Pakistan's Electricity Complaint System
By: Naseeb U Rahman
"""
            response = client_fresh.models.generate_content(
                model="gemini-2.5-flash", contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Maazrat, koi takneeki masla aa gaya hai: {str(e)}"

    # Two-Column Layout for Dashboard
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📋 Consumer Form")
        name_input = st.text_input("👤 Consumer Name")
        consumer_id_input = st.text_input("🆔 Consumer ID")
        phone_input = st.text_input("📞 Mobile Number")
        
        city_input = st.selectbox(
            "🏙️ City", options=["Quetta", "Lahore", "Islamabad", "Karachi", "Peshawar", "Multan", "Hyderabad", "Sukkur"]
        )
        complaint_type_input = st.selectbox(
            "⚡ Complaint Type", options=["Power Outage", "Low Voltage", "High Voltage", "Billing Issue", "Meter Fault", "Transformer Fault"]
        )
        complaint_input = st.text_area("📝 Complaint", height=150)
        submit = st.button("📤 Register Complaint", use_container_width=True)

    with col2:
        st.subheader("📋 Complaint Status")
        if submit:
            if name_input.strip() == "" or consumer_id_input.strip() == "":
                st.error("Meharbani karke Consumer Name aur ID zaroor likhein.")
            else:
                with st.spinner("AI Response generate ho raha hai..."):
                    result = register_complaint(name_input, consumer_id_input, phone_input, city_input, complaint_type_input, complaint_input)
                st.markdown(result)


# ==============================================================================
# 👣 FOOTER (Sari screens par standard rahega)
# ==============================================================================
st.markdown("""
<br><br><br>
<hr>
<div style="text-align:center; color:#555; padding:10px;">
    <p style="font-size:14px; font-weight:bold; margin:0;">
        ⚡ AI Assistant: Pakistan's Electricity Complaint System
    </p>
    <p style="font-size:12px; font-style:italic; margin:5px 0 0 0; color:#1c83e1;">
        Developed by: Naseeb U Rahman • Educational Purpose Only
    </p>
</div>
""", unsafe_allow_html=True)
