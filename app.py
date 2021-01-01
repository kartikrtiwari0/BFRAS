import streamlit as st

st.title('BEAUTY FACE RECCOMEDATION AND ANALYSIS SYSTEM')
option = st.selectbox(
	 'How would you like to be contacted?',
    ('Email'))
st.write('You selected:', option)
option2 = st.selectbox(
	 'How would you like to be contacted?',
    ('Home phone'))
st.write('You selected:', option2)
option3 = st.selectbox(
	 'How would you like to be contacted?',
    ('Mobile phone'))
st.write('You selected:', option3)
option4 = st.selectbox(
	 'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option4)
option5 = st.selectbox(
	 'How would you like to be contacted?',
    ('Gmail'))
st.write('You selected:', option5)
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
		.reportview-container .main footer {visibility: hidden;}  
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)