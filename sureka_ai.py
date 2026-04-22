import streamlit as st
import os
from openai import OpenAI

# ==============================
# 🔐 API KEY
# ==============================
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ==============================
# 🎨 PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Sureka AI Assistant",
    page_icon="🎨",
    layout="centered"
)

# ==============================
# 🎨 CSS
# ==============================
st.markdown("""
<style>

/* Hide Streamlit branding */
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stDecoration"] {display: none;}

/* Fix top spacing */
.block-container {
    padding-top: 3.5rem !important;
}

/* Title */
.big-title {
    font-size: 32px;
    font-weight: bold;
    text-align: center;
    color: #7b61ff;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #aaa;
}

/* Input */
.stTextInput input {
    padding: 12px !important;
    border-radius: 12px !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #7b61ff, #9c27b0);
    color: white;
    border-radius: 12px;
    height: 50px;
    font-weight: bold;
}

/* Mobile fix */
@media (max-width: 768px) {
    .stButton {
        margin-top: -10px !important;
    }
}

/* Response */
.response-box {
    background: #F2DDE3;
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
    color: #333;
    border: 1px solid #e5bfc8;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# 🎯 HEADER
# ==============================
st.markdown('<div class="big-title">🎨 Sureka Designz AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Get instant design price & replies ⚡</div>', unsafe_allow_html=True)

st.divider()

# ==============================
# 💬 INPUT
# ==============================
st.markdown("💬 Ask anything (logo, website, SEO, etc)")

user_input = st.text_input("", placeholder="Type your requirement...")

ask_btn = st.button("🚀 Get Quote", use_container_width=True)

# ==============================
# 🤖 RESPONSE LOGIC
# ==============================
if ask_btn and user_input:

    text = user_input.lower()

    # 🔥 CONTACT DETECTION
    if any(word in text for word in ["number", "contact", "phone", "call"]):
        reply = """
Sure 😊 You can contact us at 📞 9080732938.

Or share your name & number here — our team will call you shortly and assist you 🚀
"""

    else:
        # 🤖 AI RESPONSE
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
You are an AI assistant for Sureka Designz.

Business Details:
- Logo Design: ₹1999
- Social Media Design: ₹2500 (min 10 posts)
- Website Design: ₹7999+
- Brochure Design: ₹1999 (min 4 pages)
- Print Design: ₹499
- SEO: ₹15000
- UI/UX Design: ₹12000
- Video Editing: ₹1000 (30 sec)
- Flex Banner: ₹499
- Pamphlet Design: ₹1000

Working Hours: 10 AM - 8 PM

Rules:
- Be friendly and professional
- Keep responses short
- Always try to convert into lead
"""
                },
                {"role": "user", "content": user_input}
            ]
        )

        reply = response.choices[0].message.content

    # ==============================
    # 💬 SHOW RESPONSE
    # ==============================
    st.markdown(f'<div class="response-box">{reply}</div>', unsafe_allow_html=True)

# ==============================
# 🚀 FOOTER
# ==============================
st.markdown(
    "<center>⚡ Sureka AI • Powered by Sureka Designz</center>",
    unsafe_allow_html=True
)
