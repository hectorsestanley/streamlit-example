import streamlit as st
import gspread
#from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Streamlit app starts here
st.title("Welcome to Spring!")

# Google Sheets setup
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
CREDS = ServiceAccountCredentials.from_json_keyfile_name('/Users/hectorstanley/Downloads/spring-395512-5bef0d0d2984.json', SCOPE)
CLIENT = gspread.authorize(CREDS)
SHEET = CLIENT.open('Spring 1 - Streamlit')

# Login Page (Simple authentication for demonstration, not secure for production)
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type='password')
if username == "admin" and password == "admin":  # For demo purpose, you can integrate a proper authentication
    st.sidebar.success("Logged in successfully")

    st.header("Forms")

    form_option = st.selectbox("Select Form", ["Candidate Info", "Placement Info"])

    # First Form: Candidate Info
    if form_option == "Candidate Info":
        with st.form("personal_info"):
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            role_title = st.text_input("Current Role Title")
            dev_goals = st.text_input("Development Goals")
            salary = st.number_input("Salary", value=0.0)
            submit = st.form_submit_button("Submit")

            if submit:
                st.success("Candidate Info Submitted!")

    # Second Form: Placement Info
    elif form_option == "Placement Info":
        with st.form("role_info"):
            role_name = st.text_input("Role Name")
            start_date = st.date_input("Start Date", datetime.now())
            end_date = st.date_input("End Date", datetime.now())
            requirements = st.text_input("Requirements")
            salary = st.number_input("Role Salary", value=0.0)
            submit = st.form_submit_button("Submit")

            if submit:
                st.success("Placement Info Submitted!")
else:
    st.sidebar.warning("Please enter username and password")

if __name__ == "__main__":
    st.write("Thank you for completing the form")
