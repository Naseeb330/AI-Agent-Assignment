from google import genai
import os
import streamlit as st

# --- STREAMLIT UI DESIGN ---
st.set_page_config(page_title="WAPDA Smart Complaint Portal", page_icon="⚡", layout="wide")

# Center Aligned Headers
st.markdown("""
<div style="text-align:center">
    <h3 style="color:#ff4b4b;">⚠️ Note: This is Only for Educational Purpose</h3>
    <h4 style="color:#555;">By Naseeb U Rahman</h4>
    <h1 style="margin-top:-10px;">⚡ WAPDA Smart Complaint Portal</h1>
    <h3 style="color:#1c83e1; margin-top:-10px;">AI Powered by Google Gemini</h3>
    <p>Welcome! Please fill the details below.</p>
    <hr>
</div>
""", unsafe_allow_html=True)

# Shikayat darj karne ka function
def register_complaint(name, consumer_id, phone, city, complaint_type, complaint):
    api_key_fresh = os.environ.get("GEMINI_API_KEY")
    
    if not api_key_fresh:
        return "Error: Streamlit secrets mein GEMINI_API_KEY nahi mili. Kripya check karein!"
        
    try:
        client_fresh = genai.Client(api_key=api_key_fresh)
        
        # Is prompt mein start aur end dono ke liye strict structures lagaye hain
        prompt = f"""
You are an AI assistant for Pakistan's electricity complaint system.

Customer Details:
Name: {name}
Consumer ID: {consumer_id}
Phone: {phone}
City: {city}

Complaint Type:
{complaint_type}

Complaint:
{complaint}

Reply professionally based on the specific complaint type provided.

STARTING RULE: You MUST start your response with a professional greeting addressing the customer by their name, for example: "Dear {name}," followed by a short acknowledgment sentence on a new line.

FORMATTING RULE: After the greeting, leave a line break and list these exact sections. Each section MUST start on a brand NEW LINE:
- **Complaint Status:** [Details]
- **Concerned Company:** [Details]
- **Priority:** [Details]
- **Estimated Time:** [Details]
- **Recommendation:** [Details]

CLOSING RULE:
1. Write a unique, professional closing sentence that matches the complaint type. Do NOT repeat the exact same closing sentence for different types of complaints.
2. Put a double line break after the closing sentence.
3. At the very end, you MUST sign off in separate lines exactly like this (ensure your name is on its own separate line):

Sincerely,

AI Assistant Pakistan's Electricity Complaint System

By: Naseeb U Rahman
"""
        response = client_fresh.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Maazrat, koi takneeki masla aa gaya hai: {str(e)}"

# Two-Column Layout
col1, col2 = st.columns(2)

# --- LEFT COLUMN (Form Inputs) ---
with col1:
    st.subheader("📋 Consumer Form")
    name_input = st.text_input("👤 Consumer Name")
    consumer_id_input = st.text_input("🆔 Consumer ID")
    phone_input = st.text_input("📞 Mobile Number")
    
    city_input = st.selectbox(
        "🏙️ City",
        options=["Quetta", "Lahore", "Islamabad", "Karachi", "Peshawar", "Multan", "Hyderabad", "Sukkur"]
    )
    
    complaint_type_input = st.selectbox(
        "⚡ Complaint Type",
        options=["Power Outage", "Low Voltage", "High Voltage", "Billing Issue", "Meter Fault", "Transformer Fault"]
    )
    
    complaint_input = st.text_area("📝 Complaint", height=150)
    
    submit = st.button("📤 Register Complaint", use_container_width=True)

# --- RIGHT COLUMN (Output Status) ---
with col2:
    st.subheader("📋 Complaint Status")
    
    if submit:
        if name_input.strip() == "" or consumer_id_input.strip() == "":
            st.error("Meharbani karke Consumer Name aur ID zaroor likhein.")
        else:
            result = register_complaint(name_input, consumer_id_input, phone_input, city_input, complaint_type_input, complaint_input)
            st.info(result)

# --- FOOTER ---
st.markdown("""
<br><br><br>
<hr>
<div style="text-align:center; color:#555; padding:10px;">
    <p style="font-size:16px; font-weight:bold; margin:0;">
        ⚡ AI Assistant: Pakistan's Electricity Complaint System
    </p>
    <p style="font-size:14px; font-style:italic; margin:5px 0 0 0; color:#1c83e1;">
        Developed by: Naseeb U Rahman
    </p>
</div>
""", unsafe_allow_html=True)
