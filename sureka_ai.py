import streamlit as st
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(
    page_title="Sureka AI Assistant",
    page_icon="🎨",
    layout="centered"
)

# ==============================
# 🎨 CUSTOM CSS (SPACING FIX)
# ==============================
st.markdown("""
<style>

/* Remove top space */
.block-container {
    padding-top: 1.5rem !important;
}

/* Title */
.big-title {
    font-size: 32px;
    font-weight: bold;
    text-align: center;
    color: #7b61ff;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #aaa;
    margin-bottom: 5px;
}

/* Divider closer */
hr {
    margin-top: 5px !important;
    margin-bottom: 10px !important;
}

/* Ask section */
.ask-title {
    margin-top: 5px;
    margin-bottom: 5px;
}

/* Input */
.stTextInput > div > div > input {
    padding: 12px !important;
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

/* MOBILE FIX */
@media (max-width: 768px) {
    .stTextInput {
        margin-bottom: 4px !important;
    }
    .stButton {
        margin-top: -10px !important;
    }
}

.response-box {
    background: linear-gradient(90deg, #00c853, #69f0ae);
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
    color: black;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# HEADER (TIGHT)
# ==============================
st.markdown('<div class="big-title">🎨 Sureka Designz AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Get instant design price & replies ⚡</div>', unsafe_allow_html=True)

st.divider()

# ==============================
# INPUT (MOVED UP)
# ==============================
st.markdown('<div class="ask-title">💬 Ask anything (logo, website, SEO, etc)</div>', unsafe_allow_html=True)

user_input = st.text_input("", placeholder="Type your requirement...")

ask_btn = st.button("🚀 Get Quote", use_container_width=True)

# ==============================
# AI RESPONSE
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

Keep answers short, friendly, and sales-focused.
"""
                },
                {"role": "user", "content": user_input}
            ]
        )

        reply = response.choices[0].message.content

    st.markdown(f'<div class="response-box">{reply}</div>', unsafe_allow_html=True)

st.markdown("<center>⚡ Powered by Sureka Designz</center>", unsafe_allow_html=True)
