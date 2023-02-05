import streamlit as st
from mainPage import switch_page, hide_sidebar
from database import check_info, set_id

hide_sidebar()

st.image('icon.png', width=210)
st.header('Log In')
st.write('Welcome back. Enter your information below to continue.')



with st.form('log_in'):
   user_email = st.text_input('University Email')
   user_password = st.text_input('Password')
   
   

   submitted = st.form_submit_button('Submit')
   if submitted:
      if check_info(user_email, user_password):
         set_id(user_email, user_password)
         switch_page('interface')
      else:
         st.write('The email and password entered do not match. Please try again.')

      # add in if valid user, then go to main page

button_pressed = st.button("Back")
if button_pressed:
   switch_page('mainPage')
      