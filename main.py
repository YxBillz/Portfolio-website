import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("image.jpg")

with col2:
    st.title("Obiri-Ibe Stephen")
    content = """
    Hello! I'm a passionate Business Information Technology student at JAMK University of Applied Sciences Jyväskylä and I'm currently diving deep into the world of Python programming. My academic background has provided me with a good foundation in technology and business integration, and I am now equipping myself with the skills to thrive in the evolving tech industry.
I’m currently focused on mastering Python, where I’m exploring its applications in data analysis, automation, and web development. My enthusiasm for learning and problem-solving drives me to create innovative solutions that bridge the gap between technology and real-world challenges.
    """
    st.info(content)

content2 = """
You can find some of the apps I have built in python below. Please, feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://.com)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://.com)")