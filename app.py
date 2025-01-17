import streamlit as st
from connection import Connection

# Play an animation
def animation(button_name):
    st.session_state.behavior_mng_service.stopAllBehaviors()
    st.session_state.behavior_mng_service.startBehavior("questacon/"+button_name)

#creating the connection
if 'pepper' not in st.session_state:
    st.session_state.pepper = Connection()
    ip='localhost'
    # ip='127.0.0.1'
    port=42535
    # ip='10.0.0.244'
    # ip='192.168.1.53'
    # port=9559
    st.session_state.session = st.session_state.pepper.connect(ip, port)

    # Create a proxy to the AL services
    st.session_state.behavior_mng_service = st.session_state.session.service("ALBehaviorManager")

# UI layout
st.markdown("<h1 style='text-align: center;'>Questacon App</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([3,1])
with col1:
    st.header("Interactive Actions with Pepper")
    st.text("Click any button below to see Pepper in action:")
with col2:
    st.write("")
    st.write("")
    st.write("")
    if st.button("\nStop Animation\n", type="primary"):  # Create the button
        st.session_state.behavior_mng_service.stopAllBehaviors()
        animation("stand")
        st.success("Button pressed...")
# Apply CSS to ensure buttons have the same width
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.subheader("Dialog Animations")

# Create two columns for the 7 buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Space & time"):
        animation("space_and_time")
        st.success("Button pressed...")
    if st.button("Self & others"):
        animation("self_and_others")
        st.success("Button pressed...")
    if st.button("Affirmation"):
        animation("affirmation")
        st.success("Button pressed...")
    if st.button("Negation"):
        animation("negation")
        st.success("Button pressed...")

with col2:
    if st.button("Question"):
        animation("question")
        st.success("Button pressed...")
    if st.button("Exclamation"):
        animation("exclamation")
        st.success("Button pressed...")
    if st.button("Enumeration"):
        animation("enumeration")
        st.success("Button pressed...")


st.subheader("Moods")

# Create two columns for the 9 buttons
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h3 style='text-align: center;'>Positive</h3>", unsafe_allow_html=True)
    if st.button("Happy"):
        animation("happy")
        st.success("Button pressed...")
    if st.button("Kisses"):
        animation("kisses")
        st.success("Button pressed...")
    if st.button("Excited"):
        animation("excited")
        st.success("Button pressed...")

with col2:
    st.markdown("<h3 style='text-align: center;'>Neutral</h3>", unsafe_allow_html=True)
    if st.button("Thinking"):
        animation("thinking")
        st.success("Button pressed...")
    if st.button("Curious"):
        animation("curious")
        st.success("Button pressed...")
    if st.button("Chill"):
        animation("chill")
        st.success("Button pressed...")

with col3:
    st.markdown("<h3 style='text-align: center;'>Negative</h3>", unsafe_allow_html=True)
    if st.button("Fear"):
        animation("fear")
        st.success("Button pressed...")
    if st.button("Confused"):
        animation("confused")
        st.success("Button pressed...")
    if st.button("Bored"):
        animation("bored")
        st.success("Button pressed...")