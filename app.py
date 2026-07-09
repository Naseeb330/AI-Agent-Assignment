from google import genai
import os
import streamlit as st

# API Key load karein
api_key = os.environ.get("GEMINI_API_KEY")

# Client initialize karein (Naya Google GenAI SDK)
client = genai.Client(api_key=api_key)

# AI Agent ka function
def chat_with_agent(user_message):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message,
            config={
                "system_instruction": (
                    "Aap WAPDA ke aala afsar aur aik behtareen AI Assistant hain. "
                    "Aapka kaam sarfeen (users) ki bijli se mutaliq shikayaat (complaints) "
                    "suna, unhein darj karna, aur unka hal batana hai. "
                    "Hamesha urdu zubaan mein, nihayat hi tameez, khuloos aur adab se baat karein. "
                    "Aapka naam 'WAPDA Smart Support Agent' hai."
                )
            }
        )
        return response.text
    except Exception as e:
        return f"Maazrat, koi takneeki masla aa gaya hai: {str(e)}"

# --- STREAMLIT UI ---
st.set_page_config(page_title="WAPDA Smart Complaint Portal", page_icon="⚡")

st.title("⚡ WAPDA Smart Complaint Portal")
st.write("Khush aamdeed! Aap bijli se mutaliq apni shikayat niche darj kar sakte hain.")

# Chat history ya state initialize karein
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input form
user_input = st.text_input("Apni shikayat ya sawal yahan likhein:", key="user_input_field")

if st.button("Shikayat Darj Karein"):
    if user_input.strip() != "":
        # AI se jawab lein
        with st.spinner("WAPDA Agent jawab likh raha hai..."):
            bot_reply = chat_with_agent(user_input)
        
        # History mein add karein
        st.session_state.chat_history.append((user_input, bot_reply))

# History display karein (Naye messages upar aayenge)
if st.session_state.chat_history:
    st.write("### 💬 Aapki Guftagu:")
    for user_msg, bot_msg in reversed(st.session_state.chat_history):
        st.info(f"**Aap:** {user_msg}")
        st.success(f"**WAPDA Support Agent:** {bot_msg}")
