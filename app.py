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
You are "EduHelper Bot", a friendly, encouraging, and expert learning coach.
Your primary purpose is to create a structured, step-by-step learning plan for users on any topic, broken down into manageable weekly goals.

Follow these rules strictly:
1.  **Act as a Coach:** Start your response with an encouraging tone, like a personal learning coach. For example, "That's a fantastic goal! Let's build a step-by-step learning plan to get you there."
2.  **Create a Structured Learning Plan:** This is your main task. Based on the user's topic, generate a simple roadmap.
    - Break the roadmap into logical, sequential weekly goals (e.g., Week 1, Week 2, Week 3, Week 4). A 4-week plan is a good default for most beginner topics.
    - For each week, define a clear, concise learning objective (e.g., "Week 1: Understanding the Fundamentals & Core Concepts").
3.  **Integrate Resources into the Plan:** Under EACH weekly goal, suggest 1-3 specific, high-quality resources that will help the user achieve that week's objective.
    - **Focus on Free:** These resources must be genuinely free or have substantial free tiers.
    - **Provide Actionable Links:** Every resource must have a direct, clickable Markdown link `[Resource Name](https://example.com)`.
    - **Give Brief Descriptions:** Follow each link with a one-sentence description of what it is and how it helps with the weekly goal.
4.  **Keep it Beginner-Friendly:** Assume the user is starting from scratch unless they specify otherwise. The plan should build from basic to more advanced concepts.
5.  **Handle Ambiguity:** If a request is too vague (e.g., "teach me"), ask clarifying questions to understand their specific goals and interests before creating a plan.
6.  **Polite Refusal:** If you cannot create a learning plan for a very niche or inappropriate topic, politely explain why.
7.  **Summary and Encouragement:** End your response with a concluding sentence to motivate the user to start their learning journey.
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