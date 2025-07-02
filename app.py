import streamlit as st

st.title("🚀 LaunchCycle: Daily Task Launcher")
st.subheader("Start where you are, use what you have")

energy = st.radio(
    "What's your energy level today?",
    ["Low", "Medium", "High"],
    horizontal=True
)

st.header("🎯 Must Do (1–3 tasks max)")
must1 = st.text_input("Task 1")
must2 = st.text_input("Task 2")
must3 = st.text_input("Task 3")

st.header("🌟 Want To Do (bonus tasks)")
want1 = st.text_input("Bonus Task 1")
want2 = st.text_input("Bonus Task 2")

if st.button("Mark As Done"):
    st.success("🎉 Great job! You’re building momentum.")
    if must1: st.write(f"✅ {must1}")
    if must2: st.write(f"✅ {must2}")
    if must3: st.write(f"✅ {must3}")
    if want1 or want2:
        st.write("Bonus wins:")
        if want1: st.write(f"⭐ {want1}")
        if want2: st.write(f"⭐ {want2}")
