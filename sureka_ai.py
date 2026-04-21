import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load API key
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

# ---------------- UI DESIGN ---------------- #

st.set_page_config(page_title="Sureka AI", page_icon="🎨", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #0e1117;
    }
    .stTextInput>div>div>input {
        background-color: #1c1f26;
        color: white;
        border-radius: 10px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6C63FF, #9C27B0);
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #9C27B0, #6C63FF);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<h1 style='text-align:center; color:#6C63FF;'>🎨 Sureka Designz AI</h1>
<p style='text-align:center; color:gray;'>Instant replies for your design needs ⚡</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- INPUT ---------------- #

user_input = st.text_input("💬 Ask anything (logo, website, SEO, etc)")

# ---------------- BUTTON ---------------- #

if st.button("🚀 Get Reply"):

    if user_input:

        # Prompt
        prompt = f"""
You are a smart AI assistant for Sureka Designz.

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

Working Hours: 10 AM to 8 PM

Instructions:
- Reply in simple English + little Tamil style (friendly tone)
- If user asks price → give price clearly
- If service not listed → say “Yes we can do, please share details”
- Always end with asking name + contact

User Question:
{user_input}
"""

        # AI response
        response = llm.invoke(prompt)

        # Output
        st.success(response.content)

    else:
        st.warning("Please enter something 🙌")

# ---------------- FOOTER ---------------- #

st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>⚡ Powered by Sureka Designz</p>", unsafe_allow_html=True)