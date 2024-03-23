import streamlit as st

from .capitaliser_text import text as capitaliser_text
from .coursework_text import text as coursework_text
from .willhem_text import text as willhem_text


def code_display():
    option = st.selectbox("code to display", ("capitaliser", "coursework", "willhem"))

    match option:
        case "capitaliser":
            st.code(capitaliser_text)
        case "coursework":
            st.code(coursework_text)
        case "willhem":
            st.code(willhem_text)
