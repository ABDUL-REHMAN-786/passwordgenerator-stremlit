import streamlit as st
import re
import random
import string
import hashlib
import requests
from cryptography.fernet import Fernet

# AES-256 Encryption Key (Generate once and store securely)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# Function to check password strength
def check_password_strength(pwd):
    score = 0
    feedback = []

    if len(pwd) >= 8:
        score += 1
    else:
        feedback.append("Increase password length to at least 8 characters.")

    if re.search(r"[A-Z]", pwd):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", pwd):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if re.search(r"\d", pwd):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")

    if re.search(r"[!@#$%^&*]", pwd):
        score += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&*).")

    if score == 5:
        return "Strong", score, feedback
    elif score >= 3:
        return "Moderate", score, feedback
    else:
        return "Weak", score, feedback

# Function to generate a strong random password
def generate_password(length=12, use_digits=True, use_specials=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += "!@#$%^&*"

    return ''.join(random.choice(characters) for _ in range(length))

# Function to check if the password has been leaked (Have I Been Pwned API)
def check_breach(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    first5, rest = sha1_hash[:5], sha1_hash[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
    
    if response.status_code == 200:
        if rest in response.text:
            return True
    return False

# Function to encrypt passwords
def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

# Function to decrypt passwords
def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

# Streamlit UI
st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered", initial_sidebar_state="expanded")

st.title("🔐 Password Strength Meter")
st.write("Enter a password to check its security strength.")

# Password Input
password = st.text_input("Enter Password:", type="password")

if password:
    strength, score, feedback = check_password_strength(password)
    
    # Strength bar
    st.progress(score / 5)
    
    # Display strength level
    if strength == "Strong":
        st.success("✅ Strong Password! Well done!")
    elif strength == "Moderate":
        st.warning("⚠️ Moderate Password! Consider improving it.")
    else:
        st.error("❌ Weak Password! Please improve your password security.")

    # Improvement suggestions
    if feedback:
        st.write("🔹 Suggestions to Improve:")
        for tip in feedback:
            st.write(f"   - {tip}")

    # Check if password is breached
    if st.button("Check Breach Status"):
        with st.spinner("Checking..."):
            if check_breach(password):
                st.error("⚠️ This password has been leaked in data breaches. Please change it!")
            else:
                st.success("✅ This password has not been found in breaches!")

# Generate a secure password
st.subheader("🔑 Secure Password Generator")
length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
use_digits = st.checkbox("Include Numbers", value=True)
use_specials = st.checkbox("Include Special Characters", value=True)

if st.button("Generate Password"):
    new_password = generate_password(length, use_digits, use_specials)
    st.code(new_password, language="plaintext")

# Add spacing before footer
st.write("---")
st.caption("Built with ❤️ using Streamlit | Secure Passwords Matter! 🔒")  
