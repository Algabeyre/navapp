import streamlit as st

# find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Streamlit App", page_icon=":soccer:", layout="wide")

with st.container():
    st.subheader("Welcome to My Streamlit App! :wave:")
    st.title("Building Interactive Web Apps with Streamlit :computer:")
    st.write("This is a simple Streamlit application that demonstrates how to create interactive web apps easily. :sparkles:")
    st.write("Learn More > Streamlit: https://algabeyre.site :books:")


#--- WHAT I DO ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            - I build interactive web applications using Streamlit.
            - I create data visualizations to help understand complex datasets.
            - I develop machine learning models to solve real-world problems.
            - I collaborate with cross-functional teams to deliver impactful solutions.
            """
        )
        st.write("[Youtube Channel >](https://www.youtube.com/c/AlgaBeyre)")
    with right_column:
        st.image("https://images.unsplash.com/photo-1504384308090-c894fdcc538d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y29kZXJ8ZW58MHx8MHx8fDA%3D&w=1000&q=80")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            - I build interactive web applications using Streamlit.
            - I create data visualizations to help understand complex datasets.
            - I develop machine learning models to solve real-world problems.
            - I collaborate with cross-functional teams to deliver impactful solutions.
            """
        )
 
    st.video("https://www.youtube.com/watch?v=JwSS70SZdyM")


