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
st.title("SEO Keyword Bomber for TTL")

st.write("Enter the details below to fetch keyword data.")

# Initialize session state
if 'last_keyword' not in st.session_state:
    st.session_state['last_keyword'] = ''

input_keyword = st.text_input("Enter the keyword", "Marketing Automation")

# Dropdown for country selection with 'Other Country' option
countries = ["VN", "US"]
selected_country = st.selectbox("Select the country code", countries)
#input_country = st.text_input("Enter the country code", "VN")

API_KEY = st.text_input("Enter your OpenAI API Key", "sk-Need sponsor :D")

# Create two columns for the button and the message
col1, col2 = st.columns(2)
# Button in the first column
fetch_button = col1.button("Fetch Data")
col2.success("Success! Keywords Generated")  # Display success message
if fetch_button:
   
    with st.spinner("Fetching data..."):
        
        result = run_asyncio_code(input_keyword, selected_country, API_KEY) #input_country
        if result.get('success'):
            col2.success("Success! Keywords Generated")  # Display success message
            display_keyword_data(result['result']['keyword_data'])
            display_ai_report(result['result']['ai_report'])
        else:
            st.error("Failed to fetch data")
    
    
# Check if the keyword has changed
#if input_keyword != st.session_state['last_keyword']:
 #   with st.spinner("Fetching data..."):
  #      result = run_asyncio_code(input_keyword, selected_country, API_KEY) #input_country
  #      if result.get('success'):
  #          display_keyword_data(result['result']['keyword_data'])
  #          display_ai_report(result['result']['ai_report'])