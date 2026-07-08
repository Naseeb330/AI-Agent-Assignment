

from google import genai

print("Libraries loaded successfully")
import os

# Apni purani API key wali line ko mita kar yeh likhein:
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)  # 'api_key' ko chote harfo (lowercase) mein likhein

print("API connected")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello, introduce yourself"
)

print(response.text)
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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

with gr.Blocks(
    title="WAPDA Smart Complaint Portal"
) as demo:
    gr.Markdown("""
<div style="text-align:center">

<h1>⚠️ Note: This is Only for Educational Purpose</h3>

<h1>By Naseeb U Rahman</h4>

<h1>⚡ WAPDA Smart Complaint Portal</h1>

<h1>AI Powered by Google Gemini</h3>
""")
    gr.Markdown("""

Welcome! Please fill the details below.
""")

    with gr.Row():

        with gr.Column():

            name = gr.Textbox(label="👤 Consumer Name")

            consumer_id = gr.Textbox(label="🆔 Consumer ID")

            phone = gr.Textbox(label="📞 Mobile Number")

            city = gr.Dropdown(
                choices=[
                    "Quetta",
                    "Lahore",
                    "Islamabad",
                    "Karachi",
                    "Peshawar",
                    "Multan",
                    "Hyderabad",
                    "Sukkur"
                ],
                label="🏙️ City"
            )

            complaint_type = gr.Dropdown(
                choices=[
                    "Power Outage",
                    "Low Voltage",
                    "High Voltage",
                    "Billing Issue",
                    "Meter Fault",
                    "Transformer Fault"
                ],
                label="⚡ Complaint Type"
            )

            complaint = gr.Textbox(
                label="📝 Complaint",
                lines=6
            )

            submit = gr.Button(
                "📤 Register Complaint"
            )

        with gr.Column():

            output = gr.Markdown(
                "### 📋 Complaint Status"
            )

    submit.click(
        fn=register_complaint,
        inputs=[
            name,
            consumer_id,
            phone,
            city,
            complaint_type,
            complaint
        ],
        outputs=output
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
