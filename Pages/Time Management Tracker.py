import streamlit as st
import json
import pandas as pd



st.header("🔥Time Management Tracker🔥!!")

if 'studyDict' not in st.session_state:
    st.session_state.studyDict = {}
studyGoal = st.slider("What is your weekly study goal(min)?", 0, 500)
studyTime = st.slider("How long did you study today(min)?", 0, 500)
st.session_state.studyDict["Study Time(for Wk)"] = [studyGoal, 0]
st.session_state.studyDict["Study Time(Today)"] = [studyTime]
st.session_state.studyDict["Weekly Time Left"] = [studyGoal-studyTime]
st.bar_chart(data=st.session_state.studyDict) #NEW


def workoutCals(fname):
    numWorkouts = int(st.number_input("How many workouts this week?"))#NEW
    
    infile=open("data.json")
    workData = json.load(infile)[0]
    infile.close()

    option = st.selectbox("What Type of Workout?",("Walk", "Run", "Lifting"),)
    for i in range(0, 3):
        if workData["Activity"][i] == option:
            st.write(f"You have burned {numWorkouts*workData['Calories'][i]} calories this week.")        

workoutCals("data.json")

def screenTime(fname):
    timeDict ={
        "TV":st.number_input("How much time have you spent watching T.V.?"),
    "Phone":st.number_input("How much time have you spent scrolling on your phone?"),
    "Computer":st.number_input("How much time have you spent doing work on a computer?")
     }

    st.bar_chart(data = timeDict)

    if 'workData' not in st.session_state:
        
        infile=open("data.json")
        st.session_state.workData = json.load(infile)[0]
        infile.close()

    st.subheader("Below are the effects of screen time on your grades:")
    
    productive = {}
    productive["ScreenTime"] = st.session_state.workData["Screen Time %"]
    productive["Grades"] = st.session_state.workData["Grade %"]
    st.scatter_chart(data=productive) #NEW
    

screenTime("data.json")

    
st.write("How much have you enjoyed using this tracker?!")
def starSection():
    sentiment_mapping =["one", "two", "three", "four", "five"] #NEW
    selected = st.feedback("stars")
    if selected is not None:
        if sentiment_mapping[selected] == "one":
            st.write(f'😢Only 1 🌟')
        elif sentiment_mapping[selected] == "two":
            st.write(f'2 is better than 1 🌟')
        elif sentiment_mapping[selected] == "three":
            st.write(f'Thanks for 3 🌟')
        elif sentiment_mapping[selected] == "four":
            st.write(f'Yay!! 4🌟😊')
        else:
            st.write(f"✨WOW! 5✨😍!")
        
starSection()
