import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/Coffee_photo.jpg")

with col2:
    st.title("Rasool Yallanki")
    content = """
    Hello, I’m Rasool, a passionate Python programmer.
    I am currently an undergraduate at Mohan Babu University (MBU)
    and actively seeking internship and job opportunities.
    I have a strong interest in technology and enjoy contributing
    to innovative projects. My goal is to leverage my skills to
    solve real-world problems and grow in the tech industry.
    """
    st.info(content)

content2 = """Below you can find some of the apps
            I have built in Python.
            Please feel free to Contact me!"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write("[Source Code](https://pythonhow.com)")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write("[Source Code](https://pythonhow.com)")


