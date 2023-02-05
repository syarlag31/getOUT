import streamlit as st
from mainPage import switch_page, button_maker, hide_sidebar

hide_sidebar()

st.image('icon.png')
st.header('About our Project')

st.write("College can be hard.")
st.write("It's the one of the few times in your life that you'll spend surrounded by others your age, yet, nowadays, these peers can feel so far away.")
st.write("We know that perfectly manicured social media posts can be the cause of this, but we believe that social media can also be the solution.")
st.write("Enter **get:blue[OUT]**, an anonymous, filter-free way to get to know those around you.")
st.write("Our application eliminates many of the common anxieties about making friends: it gives the piece of mind that you're meeting with someone that genuinely wants to meet with you and it ensures that you both want to participate in your selected activity.")
st.write("We hope that **get:blue[OUT]** will even serve as a way to help our user's mental health and social anxieties. For example, those who would normally eat a meal by themselves can now spend this time building relationships with others, and those hesitant to go to the gym or dining hall by themselves now have a friend to go with.")
st.write("While **get:blue[OUT]** is stil in early development stages, we hope to one day implement features such as seasonal activities (think corn mazes, sporting events, and even career fairs), and a way to get more personalized matches by including interests into profiles, and an option to make these meetups into group outings.")

button_maker('howTo','Continue')
button_maker('mainPage', 'Back')