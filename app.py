import json
import streamlit as st

# Hide Streamlit branding
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.title("Network Configurator")
st.write("Fill out input fields and press the 'Generate Config' button.")

user_name = st.text_input("Your Name", value="")
os_info = st.selectbox("What is your operating system", ("Windows", "macOS", "Linux"))


if st.button("Generate Config"):
    # Send post request to store data in database

    data = {"user_name": user_name, "os_info": os_info}
    # Serializing json
    json_data = json.dumps(data, indent=4)
    st.json(json_data)
