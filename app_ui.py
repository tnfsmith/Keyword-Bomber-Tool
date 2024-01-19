# Import necessary libraries
import streamlit as st
from streamlit.components.v1 import html, components
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
st.title("Google SEO Keyword Bomber LLM")
st.write("Enter the details below to fetch keyword data. Data analyze with LLM from OpenAI.")

with st.form(key='my_form'):
    input_keyword = st.text_input("Enter the Google SEO keyword", "Marketing Automation")
    selected_country = st.selectbox("Select the country code", ["VN", "US"])
    API_KEY = st.text_input("Enter your OpenAI API Key. If not AI Analyze Report will be vacant", "sk-Need sponsor :D")
    submit_button = st.form_submit_button(label='Fetch Data')

# Create a placeholder for the success message
success_message_placeholder = st.empty()
error_message_placeholder = st.empty()

# Function to process the data fetching
def process_data():
    st.session_state['fetching_data'] = True
    with st.spinner("Fetching data..."):
        result = run_asyncio_code(input_keyword, selected_country, API_KEY)
        if result.get('success'):
            success_message_placeholder.success(f"Success! Keywords Generated: {input_keyword}. Used specified Google agent country code and language in {selected_country} for best result!")
            display_keyword_data(result['result']['keyword_data'])
            display_ai_report(result['result']['ai_report'])
        else:
            st.error("Failed to fetch data")
            error_message_placeholder.error(f"Failed to fetch data. Please try again!")

# Check if the form was submitted
if submit_button:
    process_data()

# Footer
st.markdown("---")  # This adds a horizontal line for visual separation
# Footer content with smaller text in one column
footer_content = """
<small>Developed by <a href='https://lequocthai.com'>Lê Quốc Thái</a></small> <br>
<small>Contact email: <a href='mailto:lequocthai@gmail.com'>lequocthai@gmail.com</a></small> <br>
<small>Connect social <a href='https://t.me/tnfsmith'>Telegram</a> | <a href='tel:0985010707'>Zalo</a></small>

"""

st.markdown(footer_content, unsafe_allow_html=True)
# Footer and BuyMeACoffee button
st.markdown("""
        <h10 style="text-align: center; position: fixed; bottom: 3rem;">Developed <a href='https://lequocthai.com'>Lê Quốc Thái</a> | Contact email: <a href='mailto:lequocthai@gmail.com'>lequocthai[at]gmail.com</a> | Connect social <a href='https://t.me/tnfsmith'>Telegram</a> | <a href='tel:0985010707'>Zalo</a> </h10>""",
        unsafe_allow_html=True)
button = """<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="LeQuocThaiy" data-color="#FFDD00" data-emoji="📖" data-font="Cookie" data-text="Buy me a Coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>"""
html(button, height=60, width=200)
st.markdown(
        """
        <style>
            iframe[width="200"] {
                position: fixed;
                bottom: 60px;
                right: 40px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )