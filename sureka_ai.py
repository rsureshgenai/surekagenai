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
# 🎨 CUSTOM CSS (MOBILE FIX INCLUDED)
# ==============================
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

/* Input */
.stTextInput > div > div > input {
    padding: 14px !important;
    border-radius: 12px !important;
    font-size: 16px !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #7b61ff, #9c27b0);
    color: white;
    font-weight: bold;
    border-radius: 12px;
    height: 50px;
    font-size: 16px;
}

/* MOBILE FIX: Move button UP */
@media (max-width: 768px) {
    .stTextInput {
        margin-bottom: 5px !important;
    }
    .stButton {
        margin-top: -15px !important;
    }
}

/* Title */
.big-title {
    font-size: 34px;
    font-weight: bold;
    text-align: center;
    color: #7b61ff;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #aaa;
    margin-bottom: 20px;
}

/* Response box */
.response-box {
    background: linear-gradient(90deg, #00c853, #69f0ae);
    padding: 15px;
    border-radius: 12px;
    margin-top: 15px;
    color: black;
    font-size: 16px;
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
# 💬 INPUT SECTION
# ==============================
st.markdown("### 💬 Ask anything (logo, website, SEO, etc)")

user_input = st.text_input("", placeholder="Type your requirement...")

ask_btn = st.button("🚀 Get Quote", use_container_width=True)

# ==============================
# 🤖 AI RESPONSE
# ==============================
if ask_btn and user_input:

    with st.spinner("Thinking..."):
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
- Always try to convert user into a lead
- Mention price clearly if asked
- If unclear, ask follow-up question
- Keep response short and engaging
"""
                },
                {"role": "user", "content": user_input}
            ]
        )

        reply = response.choices[0].message.content

    st.markdown(f'<div class="response-box">{reply}</div>', unsafe_allow_html=True)

st.divider()

# ==============================
# 🚀 FOOTER
# ==============================
st.markdown(
    "<center>⚡ Powered by Sureka Designz</center>",
    unsafe_allow_html=True
)
