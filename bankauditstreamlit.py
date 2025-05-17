# -*- coding: utf-8 -*-
import streamlit as st
from streamlit.components.v1 import html
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Audit Portal", layout="wide")

# --- Custom CSS ---
custom_css = """
<style>
    .main {
        background-color: #f4f4f9;
        font-family: 'Helvetica Neue', sans-serif;
    }
    header, footer {
       background-color: #ffffff;
        padding: 1rem 2rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .logo {
        font-size: 1.5rem;
        font-weight: bold;
        color: #3f51b5;
    }
    .nav {
        float: right;
    }
    .nav a {
        margin: 0 0.75rem;
        text-decoration: none;
        color: #555;
    }
    .hero {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(to right, #667eea, #764ba2);
        color: white;
    }
    .features {
        padding: 3rem 2rem;
    }


    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        height: 600px; /* Adjust as needed */
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .cta {
        background-color: #3f51b5;
        color: white;
        padding: 3rem 2rem;
        text-align: center;
    }

     /* Container for messages with fixed height and scroll */
    #message-container {
        height: 400px;
        overflow-y: auto;
        border: 1px solid #ddd;
        padding: 10px;
        margin-bottom: 10px;
        background-color: #f9f9f9;
        border-radius: 8px;
    }

    /* Sticky/fixed input container */
    #input-container {
        position: sticky;
        bottom: 0;
        background: white;
        padding-top: 10px;
        border-top: 1px solid #ddd;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- Header ---
st.markdown("""
<header>
    <div class="logo">The Audit Portal</div>
    <div class="nav">
        <a href="#features">Features</a>
        <a href="#demo">Demo</a>
        <a href="#contact">Contact</a>
    </div>
</header>
""", unsafe_allow_html=True)

# --- Hero / Value Prop ---
st.markdown("""
<div class="hero">
    <h1>Welcome to The Audit Portal</h1>
    <p>Auditors spend a large amount of time manually checking documents, matching records,
    and writing reports. These tasks are repetitive, error-prone, and slow, especially when
    dealing with high volumes of data. Here is your smart system that can analyze and
    explain audit data quickly and accurately. </p>
</div>
""", unsafe_allow_html=True)

# --- Feature Showcase ---
st.markdown("<div id='features' class='features'>", unsafe_allow_html=True)
st.subheader("🌟 Key Features")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
            <div class="feature-card">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbnn0tssCtl_n6XAJ7L15NW1hgaqQghfeO0g&s" width="100%"/>
                <h3 STYLE="color:#000000">Catches More Errors & Risks (Improved Accuracy) </h3>
                <ul STYLE="color:#000000">
                    <li>Instead of spending hours manually checking invoices or journal entries, the AI scans thousands of records in minutes.</li>
                    <li>Auditors can now focus soley on the flagged issues, not the entire dataset</li>
                    <li>Can spot patterns of fraud or errors that humans might miss—like duplicate invoices or unusual transactions at odd times.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
            <div class="feature-card">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbnn0tssCtl_n6XAJ7L15NW1hgaqQghfeO0g&s" width="100%"/>
                <h3 STYLE="color:#000000">Auto-Writes Reports (Automatic Reporting)</h3>
                <ul STYLE="color:#000000">
                    <li>After analysis, the AI (via the LLM) can generate summaries, audit findings, or explanations in clear language. </li>
                    <li>This saves time for the auditor and ensures consistent quality.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
            <div class="feature-card">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbnn0tssCtl_n6XAJ7L15NW1hgaqQghfeO0g&s" width="100%"/>
                <h3 STYLE="color:#000000"> Serves as a Smart Assistant (Expert Insight) </h3>
                <ul STYLE="color:#000000">
                    <li>Auditors can ask the AI questions like:
                        <ul>
                            <li>“Why was this flagged?”</li>
                            <li>“Summarize all contract risks.”</li>
                        </ul>
                    </li>
                    <li>The model gives quick, knowledgeable answers based on the data.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
# --- Dataset ---
st.markdown("<div id='demo'>", unsafe_allow_html=True)
# --- CSV Viewer Section ---
st.subheader("📄 Audit Data Explorer")
st.write(f"Here is the data that has been given to the demo model. Sterling Oak Bank has hired Data Consultants to find fraudlent transactions in a log of past transactions. There are thousands of transactions and it would take months to go through.")

# Define your CSV paths and summaries
csv_files = {
    "Bank Transactions": {
        "path": "data/bank_transactions_data_2.csv",
        "summary": "🔍 A full export of processed bank transactions including dates, vendors, and amounts."
    },

    "Flagged Transactions (Given from Ensemble Model)": {
        "path": "flagged.csv",
        "summary": "List of all flagged transactions that the ensemble method gave back. The ensemble method provided the fraudulent transaction that all the models (SVM, Isolation Forest, DBSCAN) agreed on."
    }
}

# Dropdown to choose the dataset
selected = st.selectbox("Choose a dataset to view:", list(csv_files.keys()))

# Load and display the chosen CSV
file_info = csv_files[selected]
df = pd.read_csv(file_info["path"])

# Show summary and preview
st.markdown(f"**About this dataset:** {file_info['summary']}")
st.dataframe(df, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)


# --- Interactive Demo ---
st.markdown("<div id='demo'>", unsafe_allow_html=True)
from openai import OpenAI
from model_utils import predict_ensemble  # Make sure model_utils.py is in your project

with open("model_context.txt", "r") as f
    model_context = f.read()

# Read the flagged data (CSV)
flagged_df = pd.read_csv("flagged.csv")  # or "flagged.txt" if it's named that

# --- LLM Assistant ---
st.markdown("### 🤖 Ask the Audit Assistant")

st.markdown("Use the AI assistant to explain fraud results, patterns, or anything about the models.")

import streamlit as st
from openai import OpenAI

# Load your OpenAI API key securely
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    # Add system message with model context only once at the start
    st.session_state.messages = [
        {"role": "system", "content": f"You are a helpful fraud analyst. Use the following context to guide all your responses:\n\n{model_context}"}
    ]

# Display previous messages
for message in st.session_state.messages[1:]:  # Skip system message
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask something about fraud detection..."):
    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send message list to OpenAI (includes model context at the top)
    try:
        stream = client.chat.completions.create(
            model="gpt-4",
            messages=st.session_state.messages,
            stream=True,
        )

        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

    except Exception as e:
        st.error(f"Something went wrong: {e}")


st.markdown("</div>", unsafe_allow_html=True)

# --- Call to Action ---
st.markdown("""
<div class="cta">
    <h2>Get Started with The Audit Portal Today</h2>
    <p>Ready to see real impact? Contact us now or sign up for early access.</p>
</div>
""", unsafe_allow_html=True)

# --- Contact Form ---
st.markdown("<div id='contact'>", unsafe_allow_html=True)
st.subheader("📬 Contact Us")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thank you! We'll be in touch soon.")
st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<footer>
    <p>&copy; 2025 Your Company Name. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)

