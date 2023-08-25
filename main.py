import streamlit as st

# Mock user data for authentication
users = {
    "user1": "password1",
    "user2": "password2",
}

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            return True
        else:
            st.error("Invalid username or password")
    return False

def main():
    st.title("To-Do List App")
    st.write("Please log in to access your tasks.")

    authenticated = login()

    if authenticated:
        st.success("Logged in successfully!")
        tasks = st.text_area("Enter your task:")
        if st.button("Add Task"):
            st.write(f"Added task: {tasks}")

if __name__ == "__main__":
    main()
