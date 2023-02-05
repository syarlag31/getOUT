import streamlit as st
from mainPage import switch_page, hide_sidebar

def button_maker(file_name :str, prompt :str):
   button_pressed = st.button(prompt)
   if button_pressed:
      switch_page(file_name)

hide_sidebar()

st.image('icon.png', width=210)
st.header('Congratulations!')
st.write("You're almost ready to **get:blue[OUT]**! Be on the lookout for a text from 7048846103 containing the details of your meet up.")

button_maker('interface', 'Back')