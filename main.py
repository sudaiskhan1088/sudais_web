import streamlit as st

st.title("Welcome to wrold of Information ")
st.header("We will provide you information about phones")
st.subheader("")
st.markdown("We offer a wide range of the latest and best smartphones to meet your needs.")

import pandas as pd

dataset = pd.read_csv("phones_data.csv")
st.dataframe(dataset)

st.subheader("GIVE A FEEDBACK")
NAME = st.text_input("GIVE YOUR NAME")
NICKNAME = st.text_input("GIVE YOUR NICKNAME")
ADDRESS = st.text_area("TELL US WHERE YOU ARE FROM")

button = st.button("Done")
if button:
    st.markdown(f"""
                NAME: {NAME}
                NICKNAME: {NICKNAME}
                 ADDRESS : {ADDRESS} """)
