import streamlit as st
import speech_recognition as sr

def transcribe_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Say something...")

        # Continuous listening loop
        while True:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                st.write("Transcription:", text)
            except sr.UnknownValueError:
                # If no speech is detected
                pass
            except sr.RequestError as e:
                st.write("Could not request results from Google Speech Recognition service; {0}".format(e))
                break

def main():
    st.title("Real-time Voice Transcription App")

    st.write("Click the button below and start speaking.")

    if st.button("Start Transcription"):
        transcribe_speech()

if __name__ == "__main__":
    main()

