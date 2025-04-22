import streamlit as st

def is_valid_number(user_input):
    return user_input.strip().lstrip('+-').isdigit()

st.title("🔢 Even or Odd Checker")
st.write("Enter a number to check if it's even or odd.")

user_input = st.text_input("Enter a number:")

if user_input:
    if is_valid_number(user_input):
        number = int(user_input)
        if number % 2 == 0:
            st.success(f"{number} is even ✅")
        else:
            st.success(f"{number} is odd 🔢")
    else:
        st.error("Please enter a valid integer (no letters or special characters).")
