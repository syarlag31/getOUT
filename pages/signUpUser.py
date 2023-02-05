import streamlit as st
from mainPage import switch_page, hide_sidebar
from database import input_user_info, check_email

hide_sidebar()


st.image('icon.png', width=210)
st.header('Sign Up')
st.write('Enter your information below to begin.')


def get_global_user_email():
   global user_email
   return user_email


with st.form('sign_up'):
   user_name = st.text_input('Full Name')
   user_phone = st.text_input('Phone Number')
   user_email = st.text_input('University Email')
   user_password = st.text_input('Password')
   

   submitted = st.form_submit_button('Submit')
   formated_correctly = False
   while submitted:
      if not (user_email.endswith('@clemson.edu') or user_email.endswith('@uncc.edu')):
         st.write("Please enter an email with a clemson.edu address or a uncc.edu address.")
         submitted = False
         break
      if check_email(user_email) >= 1:
         st.write('This email is in use! Please use another one!')
         submitted = False
         break
      if not(user_phone.isnumeric() and len(user_phone) == 10):
         submitted = False
         break
      formated_correctly = True
      break

   if formated_correctly is True:
      input_user_info(user_email, user_password, user_phone, user_name, '0')
      switch_page('logIn')

button_pressed = st.button("Back")
if button_pressed:
   switch_page('howTo')

