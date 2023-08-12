import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define a dictionary of valid usernames and passwords
VALID_USERS = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

# Fake data for candidate profiles
candidate_profiles = [
    {
        'Name': 'John Doe',
        'Age': 30,
        'Experience': '5 years',
        'Skills': 'Python, SQL, Machine Learning',
        'Education': 'MSc in Computer Science'
    },
    {
        'Name': 'Jane Smith',
        'Age': 28,
        'Experience': '3 years',
        'Skills': 'JavaScript, React, UI/UX Design',
        'Education': 'BSc in Web Development'
    },
    {
        'Name': 'Alex Johnson',
        'Age': 25,
        'Experience': '2 years',
        'Skills': 'Java, Spring Boot, Microservices',
        'Education': 'BEng in Software Engineering'
    }
]

# Google Sheets setup
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
CREDS = ServiceAccountCredentials.from_json_keyfile_name('/Users/hectorstanley/Downloads/spring-395512-5bef0d0d2984.json', SCOPE)
CLIENT = gspread.authorize(CREDS)
SHEET = CLIENT.open('Spring 1 - Streamlit')

def login():
    st.title("Login Page")

    login_placeholder = st.empty()
    username = login_placeholder.text_input("Username")
    password = login_placeholder.text_input("Password", type="password")

    login_button = login_placeholder.button("Login")

    if login_button:
        if username in VALID_USERS and password == VALID_USERS[username]:
            st.success("Login successful!")
            login_placeholder.empty()
            dashboard()
        else:
            st.error("Invalid username or password")

def dashboard():
    st.title("Candidate Profiles")
    st.write("Welcome to the Candidate Profiles Dashboard! Here are some fake profiles:")

    for profile in candidate_profiles:
        st.subheader(profile['Name'])
        st.write(f"Age: {profile['Age']}")
        st.write(f"Experience: {profile['Experience']}")
        st.write(f"Skills: {profile['Skills']}")
        st.write(f"Education: {profile['Education']}")
        st.write("-" * 50)

    st.title("Upload Your Profile")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=150, value=25)
    experience = st.text_input("Experience")
    skills = st.text_input("Skills")
    education = st.text_input("Education")

    if st.button("Upload"):
        new_profile = {
            'Name': name,
            'Age': age,
            'Experience': experience,
            'Skills': skills,
            'Education': education
        }
        candidate_profiles.append(new_profile)
        write_to_google_sheet(new_profile)
        st.success("Profile uploaded successfully!")

def write_to_google_sheet(profile):
    worksheet = SHEET.get_worksheet(0)  # Assuming the data goes to the first worksheet
    values = [profile['Name'], profile['Age'], profile['Experience'], profile['Skills'], profile['Education']]
    worksheet.append_row(values)

def main():
    login()

if __name__ == "__main__":
    main()
