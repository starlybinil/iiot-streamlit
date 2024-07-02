import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.write("# Welcome to IIoT Factory Dashboard! 👋👌")
st.sidebar.header("Home")
st.markdown(
    """
    IIoT is a factory dashboard example built specifically to test the MQTT protocol.
    **👈 Select a demo from the sidebar** to see some examples
    of what the Dashboard can do!
    ### Read about the NSF Sponsored Proto-OKN projects
    - Read about the code base at [Github](https://www.proto-okn.net/)  
"""
)