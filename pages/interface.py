import streamlit as st
from mainPage import switch_page, hide_sidebar
from database import set_choice, get_id, get_name, get_lockout, set_lockout, get_match, set_match, get_match_id

def button_maker(file_name :str, prompt :str, index :int):
   button_pressed = st.button(prompt)
   if get_lockout(get_id()):
      st.write("You can't initialize another meetup while in a meetup!")

   elif button_pressed:
      id1 = get_id()
      set_choice(id1, index)

      if get_match(id1, index):
         id2 = get_match_id(id1, index)
         set_match(id1, id2)
         switch_page(file_name)

hide_sidebar()
      

st.image('icon.png', width=210)
st.header(f'Welcome, {get_name(get_id())}')
st.write("Select where you'd like to meet up with someone at:")


      
button_maker('waitpage', 'Dining Hall', 1)
button_maker('waitpage', 'Gym', 2)
button_maker('waitpage', 'Grocery Store', 3)
button_maker('waitpage', 'Movie Theater', 4)

st.write(' ')
st.write(' ')
st.write(' ')
st.caption("If you're waiting for a match, feel free to initialize another meet up in the meantime. Your account will enter a cooldown period after a match has been made.")

button_pressed = st.button('Sign Out')
if button_pressed:
   switch_page('mainPage')

# displays meetup button if in lockout
if get_lockout(get_id()):
   button_pressed = st.button('Meetup Complete?')
   if button_pressed:
      set_lockout(get_id(), False)