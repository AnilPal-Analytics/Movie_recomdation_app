import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

import os
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

st.title("📽️Movie Recommendation System")

user_input = st.text_input("**Enter Movie Name**")
submit = st.button("Submit...")

model = genai.GenerativeModel("gemini-2.5-flash-lite")

if submit and user_input.strip():
    st.success(f"Movie name entered: {user_input}")

    response = model.generate_content(
        f"Generate movie recommendations related to: {user_input}"
    )

    st.write("🎬 **Related Recommendations:**")
    st.write(response.text)

else:
    st.warning("You need to enter the movie name")
