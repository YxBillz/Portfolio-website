import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("image.jpg")

with col2:
    st.title("Obiri-Ibe Stephen")
    content = """
    I am currently a Business Information Technology student at JAMK University of Applied Sciences with a passion for Python programming and a focus on data analysis, automation, and web development. Combining my technical skills with a business-oriented mindset, I aim to create innovative solutions that bridge the gap between technology and real-world challenges. I’m committed to continuous learning and excited to contribute to impactful projects in the evolving tech industry.
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
        st.write("[Source Code](https://github.com/YxBillz?tab=repositories)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://github.com/YxBillz?tab=repositories)")