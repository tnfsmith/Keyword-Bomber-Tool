# Import necessary libraries
import streamlit as st
import bomber
import asyncio
import pandas as pd

# Function to run asyncio code
def run_asyncio_code(keyword, country, api_key):
    return asyncio.run(bomber.get_keyword_data(keyword, country, api_key))


# Function to display Keyword Data
def display_keyword_data(keyword_data):
    st.markdown("## Keyword Data")
    for category, keywords in keyword_data.items():
        st.markdown(f"### {category}")
        df = pd.DataFrame.from_dict(keywords, orient='index').transpose()
        st.dataframe(df)

# Function to display AI Report
def display_ai_report(ai_report):
    st.markdown("## AI Analysis Report")
    st.markdown(ai_report)

# Streamlit UI layout
st.title("Google SEO Keyword Bomber TTL")

st.write("Enter the details below to fetch keyword data.")

input_keyword = st.text_input("Enter the keyword", "Marketing Automation")

# Dropdown for country selection with 'Other Country' option
countries = ["VN", "US"]
selected_country = st.selectbox("Select the country code", countries)
#input_country = st.text_input("Enter the country code", "VN")

API_KEY = st.text_input("Enter your OpenAI API Key", "sk-Need sponsor :D")

# Initialize session state for button state
if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = False

# Initialize a key in the session state to track the last input
if 'last_input' not in st.session_state:
    st.session_state['last_input'] = ''

# Button to fetch data
fetch_button = st.button("Fetch Data", disabled=st.session_state['button_clicked'])

# Create a placeholder for the success message
success_message_placeholder = st.empty()

# Function to process the data fetching
def process_data():
    with st.spinner("Fetching data..."):
        result = run_asyncio_code(input_keyword, selected_country, API_KEY)
        if result.get('success'):
            success_message_placeholder.success(f"Success! Keywords Generated: {input_keyword}. Used specified Google agent country code and language in {selected_country} for best result!")
            display_keyword_data(result['result']['keyword_data'])
            display_ai_report(result['result']['ai_report'])
        else:
            st.error("Failed to fetch data")
    st.session_state['button_clicked'] = False  # Reset button state

if fetch_button or (input_keyword != st.session_state['last_input']):
    st.session_state['last_input'] = input_keyword
    st.session_state['button_clicked'] = True  # Disable button
    process_data()