from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
 
load_dotenv()   ## load all environment variables
 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
 
st.set_page_config(page_title="My Audio Summarizer",page_icon="🤖")
 
st.header("My Audio Summarizer Web Application")
 
uploaded_audio = st.file_uploader("Upload an audio file to summarize",type=['mp3'])
 
if uploaded_audio is not None:
    ## Save the audio file to a temporary file
    audio_file_name = uploaded_audio.name
    with open(audio_file_name,"wb") as f:
        f.write(uploaded_audio.getbuffer())
 
    st.audio(audio_file_name)
 
    st.write("Uploading file...")
 
    audio_file = genai.upload_file(path=audio_file_name)
 
    st.write("Upload Completed : {}".format(audio_file.uri))
 
    st.write("Generating the summary....")
 
    prompt = """Listen carefully to the following audio file and provide the brief summary 
                in 200-250 words"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt,audio_file])
    st.write(response.text)