import streamlit as st
import string
st.set_page_config(
    page_title="bohat hard", 
    page_icon="pin-code.png",
    layout="wide"
)
st.title("🔒Password Strength Checker")

password = st.text_input("Enter your password (should contain at least 1 symbol, 1 uppercase letter, and 1 number):", type="password")

if password:
    count_uppercase = 0
    count_digits = 0
    count_symbols = 0

    for char in password:
        if char in string.ascii_uppercase:
            count_uppercase += 1
        elif char in string.digits:
            count_digits += 1
        elif char in string.punctuation:
            count_symbols += 1

    # Display counts
    st.write(f"Uppercase letters: {count_uppercase}")
    st.write(f"Digits: {count_digits}")
    st.write(f"Symbols: {count_symbols}")

    # Check password strength
    if count_uppercase >= 1 and count_digits >= 1 and count_symbols >= 1:
        st.success("Password is strong!")
    elif (count_uppercase >= 1 and count_digits >= 1) or \
         (count_uppercase >= 1 and count_symbols >= 1) or \
         (count_digits >= 1 and count_symbols >= 1):
        st.warning("Password strength is medium ")
        if count_uppercase < 1:
            st.write("- Missing uppercase letter")
        if count_digits < 1:
            st.write("- Missing digit")
        if count_symbols < 1:
            st.write("- Missing symbol")
    elif count_uppercase >= 1 or count_digits >= 1 or count_symbols >= 1:
        st.error("Password is weak ")
        if count_uppercase < 1:
            st.write("- Missing uppercase letter")
        if count_digits < 1:
            st.write("- Missing digit")
        if count_symbols < 1:
            st.write("- Missing symbol")
    else:
        st.error("This is not a valid password format")