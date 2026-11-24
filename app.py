
import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# -----------------------------
# LOAD ENVIRONMENT VARIABLES
# -----------------------------
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="TravelMate AI",
    page_icon="🌍",
    layout="centered"
)

# -----------------------------
# GROQ CLIENT
# -----------------------------
client = Groq(api_key=api_key) if api_key else None

# -----------------------------
# APP TITLE
# -----------------------------
st.title("🌍 TravelMate AI")
st.caption("Your Personal AI Tourism & Travel Assistant")

st.markdown("""
Welcome to **TravelMate AI!** ✈️

Explore beautiful destinations, discover famous food,
plan your trips and get travel recommendations.
""")

# -----------------------------
# CHAT HISTORY
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.title("⚙️ Settings")

    model_name = st.selectbox(
        "Choose AI Model",
        [
            "openai/gpt-oss-120b",
            "openai/gpt-oss-20b"
        ],
        index=0
    )

    st.markdown("---")

    st.subheader("🌎 Travel Categories")

    st.markdown("""
    - 🏔️ Tourist Destinations
    - 🏨 Hotels & Accommodation
    - 🍕 Famous Food
    - 🗺️ Travel Itinerary
    - 💰 Travel Budget
    - 🌦️ Best Time to Visit
    """)

    st.markdown("---")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.caption("AI Model: Groq")
    st.caption("Backend: Groq API")
    st.caption("Frontend: Streamlit")

# -----------------------------
# SYSTEM PROMPT
# -----------------------------
system_prompt = {
    "role": "system",
    "content": """
You are TravelMate AI, a professional tourism and travel assistant.

Your main purpose is to help users explore tourist destinations
and plan their trips.

Follow these instructions:

1. Answer questions related to tourism and travel.
2. Recommend tourist destinations in Pakistan and worldwide.
3. Suggest hotels, restaurants and historical attractions.
4. Create 1-day, 3-day, 5-day and 7-day itineraries.
5. Suggest estimated travel budgets.
6. Explain the best seasons to visit destinations.
7. Provide information about local food and culture.
8. Give travel safety tips.
9. Provide information about Hunza, Skardu, Swat, Murree,
   Naran, Kaghan, Lahore and Karachi.
10. Ask for destination, duration and budget when necessary.
11. Use headings, bullet points and simple language.
12. Be friendly, polite and helpful.
13. Never invent current hotel prices or travel conditions.
14. Politely redirect unrelated questions to tourism topics.

IMPORTANT:
You are specifically a TOURISM CHATBOT,
not a general-purpose chatbot.
"""
}

# -----------------------------
# QUICK TRAVEL SUGGESTIONS
# -----------------------------
st.subheader("✈️ Explore Travel Ideas")

col1, col2 = st.columns(2)

with col1:

    if st.button("🏔️ Explore Pakistan", use_container_width=True):
        st.session_state.quick_prompt = (
            "Suggest the top 10 tourist destinations in Pakistan."
        )

    if st.button("🗺️ Plan My Trip", use_container_width=True):
        st.session_state.quick_prompt = (
            "Create a 3-day travel itinerary for Hunza Valley."
        )

with col2:

    if st.button("🍕 Famous Local Food", use_container_width=True):
        st.session_state.quick_prompt = (
            "Tell me about famous Pakistani food for tourists."
        )

    if st.button("💰 Travel Budget", use_container_width=True):
        st.session_state.quick_prompt = (
            "Estimate a budget for a 5-day trip to Skardu."
        )

# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# USER INPUT
# -----------------------------
user_prompt = st.chat_input(
    "Ask about destinations, hotels, food or travel plans..."
)

if "quick_prompt" in st.session_state:
    user_prompt = st.session_state.pop("quick_prompt")

# -----------------------------
# GENERATE RESPONSE
# -----------------------------
if user_prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):

        if not api_key or not client:

            st.error(
                "Groq API key missing! "
                "Please configure GROQ_API_KEY in your .env file."
            )

        else:

            try:

                with st.spinner("🌍 Planning your travel experience..."):

                    response = client.chat.completions.create(
                        model=model_name,
                        messages=[
                            system_prompt,
                            *st.session_state.messages
                        ],
                        temperature=0.7,
                        max_completion_tokens=2048
                    )

                    answer = response.choices[0].message.content

                if not answer:
                    answer = "Sorry, no response received. Please try again."

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:

                st.error("Unable to generate response.")

                st.caption(f"Error details: {str(e)}")
