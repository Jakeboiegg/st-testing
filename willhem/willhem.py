import streamlit as st
import random

from .letters import letters


def random_fluff(length):
    fluff_arr = []
    for _ in range(length):
        fluff_arr.append(random.choice(letters))

    return "".join(fluff_arr)


def willhem():
    highest_value = 50
    willhem = ["w", "wm", "wim", "wiem", "wilem", "wilhem", "willhem"]

    number = st.slider("length of will---em name", 0, highest_value)

    with st.container(border=True):
        if number == 0:
            st.write()

        elif 1 <= number <= 7:
            st.write(willhem[number - 1])

        elif 8 <= number <= highest_value:
            fluff = random_fluff(number - 7)
            st.write(f"will{fluff}hem")
