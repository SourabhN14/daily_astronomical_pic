import streamlit as st
import requests

# task
# to create a website which will show daily pages astronomical pic
# of day
#1. Connect with     api.nasa.gov and get api key
#2. have a new project with streamlit and requests imported
#3 using requests try getting the data from api of nasa website
#4 using streamlit publish it on the webpage
#5 make it global

#url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/?api_key=X"

req = requests.get(url)

content1 = req.json()


#print(content)
print(type(content1))

for item in content1[:1]:
    #print("title:",item['title'])
    #print("explanation:",item['explanation'])
    #print("date:",item['date'])
    #print("credit",item['credit'])
    #print("hdurl",item['hdurl'])
    st.title("Daily Astronomy Photographer")
    st.subheader(item['title'])
    st.image(item['hdurl'])
    #st.subheader(item['explanation'],unsafe_allow_html=True)
    st.markdown(item['explanation'], unsafe_allow_html=True)
    st.markdown(item['date'],unsafe_allow_html=True)
    st.markdown("Credit : " + item['credit'],unsafe_allow_html=True)

