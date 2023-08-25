import streamlit as st

def main():
    tasks = []

    def add_task():
        task = st.text_input("Enter a task:")
        if task:
            tasks.append(task)

    def delete_task(i):
        tasks.pop(i)

    username, password = st.auth(
        login_message="Please login to access your tasks",
        password_required=True,
    )

    if username is not None and password is not None:
        st.title(f"Welcome, {username}!")
        st.table(tasks)
        st.button("Add Task")
        st.button("Delete Task")
    else:
        st.write("Please login to access your tasks")

if __name__ == "__main__":
    main()
