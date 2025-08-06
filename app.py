import streamlit as st
import google.generativeai as genai
import time 

# --- Page Configuration ---
st.set_page_config(
    page_title="EduHelper Bot",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- App Title and Description ---
st.title("🎓 EduHelper Bot")
st.caption("🚀 Your AI-powered guide to free online learning resources. Aligned with SDG #4: Quality Education.")

# --- System Prompt for the AI Model ---
SYSTEM_PROMPT = """
You are "EduHelper Bot", a friendly, encouraging, and knowledgeable AI assistant.
Your sole purpose is to help users discover free, high-quality online learning resources on any topic they are interested in.

Follow these rules strictly:
1.  **Acknowledge and Encourage:** Start your response by acknowledging the user's request and being encouraging.
2.  **Focus on Free Resources:** Only suggest resources that are genuinely free or have substantial, high-value free tiers. Mention if a resource also has a paid option, but the primary recommendation must be free.
3.  **Provide Actionable Links:** For each resource, provide a direct, clickable Markdown link, like `[Resource Name](https://example.com)`. Do not just list names.
4.  **Give Brief Descriptions:** After each link, provide a concise one-sentence description explaining what the resource is (e.g., "A platform for interactive coding exercises," "A YouTube channel with high-quality animated science videos.").
5.  **Categorize for Clarity:** Organize the resources into logical categories (e.g., "Interactive Courses," "Video Tutorials," "Reading & Articles," "Practice Platforms").
6.  **Handle Ambiguity:** If the user's request is too vague (e.g., "I want to learn"), ask clarifying questions to understand their needs better (e.g., "That's great! What subject are you interested in? And are you a beginner or do you have some experience?").
7.  **Polite Refusal:** If you cannot find resources for a very niche or inappropriate topic, politely explain why.
8.  **Maintain Persona:** Always be positive, helpful, and focused on education.
"""

# --- Sidebar Information ---
with st.sidebar:
    st.header("🔗 About this Project")
    st.markdown(
        "**EduHelper Bot** is an AI chatbot that provides free online learning "
        "resources based on your interests, making education accessible to all."
    )
    st.markdown("**🎯 SDG Goal:** #4 - Quality Education")
    st.markdown("**💻 Tech Stack:** Python, Streamlit, Google Gemini")
    st.markdown(
        "**⚠️ Note:** This app uses the developer's API key. "
        "Please be respectful of the usage."
    )
    st.markdown("**🧑‍💻 Created by:** [Your Name Here]") # Feel free to change this!

# --- Main Chat Logic ---

# Check for the API key in Streamlit's secrets
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    # If the key is not found, display an error and stop the app
    st.error("Gemini API Key not found. Please add it to your Streamlit secrets (`.streamlit/secrets.toml`).")
    st.stop()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Add the system prompt (but don't display it)
if not any(msg["role"] == "system" for msg in st.session_state.messages):
        st.session_state.messages.append({"role": "system", "content": SYSTEM_PROMPT})

# Add a welcome message if the chat is new
if len(st.session_state.messages) <= 1:
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": "Hello! I'm EduHelper Bot. What new skill or subject are you excited to learn today?"
        }
    )

# Display existing chat messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input field for user's question
if user_prompt := st.chat_input("Suggest coding courses for beginners..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("Finding the best resources for you..."):
            # Construct context for the model
            prompt_history = [
                {"role": "user" if msg["role"] == "user" else "model", "parts": [msg["content"]]}
                for msg in st.session_state.messages
            ]
            full_prompt = [
                {"role": "user", "parts": [SYSTEM_PROMPT]},
                {"role": "model", "parts": ["Understood. I am EduHelper Bot, ready to assist."]}
            ] + prompt_history

            # Get response from the model
            chat_session = model.start_chat(history=full_prompt)
            response = chat_session.send_message(user_prompt)
            response_text = response.text

            # Stream response with a typing effect
            message_placeholder = st.empty()
            full_response = ""
            for chunk in response_text.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": response_text})