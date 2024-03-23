
import streamlit as st

from coursework.coursework import coursework
from capitaliser.capitaliser import capitaliser

# Importing code display stuff
from code.capitaliser_text import text as capitaliser_text
from code.coursework_text import text as coursework_text


def main():
    # Title
    st.markdown("# ying bing loves :rainbow[a math]!!!!11!11!!")
    st.write("das so cool")

    # Checkbox for A1
    option = st.checkbox("click 4 A1 math")
    if option:
        st.write("user has been bleesed with a1")

    # Text capitaliser
    st.write("---")
    st.subheader("funny text capitaliser")
    text_capitaliser()

    # Coursework
    st.write("---")
    st.subheader("Coursework wooo")
    coursework_section()

    # Code display
    st.write("---")
    code_display()

    # Link to GitHub
    st.write("---")
    github_link()


def text_capitaliser():
    prompt = st.text_input("input here: ", value="hee hee heeeee haweeeeeewwww")
    st.write(capitaliser(prompt))


def coursework_section():
    prompt = st.text_input("How are you feeling?", value="im very happy :)")
    output = coursework(prompt)

    # Output format [emotion, message1, message2, url]
    if output[0] == 0:
        st.write(output[1])
    else:
        st.write(output[1])
        st.link_button("Play video", output[3])
        st.write(output[2])


def code_display():
    option = st.selectbox("code to display", ("capitaliser", "coursework"))

    if option == "capitaliser":
        st.code(capitaliser_text)
    elif option == "coursework":
        st.code(coursework_text)


def github_link():
    st.subheader("The github")
    st.link_button("Github :100:", "https://github.com/Jakeboiegg/st-testing.git")


if __name__ == "__main__":
    main()
