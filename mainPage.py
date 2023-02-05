import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")


def switch_page(page_name: str):
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("mainPage.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")

def button_maker(file_name: str, prompt: str):
   button_pressed = st.button(prompt)
   if button_pressed:
      switch_page(file_name)

def hide_sidebar():
    no_sidebar_style = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

st.image('icon.png')
st.header("It's time to make friends, uncurated.")
st.write('Make a selection below to begin.')

button_maker('aboutus', "Start Here")
button_maker('login', 'Log In')





