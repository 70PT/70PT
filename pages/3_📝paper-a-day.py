import streamlit as st
from PIL import Image
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

st.title("Paper-every-other-day")
st.text("The premise of this page is to track my reads and probably critique them")



