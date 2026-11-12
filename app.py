
import streamlit as st
import ollama

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="TravelMate AI",
    page_icon="🌍",
    layout="centered"
)

# -----------------------------
# APP TITLE
# -----------------------------
st.title("🌍 TravelMate AI")
st.caption("Your Personal AI Tourism & Travel Assistant")

st.markdown(
    """
    Welcome to **TravelMate AI!** ✈️

    Explore beautiful destinations, discover famous food,
    plan your trips and get travel recommendations.
    """
)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.title("⚙️ Settings")

    model_name = st.selectbox(
        "Choose AI Model",
        ["llama3.2", "llama3.2:1b"],
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

    st.caption("AI Model: Llama 3.2")
    st.caption("Backend: Ollama")
    st.caption("Frontend: Streamlit")

# -----------------------------
# INITIALIZE CHAT HISTORY
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# TOURISM SYSTEM PROMPT
# -----------------------------
system_prompt = {
    "role": "system",
    "content": """
    You are TravelMate AI, a professional tourism and travel
    assistant.

    Your main purpose is to help users explore tourist
    destinations and plan their trips.

    Follow these instructions:

    1. Answer questions related to tourism and travel.

    2. Provide information about famous tourist destinations
       in Pakistan and around the world.

    3. Recommend beautiful places, hotels, restaurants,
       historical sites and natural attractions.

    4. Create travel itineraries for 1 day, 3 days,
       5 days and 7 days.

    5. Suggest estimated travel budgets according to
       the user's requirements.

    6. Explain the best seasons and months to visit places.

    7. Provide information about local food and culture.

    8. Give travel safety tips and useful recommendations.

    9. If the user asks about Pakistan, provide detailed
       information about places such as Hunza, Skardu,
       Swat, Murree, Naran, Kaghan, Lahore and Karachi.

    10. Ask for the destination, travel duration and budget
        when necessary.

    11. Use headings, bullet points and simple language.

    12. Be friendly, polite and helpful.

    13. Never invent hotel prices, opening hours or
        current travel conditions. Clearly mention when
        information needs verification.

    14. For medical, political or unrelated questions,
        politely redirect the user to travel-related topics.

    IMPORTANT:
    You are specifically a TOURISM CHATBOT, not a
    general-purpose chatbot.
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

# Handle quick suggestion buttons
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

        try:
            with st.spinner("🌍 Planning your travel experience..."):

                response = ollama.chat(
                    model=model_name,
                    messages=[
                        system_prompt,
                        *st.session_state.messages
                    ]
                )

                answer = response["message"]["content"]

            st.markdown(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:

            st.error(
                "Unable to generate response. "
                "Please make sure Ollama is running "
                "and your selected model is installed."
            )

            st.caption(str(e))
