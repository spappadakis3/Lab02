import streamlit as st




st.header("Home Page")
st.subheader("My name is Sophia Pappadakis and I am currently taking CS 1301")
st.write("Portfolio: This page contains my portfolio")
st.write("About me: This page contains information about me!")


st.page_link("Home_Page.py", label="Home", icon="🏠")
st.page_link("Pages/portfolio.py", label="Portfolio", icon="1️⃣")
st.page_link("Pages/Time Management Tracker.py", label="About Me", icon="2️⃣")
st.page_link("http://www.google.com", label="Google", icon="🌎")


    
