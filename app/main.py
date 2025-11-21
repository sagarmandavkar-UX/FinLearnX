"""FinLearnX - AI Financial Learning + Portfolio Platform

Main Streamlit Application Entry Point
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="FinLearnX",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("💰 FinLearnX")
st.sidebar.markdown("AI-Powered Financial Education Platform")

pages = {
    "Home": "🏠",
    "Learn": "📚",
    "AI Tutor": "🤖",
    "Market Analysis": "📈",
    "Portfolio Builder": "💼",
    "Simulations Hub": "🎮",
    "Backtesting": "⏱️",
    "Paper Trading": "💵",
    "Settings": "⚙️",
    "About": "ℹ️"
}

selection = st.sidebar.radio(
    "Navigation",
    list(pages.keys()),
    format_func=lambda x: f"{pages[x]} {x}"
)

# Main content
if selection == "Home":
    st.title("🏠 Dashboard")
    st.markdown("""
    ### Welcome to FinLearnX!
    
    Your AI-powered platform for financial learning, portfolio management, and trading simulation.
    
    #### Quick Stats
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Portfolio Value", "$0", "0%")
    with col2:
        st.metric("Learning Progress", "0%", "0 modules")
    with col3:
        st.metric("Simulations Run", "0", "0 today")
    with col4:
        st.metric("AI Interactions", "0", "0 today")
    
    st.info("🚧 This is a demo version. Start by exploring the Learning Hub or AI Tutor!")

elif selection == "Learn":
    st.title("📚 Learning Hub")
    st.write("Educational modules, videos, articles, and interactive lessons...")

elif selection == "AI Tutor":
    st.title("🤖 AI Financial Tutor")
    st.write("Chat with AI agents for personalized financial education...")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Ask me anything about finance..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

elif selection == "Market Analysis":
    st.title("📈 Market Analysis")
    st.write("Technical indicators, sector rotation, macro analysis...")

elif selection == "Portfolio Builder":
    st.title("💼 Portfolio Construction")
    st.write("Build and optimize your portfolio with AI assistance...")

elif selection == "Simulations Hub":
    st.title("🎮 Simulations")
    st.write("Trading simulations, market crash scenarios, bond pricing...")

elif selection == "Backtesting":
    st.title("⏱️ Backtesting Engine")
    st.write("Test your strategies against historical data...")

elif selection == "Paper Trading":
    st.title("💵 Paper Trading")
    st.write("Practice trading with virtual cash...")

elif selection == "Settings":
    st.title("⚙️ Settings")
    st.write("Configure your preferences, API keys, and profile...")

elif selection == "About":
    st.title("ℹ️ About FinLearnX")
    st.markdown("""
    ### FinLearnX
    
    **AI-Driven Financial Learning + Portfolio Platform**
    
    Built for educational purposes to empower users with:
    - AI-powered tutoring
    - Portfolio optimization
    - Trading simulations
    - Comprehensive financial education
    
    ---
    
    ⚠️ **Disclaimer**: This platform is for educational purposes only.
    Not financial advice. Always consult with licensed professionals.
    
    👨‍💻 Created by Sagar Mandavkar
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("🛡️ Educational purposes only")
st.sidebar.markdown("Not financial advice")
