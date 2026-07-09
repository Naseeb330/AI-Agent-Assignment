from google import genai
import os
import streamlit as st

# API Key load karein
api_key = os.environ.get("GEMINI_API_KEY")

# Client initialize karein (Naya Google GenAI SDK)
client = genai.Client(api_key=api_key)

# Test connection (raat wala check)
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Hello, introduce yourself"
    )
    print("API connected successfully")
except Exception as e:
    print(f"API Connection Error: {e}")

# Shikayat darj karne ka main function (Aapka original logic)
def register_complaint(name, consumer_id, phone, city, complaint_type, complaint):
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

Reply professionally.

Mention:

Complaint Status
Concerned Company
Priority
Estimated Time
Recommendation
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Maazrat, koi takneeki masla aa gaya hai: {str(e)}"

# --- STREAMLIT UI DESIGN (Gradio Layout ki tarah) ---
st.set_page_config(page_title="WAPDA Smart Complaint Portal", page_icon="⚡", layout="wide")

# Center Aligned Headers (Gradio ki tarah Markdown text)
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

# Gradio ke row/column structure ko Streamlit ke columns mein badla
col1, col2 = st.columns(2)

# --- LEFT COLUMN (Form Inputs) ---
with col1:
    st.subheader("📋 Consumer Form")
    name = st.text_input("👤 Consumer Name")
    consumer_id = st.text_input("🆔 Consumer ID")
    phone = st.text_input("📞 Mobile Number")
    
    city = st.selectbox(
        "🏙️ City",
        options=["Quetta", "Lahore", "Islamabad", "Karachi", "Peshawar", "Multan", "Hyderabad", "Sukkur"]
    )
    
    complaint_type = st.selectbox(
        "⚡ Complaint Type",
        options=["Power Outage", "Low Voltage", "High Voltage", "Billing Issue", "Meter Fault", "Transformer Fault"]
    )
    
    complaint = st.text_area("📝 Complaint", height=150)
    
    submit = st.button("📤 Register Complaint", use_container_width=True)

# --- RIGHT COLUMN (Output Status) ---
with col2:
    st.subheader("📋 Complaint Status")
    
    # Jab tak button click nahi hoga, default text dikhega
    if submit:
        if name.strip() == "" or consumer_id.strip() == "":
            st.error("Meharbani karke Consumer Name aur ID zaroor likhein.")
        else:
            with st.spinner("WAPDA Agent aapki shikayat ka jaiza le raha hai..."):
                result = register_complaint(name, consumer_id, phone, city, complaint_type, complaint)
                
            # Response ko aik khoobsurat box mein dikhane ke liye st.info ka istemal
            st.info(result)
    else:
        st.write("Aapka response yahan nazar aayega jab aap form submit karenge.")
