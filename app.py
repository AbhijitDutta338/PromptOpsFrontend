import streamlit as st
import requests

# Replace with your deployed API endpoint
API_URL = "https://promptops-service-891930461435.us-central1.run.app"

# Sidebar
st.sidebar.title("🛠️ PromptOps")
with st.sidebar.expander("ℹ️ What is PromptOps?"):
    st.markdown("""
    PromptOps is a lightweight log triage assistant powered by Vertex AI.
    
    - Paste logs from your CI/CD pipelines or cloud infra.
    - Get an instant incident summary.
    - Receive actionable suggestions, powered by LLMs.

    🔁 Powered by Google Cloud Functions + Vertex AI
    """)

# Main page
st.title("🚨 Log Summarizer")

logs = st.text_area("Paste your logs here:", height=200)

if st.button("🔍 Summarize"):
    if not logs.strip():
        st.warning("Please paste some logs first.")
    else:
        with st.spinner("Analyzing logs with PromptOps..."):
            try:
                response = requests.post(API_URL, json={"logs": logs})
                if response.status_code == 200:
                    summary = response.json().get("summary", "No summary returned.")
                    st.subheader("🧠 AI-Powered Summary:")
                    st.success(summary)
                else:
                    st.error(f"API returned {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Error: {e}")