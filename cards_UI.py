import streamlit as st
import pandas as pd
import base64
import os

# Function to encode the image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set background image
def set_bg_hack(main_bg):
    bin_str = get_base64_of_bin_file(main_bg)
    page_bg_img = '''
    <style>
    .card {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-position: center;
    }
    </style>
    ''' % bin_str
    return page_bg_img

# Read CSV
df = pd.read_csv('conectemos_preguntas.csv')

# Initialize session state
if 'pregunta' not in st.session_state:
    st.session_state.pregunta = df['Preguntas'].sample(1).values[0]

# Function to update question
def update_question():
    st.session_state.pregunta = df['Preguntas'].sample(1).values[0]

# Path to your image
image_path = "conectm.png"

# Check if file exists
if not os.path.exists(image_path):
    st.error(f"Image file not found: {image_path}")
else:
    # Set the background image
    st.markdown(set_bg_hack(image_path), unsafe_allow_html=True)

    # Create a clickable card using st.button
    if st.button('', key='card_button'):
        update_question()

    # Display the card and question
    st.markdown(f"""
    <div class="card-container">
        <div class="card">
            <div class="card-body">
                <p class="card-text">{st.session_state.pregunta}</p>
            </div>
        </div>
    </div>

    <style>
    .card-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 1rem;
    }}

    .card {{
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        border-radius: 15px;
        width: 300px;
        height: 450px;
        color: white;
        overflow: hidden;
    }}

    .card:hover {{
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }}

    .card-body {{
        padding: 20px;
        background-color: rgba(0,0,0,.3);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }}

    .card-text {{
        margin: 0;
        font-size: 18px;
        line-height: 1.5;
    }}

    @media (max-width: 320px) {{
        .card {{
            width: 100%;
            height: 0;
            padding-bottom: 150%;
        }}
    }}

    /* Hide the default button styles */
    .stButton>button {{
        position: absolute;
        width: 300px;
        height: 450px;
        opacity: 0;
        cursor: pointer;
    }}
    </style>
    """, unsafe_allow_html=True)
