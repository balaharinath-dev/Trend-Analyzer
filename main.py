import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Social Trend",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

import base64

# Hide Streamlit default elements
hide_streamlit_style = """
    <style>
        
        .stApp {
            background-color: #ffffff
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1500px;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load local image and encode to base64
image_path = './prodapt_new.png'  # replace with your image file path
with open(image_path, "rb") as file:
    img_bytes = file.read()
encoded = base64.b64encode(img_bytes).decode()

# Inject CSS + image tag for absolute positioning
st.markdown(
    f"""
    <style>
    .top-left-image {{
        position: absolute;
        top: 10px;
        left: 0px;
        width: 150px;  /* Adjust width as needed */
        height: auto;  /* Keeps aspect ratio */
        z-index: 999;  /* Makes sure it's on top of other elements */
    }}
    </style>
    <img src="data:image/png;base64,{encoded}" class="top-left-image">
    """,
    unsafe_allow_html=True
)

# Custom CSS for styling
st.markdown("""
<style>

    /* Main heading style */
    .main-heading {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 15px !important;
        color: #333;
        background: -webkit-linear-gradient(#09122C, #D84040);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        
    }
    
    .synapt:{
        margin-bottom: 3rem !important;
    }
    
    /* Subheading style */
    .sub-heading {
        text-align: center;
        font-size: 1.2rem;
        color: #6c757d;
        margin-bottom: 3rem;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Card styling */
    .social-card {
        background: white;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        padding: 2.5rem;
        height: 450px !important;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        overflow: hidden;
        z-index: 1;
    }
    
    .social-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 8px;
        z-index: 2;
    }
    
    .instagram-card::before {
        background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
    }
    
    .youtube-card::before {
        background: #FF0000;
    }
    
    .twitter-card::before {
        background: #1DA1F2;
    }
    
    .social-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
    }
    
    /* Icon styling */
    .icon-container {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1.5rem;
        position: relative;
    }
    
    .instagram-icon-container {
        background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
    }
    
    .youtube-icon-container {
        background: #FF0000;
    }
    
    .twitter-icon-container {
        background: #000000;
    }
    
    .social-icon {
        font-size: 2.5rem;
        color: white;
    }
    
    /* Title styling */
    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #333;
    }
    
    /* Text styling */
    .card-text {
        color: #6c757d;
        margin-bottom: 1.5rem;
        line-height: 1.6;
        font-size: 1rem;
    }
    
    /* Button styling */
    .social-btn {
        padding: 0.7rem 2rem;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        color: white !important;
        font-size: 1rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .instagram-btn {
        background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
    }
    
    .youtube-btn {
        background: #FF0000;
    }
    
    .twitter-btn {
        background: #1DA1F2;
    }
    
    .social-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        opacity: 0.95;
    }
    
    /* Container for cards */
    .cards-container {
        display: flex;
        justify-content: center;
        padding: 2rem 0;
        gap: 2rem;
    }
    
    /* Responsive design */
    @media (max-width: 900px) {
        .cards-container {
            flex-direction: column;
            align-items: center;
        }
        
        .social-card {
            max-width: 400px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Load FontAwesome for icons
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

image_file = './synapt.png'
with open(image_file, "rb") as file:
    img_bytes = file.read()

# Encode it as base64
import base64
encoded = base64.b64encode(img_bytes).decode()

# Page content
st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content:center">
        <h1 class="main-heading" style="">Social Trend Analyzer by</h1>
        <img src="data:image/png;base64,{encoded}" class="synapt" alt="synapt" width="150" height="60">
    </div>
    """,
    unsafe_allow_html=True
)

# Create the grid layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="social-card instagram-card">
        <div class="icon-container instagram-icon-container">
            <i class="fab fa-instagram social-icon"></i>
        </div>
        <h3 class="card-title">Instagram</h3>
        <p class="card-text">Follow us for beautiful visuals, behind-the-scenes content, and daily inspiration.</p>
        <a href="https://instagram-trend-analyzer.streamlit.app/" target="_self" class="social-btn instagram-btn">Let's Go!</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="social-card youtube-card">
        <div class="icon-container youtube-icon-container">
            <i class="fab fa-youtube social-icon"></i>
        </div>
        <h3 class="card-title">YouTube</h3>
        <p class="card-text">Subscribe for video tutorials, product showcases, and live streams. Don't forget to hit the bell icon!</p>
        <a href="https://youtube-trend-analyzer.streamlit.app/" target="_self" class="social-btn youtube-btn">Let's Go!</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="social-card twitter-card">
        <div class="icon-container twitter-icon-container">
            <img src="https://static.vecteezy.com/system/resources/previews/027/395/710/original/twitter-brand-new-logo-3-d-with-new-x-shaped-graphic-of-the-world-s-most-popular-social-media-free-png.png"/>
        </div>
        <h3 class="card-title">X (Twitter)</h3>
        <p class="card-text">Stay updated with our latest news, announcements, and join the conversation with our team.</p>
        <a href="https://twitter-trend-analyzer.streamlit.app/" target="_self" class="social-btn twitter-btn">Let's Go!</a>
    </div>
    """, unsafe_allow_html=True)