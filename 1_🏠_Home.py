import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from constant import *
from PIL import Image
import openai
from langchain.chat_models import ChatOpenAI

st.set_page_config(page_title='Template' ,layout="wide",page_icon='👧🏻')
st.markdown(
    """
    <style>
    .transparent-container {
        background-color: rgba(255, 255, 255, 0.0) !important;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------  loading assets  ----------------- #
st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# loading assets
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
es_lottie = load_lottieurl("https://lottie.host/9792a89c-fc30-4731-8ff8-4bc4bb4f52d1/j2WhPYASbI.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
bioprocess_lottie = load_lottieurl("https://lottie.host/04857e83-146d-4368-b732-8951a1ab0019/5aJJh1w3a1.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
figma_lottie = load_lottieurl("https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json")
cm_lottie = load_lottieurl("https://lottie.host/c8eed78d-e2ed-4276-8fc7-260202be4a6d/uoL4x2yGZY.json")



# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])
    
    
with col2:
    st_lottie(lottie_gif, height=280, key="data")
        

# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Skills I\'m working on')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        # st_lottie(python_lottie, height=150, width=150, key="python", speed=2.5)
        # st.write("Python")
        st.markdown(
            """
            <div style="text-align: left;">
                <div style="margin-top: -40px; margin-left: 50px;">Python</div>
            </div>
            """.format(st_lottie(python_lottie, height=150, width=150, key="python_lottie", speed=1)),
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div style="text-align: center;">
                <div style="margin-top: -90px; margin-left: 0px;">Embedded systems (Arduino and Rasberry Pi)</div>
            </div>
            """.format(st_lottie(es_lottie, height=200, width=200, key="es_lottie", speed=1)),
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div style="text-align: center;">
                <div style="margin-top: -80px; margin-left: 0px;">Databases (mostly SQL)</div>
            </div>
            """.format(st_lottie(my_sql_lottie, height=200, width=200, key="my_sql_lottie", speed=1)),
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
            """
            <div style="text-align: center;">
                <div style="margin-top: -40px; margin-left: -40px;">Bioprocess Scale Up</div>
            </div>
            """.format(st_lottie(bioprocess_lottie, height=150, width=150, key="bioprocess_lottie", speed=2.5)),
            unsafe_allow_html=True
        )
    # with col1:
    #     st_lottie(github_lottie,height=50,width=50, key="github", speed=2.5)
    #     st.write("test")
    # with col2:
    #     st_lottie(docker_lottie,height=70,width=70, key="docker", speed=2.5)
    #     st.write("test")
    # with col3:
    #     st_lottie(figma_lottie,height=50,width=50, key="figma", speed=2.5)
    #     st.write("test")
    # with col4:
    #     st_lottie(cm_lottie,height=50,width=50, key="js", speed=1)
    #     st.write("Cultivated Meat Ops and R&D")
    
    
# ----------------- timeline ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('📌 Career Snapshot')
    import streamlit as st

    # Set the URL of the timeline you want to embed
    timeline_url = "https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=121bT5tY_rAi3MZp5l7HA20_ocJnVI4-YvW06n7-nFQI&font=Default&lang=en&initial_zoom=2&height=650"

    # Set the height of the iframe
    iframe_height = 650

    # Embed the timeline using st.components.v1.iframe
    st.components.v1.iframe(timeline_url, height=iframe_height)


# -----------------  tableau  -----------------  #
# with st.container():
#     st.markdown("""""")
#     st.subheader("📊 Tableau")
#     col1,col2 = st.columns([0.95, 0.05])
#     with col1:
#         with st.expander('See the work'):
#             components.html(
#                 """
#                 <!DOCTYPE html>
#                 <html>  
#                     <title>Basic HTML</title>  
#                     <body style="width:130%">  
#                         <div class='tableauPlaceholder' id='viz1684205791200' style='position: static'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SunnybrookTeam&#47;Overview&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SunnybrookTeam&#47;Overview' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SunnybrookTeam&#47;Overview&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684205791200');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1350px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='1550px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1350px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='1550px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='5750px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
#                     </body>  
#                 </HTML>
#                 """
#             , height=400, scrolling=True
#             )
#     st.markdown(""" <a href={}> <em>🔗 access to the link </a>""".format(info['Tableau']), unsafe_allow_html=True)
    
# # ----------------- medium ----------------- #
# with st.container():
#     st.markdown("""""")
#     st.subheader('✍️ Medium')
#     col1,col2 = st.columns([0.95, 0.05])
#     with col1:
#         with st.expander('Display my latest posts'):
#             components.html(embed_rss['rss'],height=400)
            
#         st.markdown(""" <a href={}> <em>🔗 access to the link </a>""".format(info['Medium']), unsafe_allow_html=True)

# -----------------  endorsement  ----------------- #
with st.container():
    # Divide the container into three columns
    col1,col2,col3 = st.columns([0.475, 0.475, 0.05])
    # In the first column (col1)        
    with col1:
        # Add a subheader to introduce the coworker endorsement slideshow
        st.subheader("Other things to look out for")
        # Embed an HTML component to display the slideshow
        components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Styles for the slideshow -->
        <style>
            </style>
        <div>
        st.text("test")
        </div>
        <div>
        st.text("test")
        </div>
        </head>
        <body>


        </body>
        </html> 

        """, height=270,)  

# -----------------  contact  ----------------- #
    with col2:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
