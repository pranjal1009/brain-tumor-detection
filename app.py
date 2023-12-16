import streamlit as st
from PIL import Image
import time



st.header('Hi! From MITAOE :smiley: ')
st.header('Brain Tumor Detection')

image = Image.open('mitaoe-logo-2.png')
image = image.resize((250,250))
st.image(image)

st.subheader('Group Members:')
st.text('Pranjal Patil')
st.text('Rachi Wasnik')
st.text('Isha Chatap')

st.header('Upload the Brain Image (.png or .jpg or .jpeg)')
img_main = st.file_uploader('Upload a PNG image', type=['png', 'jpg', 'jpeg'])
st.divider()

if img_main is not None:
    st.subheader('File is getting analyzed')
    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.error('Internal Server Error', icon="🚨")
else:
    st.subheader(':heavy_exclamation_mark: Please upload the image')