import streamlit as st
import pyrebase

config = {
  "apiKey": "AIzaSyAIx800R8uEyErKdDDC4nuF9j42s6MqmVA",
  "authDomain": "bfras-d8b76.firebaseapp.com",
  "databaseURL": "https://bfras-d8b76-default-rtdb.firebaseio.com",
  "storageBucket": "bfras-d8b76.appspot.com"
}

firebase = pyrebase.initialize_app(config)
firebase.database()
db = firebase.database()


st.title('BEAUTY FACE RECCOMEDATION AND ANALYSIS SYSTEM')
option = st.selectbox(
	 'What is the name for the Jewish New Year?',
    ('Select option','Hanukkah' , 'Yom Kippur' , 'Kwanza' , 'Rosh Hashanah'))
st.write('You selected:', option)
option2 = st.selectbox(
	 'How many blue stripes are there on the U.S. flag?',
    ('Select option','6' , '7' , '13' , '0'))
st.write('You selected:', option2)
option3 = st.selectbox(
	 'Which one of these characters is not friends with Harry Potter?',
    ('Select option','Ron Weasley' , 'Neville Longbottom' , 'Draco Malfoy' ,'Hermione Granger'))
st.write('You selected:', option3)
option4 = st.selectbox(
	 'What is the color of Donald Duck’s bowtie??',
    ('Select option','Red', 'Yellow', 'Blue' , 'White'))
st.write('You selected:', option4)
option5 = st.selectbox(
	 'What was the name of the band Lionel Richie was a part of?',
    ('Select option','King Harvest' , 'Spectrums' , 'Commodores' , 'The Marshall Tucker Band'))
st.write('You selected:', option5)
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
		.reportview-container .main footer {visibility: hidden;}  
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
input = st.sidebar.text_input('Enter your full name')
if st.button('Submit'):
     st.success('Your response was registered')
     data = {"q1": option, "q2":option2 , "q3":option3 , "q4":option4,"q5":option5}
     db.child("Responses").push(data)
