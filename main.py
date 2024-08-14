import os
import csv
import streamlit as st

# Create the 'data' folder if it doesn't exist
folder_path = 'data'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Streamlit app layout
st.title("Personal Details Collector")
st.write("Record your name and mobile number:")

# Audio recording functionality
audio_bytes = st.audio_recorder("Click to record", format="wav")

# Save data (audio and optionally transcribed text)
if st.button("Save"):
    if audio_bytes:
        # Save the audio recording
        file_name = f"{len(os.listdir(folder_path)) + 1}.wav"  # Unique filename
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "wb") as f:
            f.write(audio_bytes)

        # Optionally, attempt transcription (you'll need a transcription service)
        # transcribed_text = transcribe_audio(audio_bytes) 

        # Write to CSV (audio filename and potentially transcribed text)
        csv_file_path = os.path.join(folder_path, 'personal_details.csv')
        with open(csv_file_path, 'a', newline='') as csvfile:
            fieldnames = ['Audio_File'] #, 'Transcribed_Text'] 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Audio_File': file_name}) #, 'Transcribed_Text': transcribed_text})

        st.success("Audio saved successfully!")

# Optional: Display existing data (audio playback)
if st.checkbox("View existing data"):
    existing_data = []
    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_data = list(reader)

    for row in existing_data:
        audio_file_path = os.path.join(folder_path, row['Audio_File'])
        st.audio(audio_file_path, format="wav")
        # If you have transcriptions, display them as well
        # st.write(row['Transcribed_Text']) 
