import streamlit as st
import streamlit_authenticator as sta

def main():
    tasks = []

    def add_task():
        task = st.text_input("Enter a task:")
        if task:
            tasks.append(task)

    def delete_task(i):
        tasks.pop(i)

    # Initialize the authenticator
    authenticator = sta.Auth(
        app_name="To-Do List",
        secret_key="my_secret_key",
    )

    # Authenticate the user
    username, password = authenticator.authenticate()

    if username is not None and password is not None:
        st.title(f"Welcome, {username}!")
        st.table(tasks)
        st.button("Add Task")
        st.button("Delete Task")
    else:
        st.write("Please login to access your tasks")

if __name__ == "__main__":
    main()
