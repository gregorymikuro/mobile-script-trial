import os
import csv
import streamlit as st

# Create the 'data' folder if it doesn't exist
folder_path = 'data'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Streamlit app layout
st.title("Personal Details Collector")
st.write("Enter your personal details:")

# Input fields for name and mobile number
name = st.text_input("Name:")
mobile = st.text_input("Mobile Number:")

# Save data to a CSV file
csv_file_path = os.path.join(folder_path, 'personal_details.csv')
if st.button("Save"):
    with open(csv_file_path, 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Mobile']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Name': name, 'Mobile': mobile})
        st.success("Data saved successfully!")

# Optional: Display existing data
if st.checkbox("View existing data"):
    existing_data = []
    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_data = list(reader)
    st.dataframe(existing_data)

# Optional: Add more features as needed

