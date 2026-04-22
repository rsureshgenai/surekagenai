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
# 🎨 CUSTOM CSS
# ==============================
st.markdown("""
<style>

/* Hide Streamlit branding */
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stDecoration"] {display: none;}

/* Top spacing */
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
    font-size: 16px !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #7b61ff, #9c27b0);
    color: white;
    border-radius: 12px;
    height: 50px;
    font-weight: bold;
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

/* Mobile sticky buttons */
@media (max-width: 768px) {
    .stButton {
        position: sticky;
        bottom: 70px;
        z-index: 999;
    }
    a button {
        position: sticky;
        bottom: 10px;
        z-index: 999;
    }
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
st.markdown("💬 Ask anything (logo, website, SEO, packaging, etc)")

user_input = st.text_input("", placeholder="Type your requirement...")

ask_btn = st.button("🚀 Get Quote", use_container_width=True)

# ==============================
# 🤖 RESPONSE LOGIC
# ==============================
if ask_btn and user_input:

    text = user_input.lower()

    # 📞 CONTACT QUERY (NO NUMBER DISPLAY)
    if any(word in text for word in ["number", "contact", "phone", "call"]):
        reply = """
Sure 😊 You can reach us easily using the options below.

We’re available from 10 AM to 8 PM.
Looking forward to assisting you 🚀
"""
    else:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
You are an AI assistant for Sureka Designz.

Services & Pricing:
- Logo Design: ₹1999
- Social Media Design: ₹2500 (min 10 posts)
- Website Design: ₹7999+
- Brochure Design: ₹1999 (min 4 pages)
- Print Design: ₹499
- SEO: ₹15000
- UI/UX Design: ₹12000
- Video Editing: ₹1000 (30 sec)
- Flex Banner Design: ₹499
- Pamphlet Design: ₹1000
- Product Label Design: ₹699

IMPORTANT:
- If user asks for ANY design service not listed:
  → Say YES we do it
  → Give approximate starting price
  → Ask for details

Rules:
- Keep replies short
- Be friendly
- Focus on conversion
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
    # 📞 CALL BUTTON
    # ==============================
    st.markdown("""
    <a href="tel:9080732938">
        <button style="
            width:100%;
            background: linear-gradient(90deg, #ff4b2b, #ff416c);
            color:white;
            border:none;
            padding:14px;
            border-radius:12px;
            font-size:16px;
            font-weight:bold;
            margin-top:10px;
            cursor:pointer;
        ">
        📞 Call Now
        </button>
    </a>
    """, unsafe_allow_html=True)

    # ==============================
    # 💬 WHATSAPP BUTTON
    # ==============================
    st.markdown("""
    <a href="https://wa.me/919080732938?text=Hi%20I%20need%20design%20service" target="_blank">
        <button style="
            width:100%;
            background: linear-gradient(90deg, #25D366, #128C7E);
            color:white;
            border:none;
            padding:14px;
            border-radius:12px;
            font-size:16px;
            font-weight:bold;
            margin-top:10px;
            cursor:pointer;
        ">
        💬 Chat on WhatsApp
        </button>
    </a>
    """, unsafe_allow_html=True)

# ==============================
# 🚀 FOOTER
# ==============================
st.markdown(
    "<center>⚡ Sureka AI • Powered by Sureka Designz</center>",
    unsafe_allow_html=True
)
