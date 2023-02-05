import streamlit as st
from mainPage import switch_page, hide_sidebar
from database import get_user_info
from emailGenerator import email_gen

hide_sidebar()

st.image('icon.png', width = 210)
st.header('Verify Your Email')
st.caption(f"Check {variable(0)} for an email containing a verification code from getoutauthentication@gmail.com. If you haven't recieved an email within 5 minutes, reload the page.")


with st.form('email_verification'):
   email_verification = st.text_input('Verification Code')
   submitted = st.form_submit_button('Submit')

#print(email_gen(user_email))
   if submitted:
      if (email_gen(variable(0)) == int(email_verification)):
         switch_page('interface')
      else:
         st.write("The wrong code was entered. Please verify you've copied the code from the email exactly and try again.")