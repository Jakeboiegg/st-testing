import streamlit as st

from .code_text.capitaliser_text import text as capitaliser_text
from .code_text.coursework_text import text as coursework_text
from .code_text.willhem_text import text as willhem_text


def code_display():
    option = st.selectbox("code to display", ("capitaliser", "coursework", "willhem"))

    match option:
        case "capitaliser":
            st.code(capitaliser_text)
        case "coursework":
            st.code(coursework_text)
        case "willhem":
            st.code(willhem_text)
