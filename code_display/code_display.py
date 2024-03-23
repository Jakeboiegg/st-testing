import streamlit as st

from .capitaliser_text import text as capitaliser_text
from .coursework_text import text as coursework_text


def code_display():
    option = st.selectbox("code to display", ("capitaliser", "coursework"))

    if option == "capitaliser":
        st.code(capitaliser_text)
    elif option == "coursework":
        st.code(coursework_text)
