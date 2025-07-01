import streamlit as st
import json
from datetime import date
from datetime import datetime
import os


DATA_FILE = "tracker.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)





st.title("📅 Weekly Progress Tracker")

task = st.text_input("Task Name")
how = st.text_area("How did you complete it?")
status = st.selectbox("Status", ["Pending", "Completed"])
week = st.text_input("Week (e.g., 2025-W27)", datetime.now().strftime("2025-W%U"))
today = date.today().isoformat()

if st.button("Add Task"):
    data = load_data()
    new_task = {
        "week": week,
        "task": task,
        "status": status,
        "how": how,
        "date": today
    }
    data.append(new_task)
    save_data(data)
    st.success("Task added successfully!")




st.subheader("📋 Weekly Tasks")
data = load_data()
selected_week = st.selectbox("Filter by Week", ["All"] + sorted({d["week"] for d in data}))

if selected_week != "All":
    data = [d for d in data if d["week"] == selected_week]

for d in data:
    st.markdown(f"""
    - **{d['task']}** ({d['status']})  
      ➤ _{d['how']}_  
      📅 {d['date']} | 🗓️ Week: {d['week']}
    """)
