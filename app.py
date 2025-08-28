import streamlit as st
import subprocess
from utils.command_utils import run_command

st.set_page_config(page_title="CommandHub", page_icon="⚡", layout="wide")

st.title("⚡ CommandHub – All in One Command & Tool Platform")
st.write("Execute, manage, and monitor essential system commands from a web interface.")

# Input box for command
command = st.text_input("Enter a system command:", "")

if st.button("Run Command"):
    if command.strip():
        output, error = run_command(command)
        st.subheader("Output:")
        st.code(output if output else "No Output", language="bash")
        if error:
            st.subheader("Error:")
            st.code(error, language="bash")
    else:
        st.warning("⚠️ Please enter a valid command.")

# Predefined quick commands
st.subheader("🔥 Quick Commands")
col1, col2, col3 = st.columns(3)

if col1.button("Check Disk Usage"):
    output, error = run_command("df -h")
    st.code(output, language="bash")

if col2.button("List Processes"):
    output, error = run_command("ps aux --sort=-%mem | head -n 10")
    st.code(output, language="bash")

if col3.button("Check Uptime"):
    output, error = run_command("uptime")
    st.code(output, language="bash")
