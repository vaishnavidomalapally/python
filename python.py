import streamlit as st


st.title("Student Grade System")


project = st.number_input("Enter Project Marks (0 - 100):", min_value=0, max_value=100, step=1)
internal = st.number_input("Enter Internal Marks (0 - 100):", min_value=0, max_value=100, step=1)
external = st.number_input("Enter External Marks (0 - 100):", min_value=0, max_value=100, step=1)


total = project + internal + external


def calculate_grade(total):
    
    if total >= 200:
        return "A"
    elif total >= 160:
        return "B"
    elif total >= 120:
        return "C"
    elif total >= 1:
        return "D"
    elif total >= 50:
        return "E"
    else:
        return "F"

# Show results
if st.button("Calculate Grade"):
    grade = calculate_grade(total)
    st.success(f"Total Marks: {total} | Grade: {grade}")