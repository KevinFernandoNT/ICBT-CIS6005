import streamlit as st
import numpy as np
import pickle

# Load the scaler, model, and label encoder
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('introvert_extrovert_classifier.pkl', 'rb') as f:
    model = pickle.load(f)
with open('label_encorder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

st.set_page_config(page_title='Introvert Classifier')

# Add custom CSS for styling
st.markdown('''
    <style>
    html, body, [class^="st"], [class*=" st"], .main, h1, h2, h3, h4, h5, h6, p, span, label, div, .stButton>button, .stCheckbox label, .stRadio label, .stSlider label, .stTextInput, .stSelectbox, .stSuccess {
        color: #000 !important;
    }
    body {
        background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
        font-family: 'Segoe UI', 'Roboto', sans-serif;
    }
    .main {
        background-color: #fff7f0;
        border-radius: 18px;
        padding: 2.5rem 2rem 2rem 2rem;
        margin-top: 2rem;
        box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);
    }
    h1, h2, h3, h4 {
        font-weight: 700;
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff7e5f 0%, #feb47b 100%);
        border: none;
        border-radius: 8px;
        padding: 0.75em 2em;
        font-size: 1.1em;
        font-weight: 600;
        margin-top: 1em;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #feb47b 0%, #ff7e5f 100%);
        box-shadow: 0 2px 8px #ff7e5f33;
    }
    .stSlider, .stCheckbox, .stSelectbox, .stTextInput {
        background: #fff3e6;
        border-radius: 8px;
        padding: 0.5em;
        margin-bottom: 1em;
    }
    .stCheckbox label, .stRadio label, .stSlider label {
        font-weight: 500;
    }
    .stSuccess {
        background: #e0ffe0 !important;
        border-radius: 8px;
        font-weight: 600;
    }
    hr {
        border: none;
        border-top: 2px solid #ffb88c;
        margin: 2em 0 1.5em 0;
    }
    /* Modal font size and style */
    .custom-modal h2 {
        font-size: 1.1em !important;
        margin-bottom: 0.7em;
    }
    .custom-modal button {
        font-size: 1em !important;
        padding: 0.5em 1.5em !important;
    }
    </style>
''', unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<h1>Submission CIS6005 - Jude Kevin Fernando (GM/BSCSD/04/07)</h1>', unsafe_allow_html=True)

st.markdown('<h1>🧑‍🤝‍🧑 Introvert vs Extrovert Classifier</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size:1.2em;color:#444;">Fill in the details below to find out if a person is likely an <b>Extrovert</b> or <b>Introvert</b>!</p>', unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)

# Helper for modal popup
if 'show_modal' not in st.session_state:
    st.session_state['show_modal'] = False

# 1. Time_spent_Alone
st.markdown('<span style="color:#000;font-weight:600;">Time spent alone (0 = Never, 10 = Always)</span>', unsafe_allow_html=True)
Time_spent_Alone = st.slider('', 0, 10, 5, key='alone_slider')

# 2. Stage Fear
st.markdown('<span style="color:#000;font-weight:600;">Do you have stage fear?</span>', unsafe_allow_html=True)
stage_fear_option = st.radio('', ['Yes', 'No'], horizontal=True, key='stage_fear_radio')
Stage_fear_val = 1 if stage_fear_option == 'Yes' else 0

# 3. Social_event_attendance
st.markdown('<span style="color:#000;font-weight:600;">Social event attendance (0 = Never, 10 = Always)</span>', unsafe_allow_html=True)
Social_event_attendance = st.slider('', 0, 10, 5, key='event_slider')

st.markdown('<hr>', unsafe_allow_html=True)

# 4. Going_outside
st.markdown('<h4 style="color:#000;">How often do you go outside?</h4>', unsafe_allow_html=True)
going_outside_options = [
    ('1-2 days a week', 1.5),
    ('3-4 days a week', 3.5),
    ('5-6 days a week', 5.5),
    ('Everyday', 7)
]
going_outside_label_to_val = {label: avg for label, avg in going_outside_options}
going_outside_selected = st.radio('', [label for label, _ in going_outside_options], key='go_outside_radio', horizontal=False)
Going_outside = going_outside_label_to_val.get(going_outside_selected, None)

# 5. Friends_circle_size
st.markdown('<h4 style="color:#000;">How many friends are in your circle?</h4>', unsafe_allow_html=True)
friends_circle_options = [
    ('None', 0),
    ('1-5', 3),
    ('6-10', 8),
    ('11-20', 15.5),
    ('21+', 25)
]
friends_circle_label_to_val = {label: avg for label, avg in friends_circle_options}
friends_circle_selected = st.radio('', [label for label, _ in friends_circle_options], key='friends_circle_radio', horizontal=False)
Friends_circle_size = friends_circle_label_to_val.get(friends_circle_selected, None)

# 6. Post_frequency
st.markdown('<h4 style="color:#000;">How often do you post on social media?</h4>', unsafe_allow_html=True)
post_freq_options = [
    ('Do not post anything', 0),
    ('1-2 days a week', 1.5),
    ('3-4 days a week', 3.5),
    ('5-6 days a week', 5.5),
    ('Everyday', 7)
]
post_freq_label_to_val = {label: avg for label, avg in post_freq_options}
post_freq_selected = st.radio('', [label for label, _ in post_freq_options], key='post_freq_radio', horizontal=False)
Post_frequency = post_freq_label_to_val.get(post_freq_selected, None)

# 7. Drained_after_socializing
st.markdown('<span style="color:#000;font-weight:600;">Do you feel drained after socializing?</span>', unsafe_allow_html=True)
drained_option = st.radio('', ['Yes', 'No'], horizontal=True, key='drained_radio')
Drained_after_socializing_val = 1 if drained_option == 'Yes' else 0

# Prepare input for model
features = None
if None not in [Time_spent_Alone, Stage_fear_val, Social_event_attendance, Going_outside, Drained_after_socializing_val, Friends_circle_size, Post_frequency]:
    features = np.array([
        Time_spent_Alone,
        Stage_fear_val,
        Social_event_attendance,
        Going_outside,
        Drained_after_socializing_val,
        Friends_circle_size,
        Post_frequency
    ]).reshape(1, -1)

# Predict
if st.button('Predict'):
    if features is None:
        st.error('Please answer all the questions.')
    else:
        features_scaled = scaler.transform(features)
        pred = model.predict(features_scaled)
        result = label_encoder.inverse_transform(pred)[0]
        st.success(f'The model predicts: **{result}**')

st.markdown('</div>', unsafe_allow_html=True) 