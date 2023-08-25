import streamlit as st
import sqlite3
from hashlib import sha256

# Create a SQLite database
conn = sqlite3.connect("todo.db")
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        task TEXT
    )
''')
conn.commit()

def signup():
    st.subheader("Sign Up")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")

    if st.button("Sign Up"):
        hashed_password = sha256(new_password.encode()).hexdigest()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, hashed_password))
            conn.commit()
            st.success("Account created successfully. You can now log in.")
        except sqlite3.Error as e:
            st.error("Error occurred during sign up.")
            st.error(str(e))


def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        hashed_password = sha256(password.encode()).hexdigest()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        user = c.fetchone()
        if user:
            return True
        else:
            st.error("Invalid username or password")
    return False

def add_task(username):
    st.subheader("Add Task")
    task = st.text_input("Enter a task:")
    if st.button("Add Task"):
        c.execute("INSERT INTO tasks (username, task) VALUES (?, ?)", (username, task))
        conn.commit()
        st.success("Task added!")

def show_tasks(username):
    st.subheader("Your Tasks")
    c.execute("SELECT task FROM tasks WHERE username = ?", (username,))
    tasks = c.fetchall()
    if tasks:
        for idx, task in enumerate(tasks, start=1):
            st.write(f"{idx}. {task[0]}")
    else:
        st.write("No tasks available.")


def main():
    st.title("To-Do List App")
    
    st.sidebar.header("Authentication")
    signup()
    authenticated = login()

    if authenticated:
        st.sidebar.success("Logged in successfully!")
        st.sidebar.subheader("Task Management")
        username = st.sidebar.text_input("Username", key="username")
        add_task(username)
        show_tasks(username)

if __name__ == "__main__":
    main()
