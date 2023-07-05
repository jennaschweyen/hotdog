import matplotlib.pyplot as plt
import pandas as pd
import pickle
import streamlit as st
from  PIL import Image

st.set_page_config(
    page_icon=':hotdog:',
    initial_sidebar_state='expanded'
)

st.title('Hotdog... or not hotdog?')

st.write('Use the sidebar to select a page to view.')

page = st.sidebar.selectbox(
    'Page',
    ('About', 'Hotdog prediction')
)

if page == 'About':
    st.subheader('About this project')
    st.write('''
This Streamlit app hosts my Hotdog model.
We used a convolutional neural network to decipher between 
images of hotdogs and non-hotdogs.
    ''')

elif page == 'Hotdog prediction':
    st.title('Test our model!')

    # Open your model!
    # with open('hotdog.pkl', 'rb') as f:
    #     model = pickle.load(f)

    # Add file uploader to allow users to upload photos
    uploaded_photo = st.file_uploader("", type='jpg')

    # Create model prediction for uploaded photo
    # hotdog_pred = model.predict([uploaded_photo])[0]

    # Create button
    if st.button('Submit'):
        if len(uploaded_photo) ==1:

            if hotdog_pred == 'hotdog':
                st.write('This is a hotdog!')
                st.balloons()

            else:
                st.write('This is NOT a hotdog! :-1:')
