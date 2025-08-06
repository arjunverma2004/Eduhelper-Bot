# **🎓 EduHelper Bot**

## **🚀 Overview**

**EduHelper Bot** is an AI-powered chatbot designed to provide structured, step-by-step learning plans and free online resources for any topic you want to learn. Our mission is to make quality education accessible to everyone, aligning with **SDG \#4: Quality Education**.

Whether you're a complete beginner or looking to deepen your knowledge, EduHelper Bot acts as your personal learning coach, guiding you through weekly goals and curating high-quality, free resources to help you achieve your learning objectives.

## **✨ Features**

* **Personalized Learning Plans:** Get a tailored, week-by-week roadmap for any subject.  
* **Curated Free Resources:** Discover 1-3 specific, high-quality, and genuinely free online resources for each weekly goal, complete with actionable links and brief descriptions.  
* **Beginner-Friendly Approach:** Plans are designed to build from fundamental to more advanced concepts, suitable for learners starting from scratch.  
* **Interactive Chat Interface:** Engage with the bot in a conversational manner to refine your learning journey.  
* **Typing Effect:** Enjoy a dynamic and engaging user experience with streamed responses.

## **🎯 Alignment with SDG \#4: Quality Education**

This project contributes to **Sustainable Development Goal 4: Quality Education** by:

* **Increasing Access:** Providing free, structured learning paths removes financial barriers to education.  
* **Promoting Lifelong Learning:** Encouraging continuous skill development and knowledge acquisition.  
* **Enhancing Learning Outcomes:** Offering curated resources to ensure learners have access to effective materials.

## **🛠️ Tech Stack**

* **Python:** The core programming language.  
* **Streamlit:** For building the interactive web application.  
* **Google Gemini API (gemini-1.5-flash):** The powerful AI model driving the learning plan generation.

## **⚙️ Setup and Installation**

Follow these steps to get EduHelper Bot running locally or understand its deployment:

### **1\. Clone the Repository**

git clone https://github.com/\<Your-GitHub-Username\>/EduHelper-Bot.git  
cd EduHelper-Bot

### **2\. Create a Virtual Environment (Recommended)**

python \-m venv venv  
\# On Windows:  
.\\venv\\Scripts\\activate  
\# On macOS/Linux:  
source venv/bin/activate

### **3\. Install Dependencies**

pip install \-r requirements.txt

*(You'll need to create a requirements.txt file if you haven't already. You can generate it using pip freeze \> requirements.txt after installing streamlit and google-generativeai.)*

### **4\. Get Your Google Gemini API Key**

1. Go to [Google AI Studio](https://aistudio.google.com/).  
2. Log in with your Google account.  
3. Create a new API key.  
4. Copy your API key.

### **5\. Configure Streamlit Secrets**

Create a directory named .streamlit in the root of your project if it doesn't already exist. Inside .streamlit, create a file named secrets.toml.

Add your Gemini API key to secrets.toml like this:

GEMINI\_API\_KEY="your\_gemini\_api\_key\_here"

Replace "your\_gemini\_api\_key\_here" with the actual API key you obtained from Google AI Studio.

### **6\. Run the Application**

streamlit run app.py

Your browser should automatically open the EduHelper Bot application.

## **🎨 Custom Themes (Optional)**

The app supports multiple custom themes for a personalized experience. You can switch between them using the theme selector in the sidebar. The themes are defined within app.py and applied via custom CSS.

## **🤝 Contributing**

Contributions are welcome\! If you have suggestions for improvements, bug fixes, or new features, please open an issue or submit a pull request.

## **📄 License**

This project is licensed under the MIT License \- see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

## **🙏 Acknowledgements**

* Built with [Streamlit](https://streamlit.io/)  
* Powered by [Google Gemini](https://ai.google.dev/gemini-api)

**Created by: \[Your Name Here\]** (Remember to update this with your actual name or GitHub profile link\!)