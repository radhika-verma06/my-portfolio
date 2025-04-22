import streamlit as st

def celsius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9

st.title("🌡️ Temperature Converter")
conversion_type = st.radio("Choose conversion direction:", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
temp_input = st.text_input("Enter temperature:")

if temp_input:
    try:
        temp = float(temp_input)
        if conversion_type == "Celsius to Fahrenheit":
            result = celsius_to_fahrenheit(temp)
            st.success(f"{temp} °C = {result:.2f} °F")
        else:
            result = fahrenheit_to_celsius(temp)
            st.success(f"{temp} °F = {result:.2f} °C")
    except ValueError:
        st.error("Please enter a valid number.")
