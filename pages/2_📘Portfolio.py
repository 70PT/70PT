import streamlit as st
import base64
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

st.title("Portfolio")

st.write("Things I've built will go here")


