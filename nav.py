import streamlit as st
def navigate():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "My Streamlit App", "Stock Price App"])

    if selection == "Home":
        st.title("Home Page")
        st.write("Welcome to the Home Page!")
    elif selection == "My Streamlit App":
        import app  # Assuming app.py contains the first snippet
    elif selection == "Stock Price App":
        import myapp  # Assuming myapp.py contains the second snippet
if __name__ == "__main__":
    navigate()
    