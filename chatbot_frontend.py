import streamlit as st
import requests

st.set_page_config(page_title="Developer Documentation Chatbot", page_icon="📚")

st.title("📚 Developer Documentation Chatbot")

user_question = st.text_input("💬 Ask your question:")

if st.button("Ask Chatbot 🚀") and user_question.strip():
    
    # Clearly set your n8n webhook URL here
    n8n_webhook_url = "https://imranimmu.app.n8n.cloud/webhook-test/chatbot"

    try:
        with st.spinner("Fetching response from Chatbot via n8n..."):
            response = requests.get(n8n_webhook_url, params={"query": user_question})

        if response.status_code == 200:
            data = response.json()
            st.markdown("### 🤖 Chatbot Response:")
            st.markdown(data["response"])
        else:
            st.error(f"❌ Chatbot Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")
