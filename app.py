import streamlit as st
import pyrebase
from PIL import Image
import uuid
import cv2 

FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

if st.sidebar.button('CAPTURE IMAGE'):
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    RGB_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    saved_image='filename.jpg'

    #FRAME_WINDOW.image(frame)

    st.sidebar.image(saved_image , width=250, height=250,channels='RGB')
    cv2.imwrite('filename.jpg', RGB_img)

    

else:
    print('kartik op')

config = {
  "apiKey": "AIzaSyAIx800R8uEyErKdDDC4nuF9j42s6MqmVA",
  "authDomain": "bfras-d8b76.firebaseapp.com",
  "databaseURL": "https://bfras-d8b76-default-rtdb.firebaseio.com",
  "storageBucket": "bfras-d8b76.appspot.com"
}

firebase = pyrebase.initialize_app(config)
firebase.database()
db = firebase.database()
storage = firebase.storage()


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

Side_title = st.sidebar.title('ENTER INFO')
image_file = st.sidebar.file_uploader("Upload Image",type=['jpg'])

input_name = st.sidebar.text_input('Enter your full name')
input_email = st.sidebar.text_input('Email')
input_age = st.sidebar.text_input('Age')
input_gender = st.sidebar.text_input('Gender')
karik_image = "filename.jpg"

if image_file is not None:
	image_name = image_file.name
else:
	image_name = "Not uploaded image"

if image_file is not None:
            our_image = Image.open(image_file)
            saved = our_image.save('out.jpg')
            st.sidebar.image(our_image , width=250, height=250,channels='RGB')

if st.button('Submit'):
    st.success('Your response was registered')
     
    storage.child(str(uuid.uuid4())).put("filename.jpg")
    storage.child(image_name).put('out.jpg')
     

    #image_url = storage.child(image_name).get_url(image_name)
    data = {"image_name":image_name , "user_name":input_name , "user_email":input_email, "user_age":input_age , "user_gender":input_gender,'image_name':image_name,"q1_a": option, "q2_a":option2 , "q3_a":option3 , "q4_a":option4,"q5_a":option5}
    db.child("Responses").push(data)
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
		.reportview-container .main footer {visibility: hidden;}  
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
    
     




