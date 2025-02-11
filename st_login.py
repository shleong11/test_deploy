import streamlit as st

# Hardcoded password (For production, use a secure method!)
PASSWORD = "mysecurepassword"

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Function to check password
def login():
    """Checks password and updates session state."""
    if st.session_state.password == PASSWORD:
        st.session_state.authenticated = True
        st.success("✅ Login successful!")
    else:
        st.session_state.authenticated = False
        st.error("❌ Incorrect password. Try again.")

# Authentication check
if not st.session_state.authenticated:
    st.title("🔒 Secure Login")
    st.text_input("Enter Password:", type="password", key="password", on_change=login)
    st.stop()  # Stop execution if not logged in

# Main App Content (Only visible after login)
st.title("📊 Welcome to the Secure Streamlit App")
st.write("This is the main content of your application.")