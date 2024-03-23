import streamlit as st

from coursework.coursework import coursework
from capitaliser.capitaliser import capitaliser
from willhem.willhem import willhem


def main():
    # Title
    st.markdown("# ying bing loves :rainbow[a math]!!!!11!11!!")
    st.write("das so cool")

    # Checkbox for A1
    option = st.checkbox("click 4 A1 math")
    with st.container(border=True):
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

    # willhem
    st.write("---")
    st.subheader("lore accurate willonthouehm name")
    willhem()

    # Link to GitHub
    st.write("---")
    github_link()


def text_capitaliser():
    prompt = st.text_input("input here: ", value="hee hee heeeee haweeeeeewwww")
    with st.container(border=True):
        st.write(capitaliser(prompt))


def coursework_section():
    prompt = st.text_input("How are you feeling?", value="im very happy :)")
    output = coursework(prompt)

    # Output format [emotion, message1, message2, url]
    with st.container(border=True):
        if output[0] == 0:
            st.write(output[1])
        else:
            st.write(output[1])
            st.link_button("Play video", output[3])
            st.write(output[2])


def github_link():
    st.subheader("The github")
    st.link_button("Github :100:", "https://github.com/Jakeboiegg/st-testing.git")


if __name__ == "__main__":
    main()
