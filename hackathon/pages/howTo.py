import streamlit as st
from mainPage import switch_page, button_maker, hide_sidebar

hide_sidebar()

st.image('icon.png')
st.header('How Things Work')

st.write("Creating an account with **get:blue[OUT]** is easy. All it requires is your name, phone number, and university email address.")
st.write("After successfully creating an account and logging in, you'll be brought to **get:blue[OUT]'s** home page. Here, you'll be able to select what you'd like to do at your meetup!")
st.write("Once you've made your selection, you'll see a confirmation page and recieve a text from **get:blue[OUT]**. This text will contain all of the information that you'll need to begin your meetup, including your partner's name and phone number.")
st.write("From here, it's up to you both! Just be sure to press 'Meetup Complete?' on the home page once you've met up with your match.")
st.write("After this, you'll be free to start your next meetup!")


button_maker('signUpUser','Continue')
button_maker('aboutUs', 'Back')