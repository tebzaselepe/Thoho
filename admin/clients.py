import streamlit as st

from streamlit_extras.switch_page_button import switch_page

want_to_contribute = st.button("I want to contribute!")
if want_to_contribute:
    switch_page("About")