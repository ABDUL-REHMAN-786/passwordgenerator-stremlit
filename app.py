# import streamlit as st
# import re
# import random
# import string
# import hashlib
# import requests
# import time
# from cryptography.fernet import Fernet
# from datetime import datetime
# import pytz

# # Set Streamlit page configuration
# st.set_page_config(page_title="🔒 Password Manager", layout="centered")

# # AES-256 Encryption Key (Generate once and store securely)
# KEY = Fernet.generate_key()
# cipher = Fernet(KEY)

# # Initialize session state for password history if not exists
# if "password_history" not in st.session_state:
#     st.session_state.password_history = []

# # Function to check password strength
# def check_password_strength(pwd):
#     score = 0
#     feedback = []
#     if len(pwd) >= 8:
#         score += 1
#     else:
#         feedback.append("Increase password length to at least 8 characters.")
#     if re.search(r"[A-Z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one uppercase letter (A-Z).")
#     if re.search(r"[a-z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one lowercase letter (a-z).")
#     if re.search(r"\d", pwd):
#         score += 1
#     else:
#         feedback.append("Include at least one digit (0-9).")
#     if re.search(r"[!@#$%^&*]", pwd):
#         score += 1
#     else:
#         feedback.append("Use at least one special character (!@#$%^&*).")
#     if score == 5:
#         return "Strong", score, feedback
#     elif score >= 3:
#         return "Moderate", score, feedback
#     else:
#         return "Weak", score, feedback

# # Function to generate a strong random password
# def generate_password(length=12, use_digits=True, use_specials=True):
#     characters = string.ascii_letters
#     if use_digits:
#         characters += string.digits
#     if use_specials:
#         characters += "!@#$%^&*"
#     return ''.join(random.choice(characters) for _ in range(length))

# # Function to check if the password has been leaked (Have I Been Pwned API)
# def check_breach(password):
#     sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
#     first5, rest = sha1_hash[:5], sha1_hash[5:]
#     response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
#     return response.status_code == 200 and rest in response.text

# st.title("🔒 Password Manager")

# # Display Current Time and Temperature
# st.header("")
# karachi_tz = pytz.timezone("Asia/Karachi")
# current_time = datetime.now(karachi_tz).strftime("%I:%M %p, %d %B %Y")
# st.markdown(f"<div style='text-align: center; font-size: 24px;'><b>🕒 {current_time}</b></div>", unsafe_allow_html=True)

# try:
#     weather_response = requests.get("https://wttr.in/Karachi?format=%C+%t")
#     if weather_response.status_code == 200:
#         temperature = weather_response.text.split()[1]
#         if "°F" in temperature:
#             temp_celsius = round((float(temperature.replace("°F", "")) - 32) * 5/9, 1)
#             temperature = f"{temp_celsius}°C"
#         st.markdown(f"<div style='text-align: center; font-size: 24px;'><b>🌡️ Karachi Temperature: {temperature}</b></div>", unsafe_allow_html=True)
#     else:
#         st.markdown("<div style='text-align: center; font-size: 24px;'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)
# except:
#     st.markdown("<div style='text-align: center; font-size: 24px;'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)

# # Password Strength Checker
# st.header("Password Strength Meter")
# password = st.text_input("Enter Password:", type="password")
# if password:
#     with st.spinner("Analyzing password strength..."):
#         time.sleep(1.5)
#     strength, score, feedback = check_password_strength(password)
#     st.progress(score / 5)
#     st.write(f"**Strength:** {strength}")  # Display result in UI
#     if strength == "Strong":
#         st.success("✅ Strong Password! Well done!")
#         st.balloons()
#     elif strength == "Moderate":
#         st.warning("⚠️ Moderate Password! Consider improving it.")
#     else:
#         st.error("❌ Weak Password! Please improve your password security.")
#     if feedback:
#         st.write("🔹 Suggestions to Improve:")
#         for tip in feedback:
#             st.write(f"   - {tip}")
#     if st.button("Check Breach Status"):
#         with st.spinner("Checking for breaches..."):
#             time.sleep(1.5)
#             if check_breach(password):
#                 st.error("⚠️ This password has been leaked in data breaches. Please change it!")
#             else:
#                 st.success("✅ This password has not been found in breaches!")
#     st.session_state.password_history.append({"password": password, "strength": strength})

# # Password Generator
# st.header("Secure Password Generator")
# length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
# use_digits = st.checkbox("Include Numbers", value=True)
# use_specials = st.checkbox("Include Special Characters", value=True)
# if st.button("Generate Password"):
#     with st.spinner("Generating a secure password..."):
#         time.sleep(1.5)
#     new_password = generate_password(length, use_digits, use_specials)
#     st.code(new_password, language="plaintext")
#     st.balloons()
# st.write("Use a password manager to store your generated passwords securely.")

# # Password History Section
# st.header("📜 Password History")
# st.subheader("Stored Passwords")
# max_history = st.number_input("Number of Passwords to Show:", min_value=1, max_value=100, value=10)
# password_search = st.text_input("Search Password History:")
# if st.session_state.password_history:
#     filtered_history = [entry for entry in st.session_state.password_history if password_search in entry["password"]]
#     for idx, entry in enumerate(reversed(filtered_history[-max_history:])):
#         with st.expander(f"🔐 Password {idx + 1}"):
#             st.write(f"**Password:** `{entry['password']}`")
#             st.write(f"**Strength:** {entry['strength']}")
#     if st.button("Clear History"):
#         st.session_state.password_history = []
#         st.success("✅ Password history cleared!")
#         st.rerun()
# else:
#     st.info("No password history available.")

# # Footer
# st.write("---")
# st.caption("Developed by Abdul Rehman | Built with ❤️ using Streamlit | Secure Passwords Matter! 🔒")



































# import streamlit as st
# import re
# import random
# import string
# import hashlib
# import requests
# import time
# from cryptography.fernet import Fernet
# from datetime import datetime
# import pytz

# # Set Streamlit page configuration
# st.set_page_config(page_title="🔒 Password Manager", layout="centered")

# # AES-256 Encryption Key (Generate once and store securely)
# KEY = Fernet.generate_key()
# cipher = Fernet(KEY)

# # Initialize session state for password history if not exists
# if "password_history" not in st.session_state:
#     st.session_state.password_history = []

# # Function to check password strength
# def check_password_strength(pwd):
#     score = 0
#     feedback = []
#     if len(pwd) >= 8:
#         score += 1
#     else:
#         feedback.append("Increase password length to at least 8 characters.")
#     if re.search(r"[A-Z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one uppercase letter (A-Z).")
#     if re.search(r"[a-z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one lowercase letter (a-z).")
#     if re.search(r"\d", pwd):
#         score += 1
#     else:
#         feedback.append("Include at least one digit (0-9).")
#     if re.search(r"[!@#$%^&*]", pwd):
#         score += 1
#     else:
#         feedback.append("Use at least one special character (!@#$%^&*).")
#     if score == 5:
#         return "Strong", score, feedback
#     elif score >= 3:
#         return "Moderate", score, feedback
#     else:
#         return "Weak", score, feedback

# # Function to generate a strong random password
# def generate_password(length=12, use_digits=True, use_specials=True):
#     characters = string.ascii_letters
#     if use_digits:
#         characters += string.digits
#     if use_specials:
#         characters += "!@#$%^&*"
#     return ''.join(random.choice(characters) for _ in range(length))

# # Function to check if the password has been leaked (Have I Been Pwned API)
# def check_breach(password):
#     sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
#     first5, rest = sha1_hash[:5], sha1_hash[5:]
#     response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
#     return response.status_code == 200 and rest in response.text

# st.title("🔒 Password Manager")

# # Display Current Time and Temperature using OpenWeatherMap API
# st.header("")
# karachi_tz = pytz.timezone("Asia/Karachi")
# current_time = datetime.now(karachi_tz).strftime("%I:%M %p, %d %B %Y")
# st.markdown(f"<div style='text-align: center; font-size: 24px;'><b>🕒 {current_time}</b></div>", unsafe_allow_html=True)

# # API Key for OpenWeatherMap
# API_KEY = "ea815a44ac089b6f28d755bacec67f30"

# # Fetch Weather Data
# try:
#     weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=Karachi&appid={API_KEY}&units=metric"
#     weather_response = requests.get(weather_url)
#     if weather_response.status_code == 200:
#         weather_data = weather_response.json()
#         temperature = weather_data['main']['temp']
#         weather_condition = weather_data['weather'][0]['description']
#         st.markdown(f"<div style='text-align: center; font-size: 24px;'><b>🌡️ Karachi Temperature: {temperature}°C, {weather_condition.capitalize()}</b></div>", unsafe_allow_html=True)
#     else:
#         st.markdown("<div style='text-align: center; font-size: 24px;'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)
# except Exception as e:
#     st.markdown("<div style='text-align: center; font-size: 24px;'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)

# # Password Strength Checker
# st.header("Password Strength Meter")
# password = st.text_input("Enter Password:", type="password")
# if password:
#     with st.spinner("Analyzing password strength..."):
#         time.sleep(1.5)
#     strength, score, feedback = check_password_strength(password)
#     st.progress(score / 5)
#     st.write(f"**Strength:** {strength}")  # Display result in UI
#     if strength == "Strong":
#         st.success("✅ Strong Password! Well done!")
#         st.balloons()
#     elif strength == "Moderate":
#         st.warning("⚠️ Moderate Password! Consider improving it.")
#     else:
#         st.error("❌ Weak Password! Please improve your password security.")
#     if feedback:
#         st.write("🔹 Suggestions to Improve:")
#         for tip in feedback:
#             st.write(f"   - {tip}")
#     if st.button("Check Breach Status"):
#         with st.spinner("Checking for breaches..."):
#             time.sleep(1.5)
#             if check_breach(password):
#                 st.error("⚠️ This password has been leaked in data breaches. Please change it!")
#             else:
#                 st.success("✅ This password has not been found in breaches!")
#     st.session_state.password_history.append({"password": password, "strength": strength})

# # Password Generator
# st.header("Secure Password Generator")
# length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
# use_digits = st.checkbox("Include Numbers", value=True)
# use_specials = st.checkbox("Include Special Characters", value=True)
# if st.button("Generate Password"):
#     with st.spinner("Generating a secure password..."):
#         time.sleep(1.5)
#     new_password = generate_password(length, use_digits, use_specials)
#     st.code(new_password, language="plaintext")
#     st.balloons()
# st.write("Use a password manager to store your generated passwords securely.")

# # Password History Section
# st.header("📜 Password History")
# st.subheader("Stored Passwords")
# max_history = st.number_input("Number of Passwords to Show:", min_value=1, max_value=100, value=10)
# password_search = st.text_input("Search Password History:")
# if st.session_state.password_history:
#     filtered_history = [entry for entry in st.session_state.password_history if password_search in entry["password"]]
#     for idx, entry in enumerate(reversed(filtered_history[-max_history:])):
#         with st.expander(f"🔐 Password {idx + 1}"):
#             st.write(f"**Password:** `{entry['password']}`")
#             st.write(f"**Strength:** {entry['strength']}")
#     if st.button("Clear History"):
#         st.session_state.password_history = []
#         st.success("✅ Password history cleared!")
#         st.rerun()
# else:
#     st.info("No password history available.")

# # Footer
# st.write("---")
# st.caption("Developed by Abdul Rehman | Built with ❤️ using Streamlit | Secure Passwords Matter! 🔒")


























# import streamlit as st
# import re
# import random
# import string
# import hashlib
# import requests
# import time
# from cryptography.fernet import Fernet
# from datetime import datetime
# import pytz

# # Set Streamlit page configuration
# st.set_page_config(page_title="🔒 Password Manager", layout="centered")

# # AES-256 Encryption Key (Generate once and store securely)
# KEY = Fernet.generate_key()
# cipher = Fernet(KEY)

# # Initialize session state for password history if not exists
# if "password_history" not in st.session_state:
#     st.session_state.password_history = []

# # Function to check password strength
# def check_password_strength(pwd):
#     score = 0
#     feedback = []
#     if len(pwd) >= 8:
#         score += 1
#     else:
#         feedback.append("Increase password length to at least 8 characters.")
#     if re.search(r"[A-Z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one uppercase letter (A-Z).")
#     if re.search(r"[a-z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one lowercase letter (a-z).")
#     if re.search(r"\d", pwd):
#         score += 1
#     else:
#         feedback.append("Include at least one digit (0-9).")
#     if re.search(r"[!@#$%^&*]", pwd):
#         score += 1
#     else:
#         feedback.append("Use at least one special character (!@#$%^&*).")
#     if score == 5:
#         return "Strong", score, feedback
#     elif score >= 3:
#         return "Moderate", score, feedback
#     else:
#         return "Weak", score, feedback

# # Function to generate a strong random password
# def generate_password(length=12, use_digits=True, use_specials=True):
#     characters = string.ascii_letters
#     if use_digits:
#         characters += string.digits
#     if use_specials:
#         characters += "!@#$%^&*"
#     return ''.join(random.choice(characters) for _ in range(length))

# # Function to check if the password has been leaked (Have I Been Pwned API)
# def check_breach(password):
#     sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
#     first5, rest = sha1_hash[:5], sha1_hash[5:]
#     response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
#     return response.status_code == 200 and rest in response.text

# st.markdown("""
#     <style>
#         .center-text {
#             text-align: center;
#             font-size: 32px;
#             font-weight: bold;
#         }
#         .green-button {
#             background-color: #4CAF50; /* Green color */
#             color: white;
#             padding: 10px 20px;
#             font-size: 16px;
#             border-radius: 5px;
#             border: none;
#             cursor: pointer;
#             width: 200px;
#             margin: 0 auto;
#             display: block;
#         }
#         .green-button:hover {
#             background-color: #45a049; /* Darker green */
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Centered Title
# st.markdown('<div class="center-text">🔒 Password Manager</div>', unsafe_allow_html=True)

# # Display Current Time and Temperature using OpenWeatherMap API
# st.header("")
# karachi_tz = pytz.timezone("Asia/Karachi")
# current_time = datetime.now(karachi_tz).strftime("%I:%M %p, %d %B %Y")
# st.markdown(f"<div style='text-align: center; font-size: 24px;'><b>🕒 {current_time}</b></div>", unsafe_allow_html=True)

# # API Key for OpenWeatherMap
# API_KEY = "ea815a44ac089b6f28d755bacec67f30"

# # Fetch Weather Data
# try:
#     weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=Karachi&appid={API_KEY}&units=metric"
#     weather_response = requests.get(weather_url)
#     if weather_response.status_code == 200:
#         weather_data = weather_response.json()
#         temperature = weather_data['main']['temp']
#         weather_condition = weather_data['weather'][0]['description']
#         st.markdown(f"<div style='text-align: center; font-size: 24px;'><b>🌡️ Karachi Temperature: {temperature}°C, {weather_condition.capitalize()}</b></div>", unsafe_allow_html=True)
#     else:
#         st.markdown("<div style='text-align: center; font-size: 24px;'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)
# except Exception as e:
#     st.markdown("<div style='text-align: center; font-size: 24px;'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)

# # Password Strength Checker
# st.header("Password Strength Meter")
# password = st.text_input("Enter Password:", type="password")
# if password:
#     with st.spinner("Analyzing password strength..."):
#         time.sleep(1.5)
#     strength, score, feedback = check_password_strength(password)
#     st.progress(score / 5)
#     st.write(f"**Strength:** {strength}")  # Display result in UI
#     if strength == "Strong":
#         st.success("✅ Strong Password! Well done!")
#         st.balloons()
#     elif strength == "Moderate":
#         st.warning("⚠️ Moderate Password! Consider improving it.")
#     else:
#         st.error("❌ Weak Password! Please improve your password security.")
#     if feedback:
#         st.write("🔹 Suggestions to Improve:")
#         for tip in feedback:
#             st.write(f"   - {tip}")
#     if st.button("Check Breach Status"):
#         with st.spinner("Checking for breaches..."):
#             time.sleep(1.5)
#             if check_breach(password):
#                 st.error("⚠️ This password has been leaked in data breaches. Please change it!")
#             else:
#                 st.success("✅ This password has not been found in breaches!")
#     st.session_state.password_history.append({"password": password, "strength": strength})

# # Password Generator
# st.header("Secure Password Generator")
# length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
# use_digits = st.checkbox("Include Numbers", value=True)
# use_specials = st.checkbox("Include Special Characters", value=True)
# if st.button("Generate Password"):
#     with st.spinner("Generating a secure password..."):
#         time.sleep(1.5)
#     new_password = generate_password(length, use_digits, use_specials)
#     st.code(new_password, language="plaintext")
#     st.balloons()
# st.write("Use a password manager to store your generated passwords securely.")

# # Password History Section
# st.header("📜 Password History")
# st.subheader("Stored Passwords")
# max_history = st.number_input("Number of Passwords to Show:", min_value=1, max_value=100, value=10)
# password_search = st.text_input("Search Password History:")
# if st.session_state.password_history:
#     filtered_history = [entry for entry in st.session_state.password_history if password_search in entry["password"]]
#     for idx, entry in enumerate(reversed(filtered_history[-max_history:])):
#         with st.expander(f"🔐 Password {idx + 1}"):
#             st.write(f"**Password:** `{entry['password']}`")
#             st.write(f"**Strength:** {entry['strength']}")
#     if st.button("Clear History"):
#         st.session_state.password_history = []
#         st.success("✅ Password history cleared!")
#         st.rerun()
# else:
#     st.info("No password history available.")

# # Footer
# st.write("---")
# st.caption("Developed by Abdul Rehman | Built with ❤️ using Streamlit | Secure Passwords Matter! 🔒")














# import streamlit as st
# import re
# import random
# import string
# import hashlib
# import requests
# import time
# from cryptography.fernet import Fernet
# from datetime import datetime
# import pytz

# # Set Streamlit page configuration
# st.set_page_config(page_title="🔒 Password Manager", layout="centered")

# # AES-256 Encryption Key (Generate once and store securely)
# KEY = Fernet.generate_key()
# cipher = Fernet(KEY)

# # Initialize session state for password history if not exists
# if "password_history" not in st.session_state:
#     st.session_state.password_history = []

# # Function to check password strength
# def check_password_strength(pwd):
#     score = 0
#     feedback = []
#     if len(pwd) >= 8:
#         score += 1
#     else:
#         feedback.append("Increase password length to at least 8 characters.")
#     if re.search(r"[A-Z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one uppercase letter (A-Z).")
#     if re.search(r"[a-z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one lowercase letter (a-z).")
#     if re.search(r"\d", pwd):
#         score += 1
#     else:
#         feedback.append("Include at least one digit (0-9).")
#     if re.search(r"[!@#$%^&*]", pwd):
#         score += 1
#     else:
#         feedback.append("Use at least one special character (!@#$%^&*).")
#     if score == 5:
#         return "Strong", score, feedback
#     elif score >= 3:
#         return "Moderate", score, feedback
#     else:
#         return "Weak", score, feedback

# # Function to generate a strong random password
# def generate_password(length=12, use_digits=True, use_specials=True):
#     characters = string.ascii_letters
#     if use_digits:
#         characters += string.digits
#     if use_specials:
#         characters += "!@#$%^&*"
#     return ''.join(random.choice(characters) for _ in range(length))

# # Function to check if the password has been leaked (Have I Been Pwned API)
# def check_breach(password):
#     sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
#     first5, rest = sha1_hash[:5], sha1_hash[5:]
#     response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
#     return response.status_code == 200 and rest in response.text

# # Inject custom CSS for stylish UI
# st.markdown("""
#     <style>
#         /* Style for centering all text */
#         .center-text {
#             text-align: center;
#             font-size: 32px;
#             font-weight: bold;
#             color: #4CAF50; /* Green color */
#         }

#         /* Button style */
#         .green-button {
#             background-color: #4CAF50; /* Green color */
#             color: white;
#             padding: 12px 24px;
#             font-size: 16px;
#             border-radius: 8px;
#             border: none;
#             cursor: pointer;
#             width: 250px;
#             margin: 10px auto;
#             display: block;
#             text-align: center;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             transition: all 0.3s ease;
#         }

#         .green-button:hover {
#             background-color: #45a049; /* Darker green */
#             transform: translateY(-2px);
#         }

#         .green-button:active {
#             background-color: #388e3c; /* Even darker green */
#             transform: translateY(2px);
#         }

#         /* Style for text input */
#         .stTextInput input {
#             text-align: center;
#             font-size: 18px;
#             padding: 12px;
#             border-radius: 8px;
#             border: 2px solid #ddd;
#             width: 100%;
#         }

#         /* Centering title and headers */
#         h1, h2, h3 {
#             text-align: center;
#             color: #333;
#         }

#         /* Footer style */
#         .footer {
#             text-align: center;
#             color: #777;
#             font-size: 14px;
#             margin-top: 40px;
#         }

#         /* Progress bar color */
#         .stProgress>div>div {
#             background-color: #4CAF50; /* Green progress */
#         }

#         /* Style for code blocks */
#         pre {
#             background-color: #f7f7f7;
#             padding: 15px;
#             border-radius: 8px;
#             border: 1px solid #ddd;
#             font-size: 16px;
#             color: #333;
#         }

#         /* Background color */
#         body {
#             background-color: #f1f1f1;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Centered Title
# st.markdown('<div class="center-text">🔒 Password Manager</div>', unsafe_allow_html=True)

# # Display Current Time and Temperature using OpenWeatherMap API
# st.header("")
# karachi_tz = pytz.timezone("Asia/Karachi")
# current_time = datetime.now(karachi_tz).strftime("%I:%M %p, %d %B %Y")
# st.markdown(f"<div style='text-align: center; font-size: 24px;'><b>🕒 {current_time}</b></div>", unsafe_allow_html=True)

# # API Key for OpenWeatherMap
# API_KEY = "ea815a44ac089b6f28d755bacec67f30"

# # Fetch Weather Data
# try:
#     weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=Karachi&appid={API_KEY}&units=metric"
#     weather_response = requests.get(weather_url)
#     if weather_response.status_code == 200:
#         weather_data = weather_response.json()
#         temperature = weather_data['main']['temp']
#         weather_condition = weather_data['weather'][0]['description']
#         st.markdown(f"<div style='text-align: center; font-size: 24px;'><b>🌡️ Karachi Temperature: {temperature}°C, {weather_condition.capitalize()}</b></div>", unsafe_allow_html=True)
#     else:
#         st.markdown("<div style='text-align: center; font-size: 24px;'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)
# except Exception as e:
#     st.markdown("<div style='text-align: center; font-size: 24px;'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)

# # Password Strength Checker
# st.header("Password Strength Meter")
# password = st.text_input("Enter Password:", type="password")
# if password:
#     with st.spinner("Analyzing password strength..."):
#         time.sleep(1.5)
#     strength, score, feedback = check_password_strength(password)
#     st.progress(score / 5)
#     st.write(f"**Strength:** {strength}")  # Display result in UI
#     if strength == "Strong":
#         st.success("✅ Strong Password! Well done!")
#         st.balloons()
#     elif strength == "Moderate":
#         st.warning("⚠️ Moderate Password! Consider improving it.")
#     else:
#         st.error("❌ Weak Password! Please improve your password security.")
#     if feedback:
#         st.write("🔹 Suggestions to Improve:")
#         for tip in feedback:
#             st.write(f"   - {tip}")
#     if st.button("Check Breach Status", key="breach_button", help="Check if your password has been leaked"):
#         with st.spinner("Checking for breaches..."):
#             time.sleep(1.5)
#             if check_breach(password):
#                 st.error("⚠️ This password has been leaked in data breaches. Please change it!")
#             else:
#                 st.success("✅ This password has not been found in breaches!")
#     st.session_state.password_history.append({"password": password, "strength": strength})

# # Password Generator
# st.header("Secure Password Generator")
# length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
# use_digits = st.checkbox("Include Numbers", value=True)
# use_specials = st.checkbox("Include Special Characters", value=True)
# if st.button("Generate Password", key="generate_button"):
#     with st.spinner("Generating a secure password..."):
#         time.sleep(1.5)
#     new_password = generate_password(length, use_digits, use_specials)
#     st.code(new_password, language="plaintext")
#     st.balloons()
# st.write("Use a password manager to store your generated passwords securely.")

# # Password History Section
# st.header("📜 Password History")
# st.subheader("Stored Passwords")
# max_history = st.number_input("Number of Passwords to Show:", min_value=1, max_value=100, value=10)
# password_search = st.text_input("Search Password History:")
# if st.session_state.password_history:
#     filtered_history = [entry for entry in st.session_state.password_history if password_search in entry["password"]]
#     for idx, entry in enumerate(reversed(filtered_history[-max_history:])):
#         with st.expander(f"🔐 Password {idx + 1}"):
#             st.write(f"**Password:** `{entry['password']}`")
#             st.write(f"**Strength:** {entry['strength']}")
#     if st.button("Clear History", key="clear_history", help="Clear all stored passwords"):
#         st.session_state.password_history = []
#         st.success("✅ Password history cleared!")
#         st.rerun()
# else:
#     st.info("No password history available.")

# # Footer
# st.markdown('<div class="footer">Developed by Abdul Rehman | Built with ❤️ using Streamlit | Secure Passwords Matter! 🔒</div>', unsafe_allow_html=True)


# import streamlit as st
# import re
# import random
# import string
# import hashlib
# import requests
# import time
# from cryptography.fernet import Fernet
# from datetime import datetime
# import pytz

# # Set Streamlit page configuration
# st.set_page_config(page_title="🔒 Password Manager", layout="centered")

# # AES-256 Encryption Key (Generate once and store securely)
# KEY = Fernet.generate_key()
# cipher = Fernet(KEY)

# # Initialize session state for password history if not exists
# if "password_history" not in st.session_state:
#     st.session_state.password_history = []

# # Function to check password strength
# def check_password_strength(pwd):
#     score = 0
#     feedback = []
#     if len(pwd) >= 8:
#         score += 1
#     else:
#         feedback.append("Increase password length to at least 8 characters.")
#     if re.search(r"[A-Z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one uppercase letter (A-Z).")
#     if re.search(r"[a-z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one lowercase letter (a-z).")
#     if re.search(r"\d", pwd):
#         score += 1
#     else:
#         feedback.append("Include at least one digit (0-9).")
#     if re.search(r"[!@#$%^&*]", pwd):
#         score += 1
#     else:
#         feedback.append("Use at least one special character (!@#$%^&*).")
#     if score == 5:
#         return "Strong", score, feedback
#     elif score >= 3:
#         return "Moderate", score, feedback
#     else:
#         return "Weak", score, feedback

# # Function to generate a strong random password
# def generate_password(length=12, use_digits=True, use_specials=True):
#     characters = string.ascii_letters
#     if use_digits:
#         characters += string.digits
#     if use_specials:
#         characters += "!@#$%^&*"
#     return ''.join(random.choice(characters) for _ in range(length))

# # Function to check if the password has been leaked (Have I Been Pwned API)
# def check_breach(password):
#     sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
#     first5, rest = sha1_hash[:5], sha1_hash[5:]
#     response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
#     return response.status_code == 200 and rest in response.text

# # Inject custom CSS for stylish UI
# st.markdown("""
#     <style>
#         /* Style for centering all text */
#         .center-text {
#             text-align: center;
#             font-size: 32px;
#             font-weight: bold;
#             color: #4CAF50; /* Green color */
#         }

#         /* Button style */
#         .green-button {
#             background-color: #4CAF50; /* Green color */
#             color: white;
#             padding: 12px 24px;
#             font-size: 16px;
#             border-radius: 8px;
#             border: none;
#             cursor: pointer;
#             width: 250px;
#             margin: 10px auto;
#             display: block;
#             text-align: center;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             transition: all 0.3s ease;
#         }

#         .green-button:hover {
#             background-color: #45a049; /* Darker green */
#             transform: translateY(-2px);
#         }

#         .green-button:active {
#             background-color: #388e3c; /* Even darker green */
#             transform: translateY(2px);
#         }

#         /* Style for text input */
#         .stTextInput input {
#             text-align: center;
#             font-size: 18px;
#             padding: 12px;
#             border-radius: 8px;
#             border: 2px solid #ddd;
#             width: 100%;
#         }

#         /* Centering title and headers */
#         h1, h2, h3 {
#             text-align: center;
#             color: #333;
#         }

#         /* Styling for green section headers */
#         .section-header {
#             color: #4CAF50;
#             font-weight: bold;
#             text-align: center;
#         }

#         /* Red color for the temperature section */
#         .temp-section {
#             color: red;
#             font-weight: bold;
#             text-align: center;
#         }

#         /* Red color for the time section */
#         .time-section {
#             color: red;
#             font-weight: bold;
#             text-align: center;
#             font-size: 32px;
#         }

#         /* Footer style */
#         .footer {
#             text-align: center;
#             color: #777;
#             font-size: 14px;
#             margin-top: 40px;
#         }

#         /* Progress bar color */
#         .stProgress>div>div {
#             background-color: #4CAF50; /* Green progress */
#         }

#         /* Style for code blocks */
#         pre {
#             background-color: #f7f7f7;
#             padding: 15px;
#             border-radius: 8px;
#             border: 1px solid #ddd;
#             font-size: 16px;
#             color: #333;
#         }

#         /* Background color */
#         body {
#             background-color: #f1f1f1;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Centered Title
# st.markdown('<div class="center-text">🔒 Password Manager</div>', unsafe_allow_html=True)

# # Display Current Time and Temperature using OpenWeatherMap API
# st.header("")
# karachi_tz = pytz.timezone("Asia/Karachi")
# current_time = datetime.now(karachi_tz).strftime("%I:%M %p, %d %B %Y")
# st.markdown(f"<div class='time-section'><b>🕒 {current_time}</b></div>", unsafe_allow_html=True)

# # API Key for OpenWeatherMap
# API_KEY = "ea815a44ac089b6f28d755bacec67f30"

# # Fetch Weather Data
# try:
#     weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=Karachi&appid={API_KEY}&units=metric"
#     weather_response = requests.get(weather_url)
#     if weather_response.status_code == 200:
#         weather_data = weather_response.json()
#         temperature = weather_data['main']['temp']
#         weather_condition = weather_data['weather'][0]['description']
#         st.markdown(f"<div class='temp-section'><b>🌡️ Karachi Temperature: {temperature}°C, {weather_condition.capitalize()}</b></div>", unsafe_allow_html=True)
#     else:
#         st.markdown("<div class='temp-section'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)
# except Exception as e:
#     st.markdown("<div class='temp-section'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)

# # Password Strength Checker
# st.markdown('<div class="section-header">Password Strength Meter</div>', unsafe_allow_html=True)
# password = st.text_input("Enter Password:", type="password")
# if password:
#     with st.spinner("Analyzing password strength..."):
#         time.sleep(1.5)
#     strength, score, feedback = check_password_strength(password)
#     st.progress(score / 5)
#     st.write(f"**Strength:** {strength}")  # Display result in UI
#     if strength == "Strong":
#         st.success("✅ Strong Password! Well done!")
#         st.balloons()
#     elif strength == "Moderate":
#         st.warning("⚠️ Moderate Password! Consider improving it.")
#     else:
#         st.error("❌ Weak Password! Please improve your password security.")
#     if feedback:
#         st.write("🔹 Suggestions to Improve:")
#         for tip in feedback:
#             st.write(f"   - {tip}")
#     if st.button("Check Breach Status", key="breach_button", help="Check if your password has been leaked"):
#         with st.spinner("Checking for breaches..."):
#             time.sleep(1.5)
#             if check_breach(password):
#                 st.error("⚠️ This password has been leaked in data breaches. Please change it!")
#             else:
#                 st.success("✅ This password has not been found in breaches!")
#     st.session_state.password_history.append({"password": password, "strength": strength})

# # Password Generator
# st.markdown('<div class="section-header">Secure Password Generator</div>', unsafe_allow_html=True)
# length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
# use_digits = st.checkbox("Include Numbers", value=True)
# use_specials = st.checkbox("Include Special Characters", value=True)
# if st.button("Generate Password", key="generate_button"):
#     with st.spinner("Generating a secure password..."):
#         time.sleep(1.5)
#     new_password = generate_password(length, use_digits, use_specials)
#     st.code(new_password, language="plaintext")
#     st.balloons()
# st.write("Use a password manager to store your generated passwords securely.")

# # Password History Section
# st.markdown('<div class="section-header">📜 Password History</div>', unsafe_allow_html=True)
# st.subheader("Stored Passwords")
# max_history = st.number_input("Number of Passwords to Show:", min_value=1, max_value=100, value=10)
# password_search = st.text_input("Search Password History:")
# if st.session_state.password_history:
#     filtered_history = [entry for entry in st.session_state.password_history if password_search in entry["password"]]
#     for idx, entry in enumerate(reversed(filtered_history[-max_history:])):
#         with st.expander(f"🔐 Password {idx + 1}"):
#             st.write(f"**Password:** `{entry['password']}`")
#             st.write(f"**Strength:** {entry['strength']}")
#     if st.button("Clear History", key="clear_history", help="Clear all stored passwords"):
#         st.session_state.password_history = []
#         st.success("✅ Password history cleared!")
#         st.rerun()
# else:
#     st.info("No password history available.")

# # Footer
# st.markdown('<div class="footer">Developed by Abdul Rehman | Built with ❤️ using Streamlit | Secure Passwords Matter! 🔒</div>', unsafe_allow_html=True)



# import streamlit as st
# import re
# import random
# import string
# import hashlib
# import requests
# import time
# from cryptography.fernet import Fernet
# from datetime import datetime
# import pytz

# # Set Streamlit page configuration
# st.set_page_config(page_title="🔒 Password Manager", layout="centered")

# # AES-256 Encryption Key (Generate once and store securely)
# KEY = Fernet.generate_key()
# cipher = Fernet(KEY)

# # Initialize session state for password history if not exists
# if "password_history" not in st.session_state:
#     st.session_state.password_history = []

# # Function to check password strength
# def check_password_strength(pwd):
#     score = 0
#     feedback = []
#     if len(pwd) >= 8:
#         score += 1
#     else:
#         feedback.append("Increase password length to at least 8 characters.")
#     if re.search(r"[A-Z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one uppercase letter (A-Z).")
#     if re.search(r"[a-z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one lowercase letter (a-z).")
#     if re.search(r"\d", pwd):
#         score += 1
#     else:
#         feedback.append("Include at least one digit (0-9).")
#     if re.search(r"[!@#$%^&*]", pwd):
#         score += 1
#     else:
#         feedback.append("Use at least one special character (!@#$%^&*).")
#     if score == 5:
#         return "Strong", score, feedback
#     elif score >= 3:
#         return "Moderate", score, feedback
#     else:
#         return "Weak", score, feedback

# # Function to generate a strong random password
# def generate_password(length=12, use_digits=True, use_specials=True):
#     characters = string.ascii_letters
#     if use_digits:
#         characters += string.digits
#     if use_specials:
#         characters += "!@#$%^&*"
#     return ''.join(random.choice(characters) for _ in range(length))

# # Function to check if the password has been leaked (Have I Been Pwned API)
# def check_breach(password):
#     sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
#     first5, rest = sha1_hash[:5], sha1_hash[5:]
#     response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
#     return response.status_code == 200 and rest in response.text

# # Inject custom CSS for stylish UI
# st.markdown("""
#     <style>
#         /* Style for centering all text */
#         .center-text {
#             text-align: center;
#             font-size: 32px;
#             font-weight: bold;
#             color: #4CAF50; /* Green color */
#         }

#         /* Button style */
#         .red-button {
#             background-color: #FF5733; /* Red color */
#             color: white;
#             padding: 12px 24px;
#             font-size: 16px;
#             border-radius: 8px;
#             border: none;
#             cursor: pointer;
#             width: 250px;
#             margin: 10px auto;
#             display: block;
#             text-align: center;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             transition: all 0.3s ease;
#         }

#         .red-button:hover {
#             background-color: #e04e1b; /* Darker red */
#             transform: translateY(-2px);
#         }

#         .red-button:active {
#             background-color: #b64014; /* Even darker red */
#             transform: translateY(2px);
#         }

#         /* Style for text input */
#         .stTextInput input {
#             text-align: center;
#             font-size: 18px;
#             padding: 12px;
#             border-radius: 8px;
#             border: 2px solid #ddd;
#             width: 100%;
#         }

#         /* Centering title and headers */
#         h1, h2, h3 {
#             text-align: center;
#             color: #333;
#         }

#         /* Styling for green section headers */
#         .section-header {
#             color: #4CAF50;
#             font-weight: bold;
#             text-align: center;
#         }

#         /* Red color for the temperature section */
#         .temp-section {
#             color: red;
#             font-weight: bold;
#             text-align: center;
#         }

#         /* Red color for the time section */
#         .time-section {
#             color: red;
#             font-weight: bold;
#             text-align: center;
#             font-size: 32px;
#         }

#         /* Footer style */
#         .footer {
#             text-align: center;
#             color: #777;
#             font-size: 14px;
#             margin-top: 40px;
#         }

#         /* Progress bar color */
#         .stProgress>div>div {
#             background-color: #4CAF50; /* Green progress */
#         }

#         /* Style for code blocks */
#         pre {
#             background-color: #f7f7f7;
#             padding: 15px;
#             border-radius: 8px;
#             border: 1px solid #ddd;
#             font-size: 16px;
#             color: #333;
#         }

#         /* Background color */
#         body {
#             background-color: #f1f1f1;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Centered Title
# st.markdown('<div class="center-text">🔒 Password Manager</div>', unsafe_allow_html=True)

# # Display Current Time and Temperature using OpenWeatherMap API
# st.header("")
# karachi_tz = pytz.timezone("Asia/Karachi")
# current_time = datetime.now(karachi_tz).strftime("%I:%M %p, %d %B %Y")
# st.markdown(f"<div class='time-section'><b>🕒 {current_time}</b></div>", unsafe_allow_html=True)

# # API Key for OpenWeatherMap
# API_KEY = "ea815a44ac089b6f28d755bacec67f30"

# # Fetch Weather Data
# try:
#     weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=Karachi&appid={API_KEY}&units=metric"
#     weather_response = requests.get(weather_url)
#     if weather_response.status_code == 200:
#         weather_data = weather_response.json()
#         temperature = weather_data['main']['temp']
#         weather_condition = weather_data['weather'][0]['description']
#         st.markdown(f"<div class='temp-section'><b>🌡️ Karachi Temperature: {temperature}°C, {weather_condition.capitalize()}</b></div>", unsafe_allow_html=True)
#     else:
#         st.markdown("<div class='temp-section'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)
# except Exception as e:
#     st.markdown("<div class='temp-section'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)

# # Password Strength Checker
# st.markdown('<div class="section-header">Password Strength Meter</div>', unsafe_allow_html=True)
# password = st.text_input("Enter Password:", type="password")
# if password:
#     with st.spinner("Analyzing password strength..."):
#         time.sleep(1.5)
#     strength, score, feedback = check_password_strength(password)
#     st.progress(score / 5)
#     st.write(f"**Strength:** {strength}")  # Display result in UI
#     if strength == "Strong":
#         st.success("✅ Strong Password! Well done!")
#         st.balloons()
#     elif strength == "Moderate":
#         st.warning("⚠️ Moderate Password! Consider improving it.")
#     else:
#         st.error("❌ Weak Password! Please improve your password security.")
#     if feedback:
#         st.write("🔹 Suggestions to Improve:")
#         for tip in feedback:
#             st.write(f"   - {tip}")
#     if st.button("Check Breach Status", key="breach_button", help="Check if your password has been leaked"):
#         with st.spinner("Checking for breaches..."):
#             time.sleep(1.5)
#             if check_breach(password):
#                 st.error("⚠️ This password has been leaked in data breaches. Please change it!")
#             else:
#                 st.success("✅ This password has not been found in breaches!")
#     st.session_state.password_history.append({"password": password, "strength": strength})

# # Password Generator
# st.markdown('<div class="section-header">Secure Password Generator</div>', unsafe_allow_html=True)
# length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
# use_digits = st.checkbox("Include Numbers", value=True)
# use_specials = st.checkbox("Include Special Characters", value=True)
# if st.button("Generate Password", key="generate_button"):
#     with st.spinner("Generating a secure password..."):
#         time.sleep(1.5)
#     new_password = generate_password(length, use_digits, use_specials)
#     st.code(new_password, language="plaintext")
#     st.balloons()
# st.write("Use a password manager to store your generated passwords securely.")

# # Password History Section
# st.markdown('<div class="section-header">📜 Password History</div>', unsafe_allow_html=True)
# st.subheader("Stored Passwords")
# max_history = st.number_input("Number of Passwords to Show:", min_value=1, max_value=100, value=10)
# password_search = st.text_input("Search Password History:")
# if st.session_state.password_history:
#     filtered_history = [entry for entry in st.session_state.password_history if password_search in entry["password"]]
#     for idx, entry in enumerate(reversed(filtered_history[-max_history:])):
#         with st.expander(f"🔐 Password {idx + 1}"):
#             st.write(f"**Password:** `{entry['password']}`")
#             st.write(f"**Strength:** {entry['strength']}")
#     if st.button("Clear History", key="clear_history", help="Clear all stored passwords"):
#         st.session_state.password_history = []
#         st.success("✅ Password history cleared!")
#         st.rerun()
# else:
#     st.info("No password history available.")

# # Footer
# st.markdown('<div class="footer">Developed by Abdul Rehman | Built with ❤️ using Streamlit | Secure Passwords Matter! 🔒</div>', unsafe_allow_html=True)





# import streamlit as st
# import re
# import random
# import string
# import hashlib
# import requests
# import time
# from cryptography.fernet import Fernet
# from datetime import datetime
# import pytz

# # Set Streamlit page configuration
# st.set_page_config(page_title="🔒 Password Manager", layout="centered")

# # AES-256 Encryption Key (Generate once and store securely)
# KEY = Fernet.generate_key()
# cipher = Fernet(KEY)

# # Initialize session state for password history if not exists
# if "password_history" not in st.session_state:
#     st.session_state.password_history = []

# # Function to check password strength
# def check_password_strength(pwd):
#     score = 0
#     feedback = []
#     if len(pwd) >= 8:
#         score += 1
#     else:
#         feedback.append("Increase password length to at least 8 characters.")
#     if re.search(r"[A-Z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one uppercase letter (A-Z).")
#     if re.search(r"[a-z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one lowercase letter (a-z).")
#     if re.search(r"\d", pwd):
#         score += 1
#     else:
#         feedback.append("Include at least one digit (0-9).")
#     if re.search(r"[!@#$%^&*]", pwd):
#         score += 1
#     else:
#         feedback.append("Use at least one special character (!@#$%^&*).")
#     if score == 5:
#         return "Strong", score, feedback
#     elif score >= 3:
#         return "Moderate", score, feedback
#     else:
#         return "Weak", score, feedback

# # Function to generate a strong random password
# def generate_password(length=12, use_digits=True, use_specials=True):
#     characters = string.ascii_letters
#     if use_digits:
#         characters += string.digits
#     if use_specials:
#         characters += "!@#$%^&*"
#     return ''.join(random.choice(characters) for _ in range(length))

# # Function to check if the password has been leaked (Have I Been Pwned API)
# def check_breach(password):
#     sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
#     first5, rest = sha1_hash[:5], sha1_hash[5:]
#     response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
#     return response.status_code == 200 and rest in response.text

# # Inject custom CSS for stylish UI
# st.markdown("""
#     <style>
#         /* Style for centering all text */
#         .center-text {
#             text-align: center;
#             font-size: 32px;
#             font-weight: bold;
#             color: #4CAF50; /* Green color */
#         }

#         /* Button style */
#         .red-button {
#             background-color: #FF5733; /* Red color */
#             color: white;
#             padding: 12px 24px;
#             font-size: 16px;
#             border-radius: 8px;
#             border: none;
#             cursor: pointer;
#             width: 250px;
#             margin: 10px auto;
#             display: block;
#             text-align: center;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             transition: all 0.3s ease;
#         }

#         .red-button:hover {
#             background-color: #e04e1b; /* Darker red */
#             transform: translateY(-2px);
#         }

#         .red-button:active {
#             background-color: #b64014; /* Even darker red */
#             transform: translateY(2px);
#         }

#         /* Style for text input */
#         .stTextInput input {
#             text-align: center;
#             font-size: 18px;
#             padding: 12px;
#             border-radius: 8px;
#             border: 2px solid #ddd;
#             width: 100%;
#         }

#         /* Centering title and headers */
#         h1, h2, h3 {
#             text-align: center;
#             color: #333;
#         }

#         /* Styling for green section headers */
#         .section-header {
#             color: #4CAF50;
#             font-weight: bold;
#             text-align: center;
#             font-size: 28px;  /* Larger size */
#         }

#         .section-header-password-strength {
#             font-size: 34px;  /* Even larger size for Password Strength Meter */
#         }

#         /* Red color for the temperature section */
#         .temp-section {
#             color: red;
#             font-weight: bold;
#             text-align: center;
#         }

#         /* Red color for the time section */
#         .time-section {
#             color: red;
#             font-weight: bold;
#             text-align: center;
#             font-size: 32px;
#         }

#         /* Footer style */
#         .footer {
#             text-align: center;
#             color: #777;
#             font-size: 14px;
#             margin-top: 40px;
#         }

#         /* Progress bar color */
#         .stProgress>div>div {
#             background-color: #4CAF50; /* Green progress */
#         }

#         /* Style for code blocks */
#         pre {
#             background-color: #f7f7f7;
#             padding: 15px;
#             border-radius: 8px;
#             border: 1px solid #ddd;
#             font-size: 16px;
#             color: #333;
#         }

#         /* Background color */
#         body {
#             background-color: #f1f1f1;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Centered Title
# st.markdown('<div class="center-text">🔒 Password Manager</div>', unsafe_allow_html=True)

# # Display Current Time and Temperature using OpenWeatherMap API
# st.header("")
# karachi_tz = pytz.timezone("Asia/Karachi")
# current_time = datetime.now(karachi_tz).strftime("%I:%M %p, %d %B %Y")
# st.markdown(f"<div class='time-section'><b>🕒 {current_time}</b></div>", unsafe_allow_html=True)

# # API Key for OpenWeatherMap
# API_KEY = "ea815a44ac089b6f28d755bacec67f30"

# # Fetch Weather Data
# try:
#     weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=Karachi&appid={API_KEY}&units=metric"
#     weather_response = requests.get(weather_url)
#     if weather_response.status_code == 200:
#         weather_data = weather_response.json()
#         temperature = weather_data['main']['temp']
#         weather_condition = weather_data['weather'][0]['description']
#         st.markdown(f"<div class='temp-section'><b>🌡️ Karachi Temperature: {temperature}°C, {weather_condition.capitalize()}</b></div>", unsafe_allow_html=True)
#     else:
#         st.markdown("<div class='temp-section'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)
# except Exception as e:
#     st.markdown("<div class='temp-section'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)

# # Password Strength Checker
# st.markdown('<div class="section-header section-header-password-strength">Password Strength Meter</div>', unsafe_allow_html=True)
# password = st.text_input("Enter Password:", type="password")
# if password:
#     with st.spinner("Analyzing password strength..."):
#         time.sleep(1.5)
#     strength, score, feedback = check_password_strength(password)
#     st.progress(score / 5)
#     st.write(f"**Strength:** {strength}")  # Display result in UI
#     if strength == "Strong":
#         st.success("✅ Strong Password! Well done!")
#         st.balloons()
#     elif strength == "Moderate":
#         st.warning("⚠️ Moderate Password! Consider improving it.")
#     else:
#         st.error("❌ Weak Password! Please improve your password security.")
#     if feedback:
#         st.write("🔹 Suggestions to Improve:")
#         for tip in feedback:
#             st.write(f"   - {tip}")
#     if st.button("Check Breach Status", key="breach_button", help="Check if your password has been leaked"):
#         with st.spinner("Checking for breaches..."):
#             time.sleep(1.5)
#             if check_breach(password):
#                 st.error("⚠️ This password has been leaked in data breaches. Please change it!")
#             else:
#                 st.success("✅ This password has not been found in breaches!")
#     st.session_state.password_history.append({"password": password, "strength": strength})

# # Password Generator
# st.markdown('<div class="section-header">Secure Password Generator</div>', unsafe_allow_html=True)
# length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
# use_digits = st.checkbox("Include Numbers", value=True)
# use_specials = st.checkbox("Include Special Characters", value=True)
# if st.button("Generate Password", key="generate_button"):
#     with st.spinner("Generating a secure password..."):
#         time.sleep(1.5)
#     new_password = generate_password(length, use_digits, use_specials)
#     st.code(new_password, language="plaintext")
#     st.balloons()
# st.write("Use a password manager to store your generated passwords securely.")

# # Password History Section
# st.markdown('<div class="section-header">📜 Password History</div>', unsafe_allow_html=True)
# st.subheader("Stored Passwords")
# max_history = st.number_input("Number of Passwords to Show:", min_value=1, max_value=100, value=10)
# password_search = st.text_input("Search Password History:")
# if st.session_state.password_history:
#     filtered_history = [entry for entry in st.session_state.password_history if password_search in entry["password"]]
#     for idx, entry in enumerate(reversed(filtered_history[-max_history:])):
#         with st.expander(f"🔐 Password {idx + 1}"):
#             st.write(f"**Password:** `{entry['password']}`")
#             st.write(f"**Strength:** {entry['strength']}")
#     if st.button("Clear History", key="clear_history", help="Clear all stored passwords"):
#         st.session_state.password_history = []
#         st.success("✅ Password history cleared!")
#         st.rerun()
# else:
#     st.info("No password history available.")

# # Footer
# st.markdown('<div class="footer">Developed by Abdul Rehman | Built with ❤️ using Streamlit | Secure Passwords Matter! 🔒</div>', unsafe_allow_html=True)





# import streamlit as st
# import re
# import random
# import string
# import hashlib
# import requests
# import time
# from cryptography.fernet import Fernet
# from datetime import datetime
# import pytz

# # Set Streamlit page configuration
# st.set_page_config(page_title="🔒 Password Manager", layout="centered")

# # AES-256 Encryption Key (Generate once and store securely)
# KEY = Fernet.generate_key()
# cipher = Fernet(KEY)

# # Initialize session state for password history if not exists
# if "password_history" not in st.session_state:
#     st.session_state.password_history = []

# # Function to check password strength
# def check_password_strength(pwd):
#     score = 0
#     feedback = []
#     if len(pwd) >= 8:
#         score += 1
#     else:
#         feedback.append("Increase password length to at least 8 characters.")
#     if re.search(r"[A-Z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one uppercase letter (A-Z).")
#     if re.search(r"[a-z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one lowercase letter (a-z).")
#     if re.search(r"\d", pwd):
#         score += 1
#     else:
#         feedback.append("Include at least one digit (0-9).")
#     if re.search(r"[!@#$%^&*]", pwd):
#         score += 1
#     else:
#         feedback.append("Use at least one special character (!@#$%^&*).")
#     if score == 5:
#         return "Strong", score, feedback
#     elif score >= 3:
#         return "Moderate", score, feedback
#     else:
#         return "Weak", score, feedback

# # Function to generate a strong random password
# def generate_password(length=12, use_digits=True, use_specials=True):
#     characters = string.ascii_letters
#     if use_digits:
#         characters += string.digits
#     if use_specials:
#         characters += "!@#$%^&*"
#     return ''.join(random.choice(characters) for _ in range(length))

# # Function to check if the password has been leaked (Have I Been Pwned API)
# def check_breach(password):
#     sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
#     first5, rest = sha1_hash[:5], sha1_hash[5:]
#     response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
#     return response.status_code == 200 and rest in response.text

# # Inject custom CSS for stylish UI
# st.markdown("""
#     <style>
#         /* Style for centering all text */
#         .center-text {
#             text-align: center;
#             font-size: 32px;
#             font-weight: bold;
#             color: #4CAF50; /* Green color */
#         }

#         /* Button style */
#         .red-button {
#             background-color: #FF5733; /* Red color */
#             color: white;
#             padding: 12px 24px;
#             font-size: 16px;
#             border-radius: 8px;
#             border: none;
#             cursor: pointer;
#             width: 250px;
#             margin: 10px auto;
#             display: block;
#             text-align: center;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             transition: all 0.3s ease;
#         }

#         .red-button:hover {
#             background-color: #e04e1b; /* Darker red */
#             transform: translateY(-2px);
#         }

#         .red-button:active {
#             background-color: #b64014; /* Even darker red */
#             transform: translateY(2px);
#         }

#         /* Style for text input */
#         .stTextInput input {
#             text-align: center;
#             font-size: 18px;
#             padding: 12px;
#             border-radius: 8px;
#             border: 2px solid #ddd;
#             width: 100%;
#         }

#         /* Centering title and headers */
#         h1, h2, h3 {
#             text-align: center;
#             color: #333;
#         }

#         /* Styling for green section headers */
#         .section-header {
#             color: #4CAF50;
#             font-weight: bold;
#             text-align: center;
#             font-size: 28px;  /* Larger size */
#         }

#         .section-header-password-strength {
#             font-size: 34px;  /* Even larger size for Password Strength Meter */
#         }

#         /* Red color for the temperature section */
#         .temp-section {
#             color: red;
#             font-weight: bold;
#             text-align: center;
#         }

#         /* Red color for the time section */
#         .time-section {
#             color: red;
#             font-weight: bold;
#             text-align: center;
#             font-size: 32px;
#         }

#         /* Footer style */
#         .footer {
#             text-align: center;
#             color: #777;
#             font-size: 14px;
#             margin-top: 40px;
#         }

#         /* Progress bar color */
#         .stProgress>div>div {
#             background-color: #4CAF50; /* Green progress */
#         }

#         /* Style for code blocks */
#         pre {
#             background-color: #f7f7f7;
#             padding: 15px;
#             border-radius: 8px;
#             border: 1px solid #ddd;
#             font-size: 16px;
#             color: #333;
#         }

#         /* Background color */
#         body {
#             background-color: #f1f1f1;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Centered Title
# st.markdown('<div class="center-text">🔒 Password Manager</div>', unsafe_allow_html=True)

# # Display Current Time and Temperature using OpenWeatherMap API
# st.header("")
# karachi_tz = pytz.timezone("Asia/Karachi")
# current_time = datetime.now(karachi_tz).strftime("%I:%M %p, %d %B %Y")
# st.markdown(f"<div class='time-section'><b>🕒 {current_time}</b></div>", unsafe_allow_html=True)

# # API Key for OpenWeatherMap
# API_KEY = "ea815a44ac089b6f28d755bacec67f30"

# # Fetch Weather Data
# try:
#     weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=Karachi&appid={API_KEY}&units=metric"
#     weather_response = requests.get(weather_url)
#     if weather_response.status_code == 200:
#         weather_data = weather_response.json()
#         temperature = weather_data['main']['temp']
#         weather_condition = weather_data['weather'][0]['description']
#         st.markdown(f"<div class='temp-section'><b>🌡️ Karachi Temperature: {temperature}°C, {weather_condition.capitalize()}</b></div>", unsafe_allow_html=True)
#     else:
#         st.markdown("<div class='temp-section'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)
# except Exception as e:
#     st.markdown("<div class='temp-section'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)

# # Password Strength Checker
# st.markdown('<div class="section-header section-header-password-strength">Password Strength Meter</div>', unsafe_allow_html=True)
# password = st.text_input("Enter Password:", type="password")
# if password:
#     with st.spinner("Analyzing password strength..."):
#         time.sleep(1.5)
#     strength, score, feedback = check_password_strength(password)
#     st.progress(score / 5)
#     st.write(f"**Strength:** {strength}")  # Display result in UI
#     if strength == "Strong":
#         st.success("✅ Strong Password! Well done!")
#         st.balloons()
#     elif strength == "Moderate":
#         st.warning("⚠️ Moderate Password! Consider improving it.")
#     else:
#         st.error("❌ Weak Password! Please improve your password security.")
#     if feedback:
#         st.write("🔹 Suggestions to Improve:")
#         for tip in feedback:
#             st.write(f"   - {tip}")
#     if st.button("Check Breach Status", key="breach_button", help="Check if your password has been leaked", 
#                  use_container_width=True, 
#                  args=({"class": "red-button"})):
#         with st.spinner("Checking for breaches..."):
#             time.sleep(1.5)
#             if check_breach(password):
#                 st.error("⚠️ This password has been leaked in data breaches. Please change it!")
#             else:
#                 st.success("✅ This password has not been found in breaches!")
#     st.session_state.password_history.append({"password": password, "strength": strength})

# # Password Generator
# st.markdown('<div class="section-header">Secure Password Generator</div>', unsafe_allow_html=True)
# length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
# use_digits = st.checkbox("Include Numbers", value=True)
# use_specials = st.checkbox("Include Special Characters", value=True)
# if st.button("Generate Password", key="generate_button", use_container_width=True, 
#              args=({"class": "red-button"})):
#     with st.spinner("Generating a secure password..."):
#         time.sleep(1.5)
#     new_password = generate_password(length, use_digits, use_specials)
#     st.code(new_password, language="plaintext")
#     st.balloons()
# st.write("Use a password manager to store your generated passwords securely.")

# # Password History Section
# st.markdown('<div class="section-header">📜 Password History</div>', unsafe_allow_html=True)
# st.subheader("Stored Passwords")
# max_history = st.number_input("Number of Passwords to Show:", min_value=1, max_value=100, value=10)
# password_search = st.text_input("Search Password History:")
# if st.session_state.password_history:
#     filtered_history = [entry for entry in st.session_state.password_history if password_search in entry["password"]]
#     for idx, entry in enumerate(reversed(filtered_history[-max_history:])):
#         with st.expander(f"🔐 Password {idx + 1}"):
#             st.write(f"**Password:** `{entry['password']}`")
#             st.write(f"**Strength:** {entry['strength']}")
#     if st.button("Clear History", key="clear_history", help="Clear all stored passwords", 
#                  use_container_width=True, 
#                  args=({"class": "red-button"})):
#         st.session_state.password_history = []
#         st.success("✅ Password history cleared!")
#         st.rerun()
# else:
#     st.info("No password history available.")

# # Footer
# st.markdown('<div class="footer">Developed by Abdul Rehman | Built with ❤️ using Streamlit | Secure Passwords Matter! 🔒</div>', unsafe_allow_html=True)



# import streamlit as st
# import re
# import random
# import string
# import hashlib
# import requests
# import time
# from cryptography.fernet import Fernet
# from datetime import datetime
# import pytz

# # Set Streamlit page configuration
# st.set_page_config(page_title="🔒 Password Manager", layout="centered")

# # AES-256 Encryption Key (Generate once and store securely)
# KEY = Fernet.generate_key()
# cipher = Fernet(KEY)

# # Initialize session state for password history if not exists
# if "password_history" not in st.session_state:
#     st.session_state.password_history = []

# # Function to check password strength
# def check_password_strength(pwd):
#     score = 0
#     feedback = []
#     if len(pwd) >= 8:
#         score += 1
#     else:
#         feedback.append("Increase password length to at least 8 characters.")
#     if re.search(r"[A-Z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one uppercase letter (A-Z).")
#     if re.search(r"[a-z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one lowercase letter (a-z).")
#     if re.search(r"\d", pwd):
#         score += 1
#     else:
#         feedback.append("Include at least one digit (0-9).")
#     if re.search(r"[!@#$%^&*]", pwd):
#         score += 1
#     else:
#         feedback.append("Use at least one special character (!@#$%^&*).")
#     if score == 5:
#         return "Strong", score, feedback
#     elif score >= 3:
#         return "Moderate", score, feedback
#     else:
#         return "Weak", score, feedback

# # Function to generate a strong random password
# def generate_password(length=12, use_digits=True, use_specials=True, use_upper=True, use_lower=True):
#     characters = ""
#     if use_upper:
#         characters += string.ascii_uppercase
#     if use_lower:
#         characters += string.ascii_lowercase
#     if use_digits:
#         characters += string.digits
#     if use_specials:
#         characters += "!@#$%^&*"
    
#     return ''.join(random.choice(characters) for _ in range(length))

# # Function to check if the password has been leaked (Have I Been Pwned API)
# def check_breach(password):
#     sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
#     first5, rest = sha1_hash[:5], sha1_hash[5:]
#     response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
#     return response.status_code == 200 and rest in response.text

# # Inject custom CSS for stylish UI
# st.markdown("""
#     <style>
#         /* Style for centering all text */
#         .center-text {
#             text-align: center;
#             font-size: 32px;
#             font-weight: bold;
#             color: #4CAF50; /* Green color */
#         }

#         /* Button style */
#         .red-button {
#             background-color: #FF5733; /* Red color */
#             color: white;
#             padding: 12px 24px;
#             font-size: 16px;
#             border-radius: 8px;
#             border: none;
#             cursor: pointer;
#             width: 250px;
#             margin: 10px auto;
#             display: block;
#             text-align: center;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             transition: all 0.3s ease;
#         }

#         .red-button:hover {
#             background-color: #e04e1b; /* Darker red */
#             transform: translateY(-2px);
#         }

#         .red-button:active {
#             background-color: #b64014; /* Even darker red */
#             transform: translateY(2px);
#         }

#         /* Style for text input */
#         .stTextInput input {
#             text-align: center;
#             font-size: 18px;
#             padding: 12px;
#             border-radius: 8px;
#             border: 2px solid #ddd;
#             width: 100%;
#         }

#         /* Centering title and headers */
#         h1, h2, h3 {
#             text-align: center;
#             color: #333;
#         }

#         /* Styling for green section headers */
#         .section-header {
#             color: #4CAF50;
#             font-weight: bold;
#             text-align: center;
#             font-size: 28px;  /* Larger size */
#         }

#         .section-header-password-strength {
#             font-size: 34px;  /* Even larger size for Password Strength Meter */
#         }

#         /* Red color for the temperature section */
#         .temp-section {
#             color: red;
#             font-weight: bold;
#             text-align: center;
#         }

#         /* Red color for the time section */
#         .time-section {
#             color: red;
#             font-weight: bold;
#             text-align: center;
#             font-size: 32px;
#         }

#         /* Footer style */
#         .footer {
#             text-align: center;
#             color: #777;
#             font-size: 14px;
#             margin-top: 40px;
#         }

#         /* Progress bar color */
#         .stProgress>div>div {
#             background-color: #4CAF50; /* Green progress */
#         }

#         /* Style for code blocks */
#         pre {
#             background-color: #f7f7f7;
#             padding: 15px;
#             border-radius: 8px;
#             border: 1px solid #ddd;
#             font-size: 16px;
#             color: #333;
#         }

#         /* Background color */
#         body {
#             background-color: #f1f1f1;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Centered Title
# st.markdown('<div class="center-text">🔒 Password Manager</div>', unsafe_allow_html=True)

# # Password Strength Checker
# st.markdown('<div class="section-header section-header-password-strength">Password Strength Meter</div>', unsafe_allow_html=True)
# password = st.text_input("Enter Password:", type="password")
# if password:
#     with st.spinner("Analyzing password strength..."):
#         time.sleep(1.5)
#     strength, score, feedback = check_password_strength(password)
#     st.progress(score / 5)
#     st.write(f"**Strength:** {strength}")  # Display result in UI
#     if strength == "Strong":
#         st.success("✅ Strong Password! Well done!")
#         st.balloons()
#     elif strength == "Moderate":
#         st.warning("⚠️ Moderate Password! Consider improving it.")
#     else:
#         st.error("❌ Weak Password! Please improve your password security.")
#     if feedback:
#         st.write("🔹 Suggestions to Improve:")
#         for tip in feedback:
#             st.write(f"   - {tip}")

# # Secure Password Generator Section
# st.markdown('<div class="section-header">Secure Password Generator</div>', unsafe_allow_html=True)
# length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
# use_digits = st.checkbox("Include Numbers", value=True)
# use_specials = st.checkbox("Include Special Characters", value=True)
# use_upper = st.checkbox("Include Uppercase Letters", value=True)
# use_lower = st.checkbox("Include Lowercase Letters", value=True)

# # Generate Password Button
# if st.button("Generate Password", key="generate_button", use_container_width=True, 
#              help="Generate a strong password", 
#              args=({"class": "red-button"})):
#     with st.spinner("Generating a secure password..."):
#         time.sleep(1.5)
#     new_password = generate_password(length, use_digits, use_specials, use_upper, use_lower)
#     st.code(new_password, language="plaintext")
#     st.session_state.generated_password = new_password  # Store the generated password
#     st.balloons()

#     # Provide download link for the generated password
#     password_file = f"{new_password}.txt"
#     st.download_button(
#         label="Download Password",
#         data=new_password,
#         file_name=password_file,
#         mime="text/plain",
#         use_container_width=True,
#         key="download_button",
#         help="Click to download your generated password",
#         args=({"class": "red-button"})
#     )

# st.write("Use a password manager to store your generated passwords securely.")

# # Password History Section
# st.markdown('<div class="section-header">📜 Password History</div>', unsafe_allow_html=True)
# st.subheader("Stored Passwords")
# max_history = st.number_input("Number of Passwords to Show:", min_value=1, max_value=100, value=10)
# password_search = st.text_input("Search Password History:")
# if st.session_state.password_history:
#     filtered_history = [entry for entry in st.session_state.password_history if password_search in entry["password"]]
#     for idx, entry in enumerate(reversed(filtered_history[-max_history:])):
#         with st.expander(f"🔐 Password {idx + 1}"):
#             st.write(f"**Password:** `{entry['password']}`")
#             st.write(f"**Strength:** {entry['strength']}")
#     if st.button("Clear History", key="clear_history", help="Clear all stored passwords", 
#                  use_container_width=True, 
#                  args=({"class": "red-button"})):
#         st.session_state.password_history = []
#         st.success("✅ Password history cleared!")
#         st.rerun()
# else:
#     st.info("No password history available.")

# # Footer
# st.markdown('<div class="footer">Developed by Abdul Rehman | Built with ❤️ using Streamlit | Secure Passwords Matter! 🔒</div>', unsafe_allow_html=True)



# import streamlit as st
# import re
# import random
# import string
# import hashlib
# import requests
# import time
# from cryptography.fernet import Fernet
# from datetime import datetime
# import pytz

# # Set Streamlit page configuration
# st.set_page_config(page_title="🔒 Password Manager", layout="centered")

# # AES-256 Encryption Key (Generate once and store securely)
# KEY = Fernet.generate_key()
# cipher = Fernet(KEY)

# # Initialize session state for password history if not exists
# if "password_history" not in st.session_state:
#     st.session_state.password_history = []

# # Function to check password strength
# def check_password_strength(pwd):
#     score = 0
#     feedback = []
#     if len(pwd) >= 8:
#         score += 1
#     else:
#         feedback.append("Increase password length to at least 8 characters.")
#     if re.search(r"[A-Z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one uppercase letter (A-Z).")
#     if re.search(r"[a-z]", pwd):
#         score += 1
#     else:
#         feedback.append("Add at least one lowercase letter (a-z).")
#     if re.search(r"\d", pwd):
#         score += 1
#     else:
#         feedback.append("Include at least one digit (0-9).")
#     if re.search(r"[!@#$%^&*]", pwd):
#         score += 1
#     else:
#         feedback.append("Use at least one special character (!@#$%^&*).")
#     if score == 5:
#         return "Strong", score, feedback
#     elif score >= 3:
#         return "Moderate", score, feedback
#     else:
#         return "Weak", score, feedback

# # Function to generate a strong random password
# def generate_password(length=12, use_digits=True, use_specials=True, use_upper=True, use_lower=True):
#     characters = ""
#     if use_upper:
#         characters += string.ascii_uppercase
#     if use_lower:
#         characters += string.ascii_lowercase
#     if use_digits:
#         characters += string.digits
#     if use_specials:
#         characters += "!@#$%^&*"
    
#     return ''.join(random.choice(characters) for _ in range(length))

# # Function to check if the password has been leaked (Have I Been Pwned API)
# def check_breach(password):
#     sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
#     first5, rest = sha1_hash[:5], sha1_hash[5:]
#     response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
#     return response.status_code == 200 and rest in response.text

# # Function to get weather information
# def get_weather_data(city="London"):
#     api_key = "ea815a44ac089b6f28d755bacec67f30"  # Replace with your OpenWeatherMap API Key
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     data = response.json()
    
#     if data["cod"] == 200:
#         main = data["main"]
#         weather = data["weather"][0]
#         temperature = main["temp"]
#         city_name = data["name"]
#         weather_description = weather["description"]
#         return city_name, temperature, weather_description
#     else:
#         return "Error", "N/A", "N/A"

# # Inject custom CSS for stylish UI
# st.markdown("""
#     <style>
#         /* Style for centering all text */
#         .center-text {
#             text-align: center;
#             font-size: 32px;
#             font-weight: bold;
#             color: #4CAF50; /* Green color */
#         }

#         /* Button style */
#         .red-button {
#             background-color: #FF5733; /* Red color */
#             color: white;
#             padding: 12px 24px;
#             font-size: 16px;
#             border-radius: 8px;
#             border: none;
#             cursor: pointer;
#             width: 250px;
#             margin: 10px auto;
#             display: block;
#             text-align: center;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             transition: all 0.3s ease;
#         }

#         .red-button:hover {
#             background-color: #e04e1b; /* Darker red */
#             transform: translateY(-2px);
#         }

#         .red-button:active {
#             background-color: #b64014; /* Even darker red */
#             transform: translateY(2px);
#         }

#         /* Style for text input */
#         .stTextInput input {
#             text-align: center;
#             font-size: 18px;
#             padding: 12px;
#             border-radius: 8px;
#             border: 2px solid #ddd;
#             width: 100%;
#         }

#         /* Centering title and headers */
#         h1, h2, h3 {
#             text-align: center;
#             color: #333;
#         }

#         /* Styling for green section headers */
#         .section-header {
#             color: #4CAF50;
#             font-weight: bold;
#             text-align: center;
#             font-size: 28px;  /* Larger size */
#         }

#         .section-header-password-strength {
#             font-size: 34px;  /* Even larger size for Password Strength Meter */
#         }

#         /* Red color for the temperature section */
#         .temp-section {
#             color: red;
#             font-weight: bold;
#             text-align: center;
#         }

#         /* Red color for the time section */
#         .time-section {
#             color: red;
#             font-weight: bold;
#             text-align: center;
#             font-size: 32px;
#         }

#         /* Footer style */
#         .footer {
#             text-align: center;
#             color: #777;
#             font-size: 14px;
#             margin-top: 40px;
#         }

#         /* Progress bar color */
#         .stProgress>div>div {
#             background-color: #4CAF50; /* Green progress */
#         }

#         /* Style for code blocks */
#         pre {
#             background-color: #f7f7f7;
#             padding: 15px;
#             border-radius: 8px;
#             border: 1px solid #ddd;
#             font-size: 16px;
#             color: #333;
#         }

#         /* Background color */
#         body {
#             background-color: #f1f1f1;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Centered Title
# st.markdown('<div class="center-text">🔒 Password Manager</div>', unsafe_allow_html=True)

# # Get current date and time
# current_time = datetime.now(pytz.timezone("UTC"))
# current_date_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# # Display date and time
# st.markdown(f'<div class="time-section">Current Date and Time: {current_date_time}</div>', unsafe_allow_html=True)

# # Fetch and display weather data (City and Temperature)
# city, temperature, description = get_weather_data(city="London")  # Replace with any city
# st.markdown(f'<div class="temp-section">Weather in {city}: {temperature}°C, {description.capitalize()}</div>', unsafe_allow_html=True)

# # Password Strength Checker
# st.markdown('<div class="section-header section-header-password-strength">Password Strength Meter</div>', unsafe_allow_html=True)
# password = st.text_input("Enter Password:", type="password")
# if password:
#     with st.spinner("Analyzing password strength..."):
#         time.sleep(1.5)
#     strength, score, feedback = check_password_strength(password)
#     st.progress(score / 5)
#     st.write(f"**Strength:** {strength}")  # Display result in UI
#     if strength == "Strong":
#         st.success("✅ Strong Password! Well done!")
#         st.balloons()
#     elif strength == "Moderate":
#         st.warning("⚠️ Moderate Password! Consider improving it.")
#     else:
#         st.error("❌ Weak Password! Please improve your password security.")
#     if feedback:
#         st.write("🔹 Suggestions to Improve:")
#         for tip in feedback:
#             st.write(f"   - {tip}")

# # Secure Password Generator Section
# st.markdown('<div class="section-header">Secure Password Generator</div>', unsafe_allow_html=True)
# length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
# use_digits = st.checkbox("Include Numbers", value=True)
# use_specials = st.checkbox("Include Special Characters", value=True)
# use_upper = st.checkbox("Include Uppercase Letters", value=True)
# use_lower = st.checkbox("Include Lowercase Letters", value=True)

# # Generate Password Button
# if st.button("Generate Password", key="generate_button", use_container_width=True, 
#              help="Generate a strong password", 
#              args=({"class": "red-button"})):
#     with st.spinner("Generating a secure password..."):
#         time.sleep(1.5)
#     new_password = generate_password(length, use_digits, use_specials, use_upper, use_lower)
#     st.code(new_password, language="plaintext")
#     st.session_state.generated_password = new_password  # Store the generated password
#     st.balloons()

#     # Provide download link for the generated password
#     password_file = f"{new_password}.txt"
#     st.download_button(
#         label="Download Password",
#         data=new_password,
#         file_name=password_file,
#         mime="text/plain",
#         use_container_width=True,
#         key="download_button",
#         help="Click to download your generated password",
#         args=({"class": "red-button"})
#     )

# st.write("Use a password manager to store your generated passwords securely.")

# # Password History Section
# st.markdown('<div class="section-header">📜 Password History</div>', unsafe_allow_html=True)
# st.subheader("Stored Passwords")
# max_history = st.number_input("Number of Passwords to Show:", min_value=1, max_value=100, value=10)
# password_search = st.text_input("Search Password History:")
# if st.session_state.password_history:
#     filtered_history = [entry for entry in st.session_state.password_history if password_search in entry["password"]]
#     for idx, entry in enumerate(reversed(filtered_history[-max_history:])):
#         with st.expander(f"🔐 Password {idx + 1}"):
#             st.write(f"**Password:** `{entry['password']}`")
#             st.write(f"**Strength:** {entry['strength']}")
#     if st.button("Clear History", key="clear_history", help="Clear all stored passwords", 
#                  use_container_width=True, 
#                  args=({"class": "red-button"})):
#         st.session_state.password_history = []
#         st.success("✅ Password history cleared!")
#         st.rerun()
# else:
#     st.info("No password history available.")

# # Footer
# st.markdown('<div class="footer">Developed by Abdul Rehman | Built with ❤️ using Streamlit | Secure Passwords Matter! 🔒</div>', unsafe_allow_html=True)



import streamlit as st
import re
import random
import string
import hashlib
import requests
import time
from cryptography.fernet import Fernet
from datetime import datetime
import pytz

# Set Streamlit page configuration
st.set_page_config(page_title="🔒 Password Manager", layout="centered")

# AES-256 Encryption Key (Generate once and store securely)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# Initialize session state for password history if not exists
if "password_history" not in st.session_state:
    st.session_state.password_history = []

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
def generate_password(length=12, use_digits=True, use_specials=True, use_upper=True, use_lower=True):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
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
    return response.status_code == 200 and rest in response.text

# Function to get weather information for Karachi
def get_weather_data(city="Karachi"):
    api_key = "ea815a44ac089b6f28d755bacec67f30"  # Replace with your OpenWeatherMap API Key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        city_name = data["name"]
        weather_description = weather["description"]
        return city_name, temperature, weather_description
    else:
        return "Error", "N/A", "N/A"

# Inject custom CSS for stylish UI
st.markdown("""
    <style>
        /* Style for centering all text */
        .center-text {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: #4CAF50; /* Green color */
        }

        /* Button style */
        .red-button {
            background-color: #FF5733; /* Red color */
            color: white;
            padding: 12px 24px;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            width: 250px;
            margin: 10px auto;
            display: block;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .red-button:hover {
            background-color: #e04e1b; /* Darker red */
            transform: translateY(-2px);
        }

        .red-button:active {
            background-color: #b64014; /* Even darker red */
            transform: translateY(2px);
        }

        /* Style for text input */
        .stTextInput input {
            text-align: center;
            font-size: 18px;
            padding: 12px;
            border-radius: 8px;
            border: 2px solid #ddd;
            width: 100%;
        }

        /* Centering title and headers */
        h1, h2, h3 {
            text-align: center;
            color: #333;
        }

        /* Styling for green section headers */
        .section-header {
            color: #4CAF50;
            font-weight: bold;
            text-align: center;
            font-size: 28px;  /* Larger size */
        }

        .section-header-password-strength {
            font-size: 34px;  /* Even larger size for Password Strength Meter */
        }

        /* Red color for the temperature section */
        .temp-section {
            color: red;
            font-weight: bold;
            text-align: center;
        }

        /* Red color for the time section */
        .time-section {
            color: red;
            font-weight: bold;
            text-align: center;
            font-size: 32px;
        }

        /* Footer style */
        .footer {
            text-align: center;
            color: #777;
            font-size: 14px;
            margin-top: 40px;
        }

        /* Progress bar color */
        .stProgress>div>div {
            background-color: #4CAF50; /* Green progress */
        }

        /* Style for code blocks */
        pre {
            background-color: #f7f7f7;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #ddd;
            font-size: 16px;
            color: #333;
        }

        /* Background color */
        body {
            background-color: #f1f1f1;
        }
    </style>
""", unsafe_allow_html=True)

# Centered Title
st.markdown('<div class="center-text">🔒 Password Manager</div>', unsafe_allow_html=True)

# Get current date and time
current_time = datetime.now(pytz.timezone("UTC"))
current_date_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Display date and time
st.markdown(f'<div class="time-section">Current Date and Time: {current_date_time}</div>', unsafe_allow_html=True)

# Fetch and display weather data for Karachi
city, temperature, description = get_weather_data(city="Karachi")  # Karachi weather update
st.markdown(f'<div class="temp-section">Weather in {city}: {temperature}°C, {description.capitalize()}</div>', unsafe_allow_html=True)

# Password Strength Checker
st.markdown('<div class="section-header section-header-password-strength">Password Strength Meter</div>', unsafe_allow_html=True)
password = st.text_input("Enter Password:", type="password")
if password:
    with st.spinner("Analyzing password strength..."):
        time.sleep(1.5)
    strength, score, feedback = check_password_strength(password)
    st.progress(score / 5)
    st.write(f"**Strength:** {strength}")  # Display result in UI
    if strength == "Strong":
        st.success("✅ Strong Password! Well done!")
        st.balloons()
    elif strength == "Moderate":
        st.warning("⚠️ Moderate Password! Consider improving it.")
    else:
        st.error("❌ Weak Password! Please improve your password security.")
    if feedback:
        st.write("🔹 Suggestions to Improve:")
        for tip in feedback:
            st.write(f"   - {tip}")

# Secure Password Generator Section
st.markdown('<div class="section-header">Secure Password Generator</div>', unsafe_allow_html=True)
length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
use_digits = st.checkbox("Include Numbers", value=True)
use_specials = st.checkbox("Include Special Characters", value=True)
use_upper = st.checkbox("Include Uppercase Letters", value=True)
use_lower = st.checkbox("Include Lowercase Letters", value=True)

# Generate Password Button
if st.button("Generate Password", key="generate_button", use_container_width=True, 
             help="Generate a strong password", 
             args=({"class": "red-button"})):
    with st.spinner("Generating a secure password..."):
        time.sleep(1.5)
    new_password = generate_password(length, use_digits, use_specials, use_upper, use_lower)
    st.code(new_password, language="plaintext")
    st.session_state.generated_password = new_password  # Store the generated password
    st.balloons()

    # Provide download link for the generated password
    password_file = f"{new_password}.txt"
    st.download_button(
        label="Download Password",
        data=new_password,
        file_name=password_file,
        mime="text/plain",
        use_container_width=True,
        key="download_button",
        help="Click to download your generated password",
        args=({"class": "red-button"})
    )

st.write("Use a password manager to store your generated passwords securely.")

# Password History Section
st.markdown('<div class="section-header">📜 Password History</div>', unsafe_allow_html=True)
st.subheader("Stored Passwords")
max_history = st.number_input("Number of Passwords to Show:", min_value=1, max_value=100, value=10)
password_search = st.text_input("Search Password History:")
if st.session_state.password_history:
    filtered_history = [entry for entry in st.session_state.password_history if password_search in entry["password"]]
    for idx, entry in enumerate(reversed(filtered_history[-max_history:])):
        with st.expander(f"🔐 Password {idx + 1}"):
            st.write(f"**Password:** `{entry['password']}`")
            st.write(f"**Strength:** {entry['strength']}")
    if st.button("Clear History", key="clear_history", help="Clear all stored passwords", 
                 use_container_width=True, 
                 args=({"class": "red-button"})):
        st.session_state.password_history = []
        st.success("✅ Password history cleared!")
        st.rerun()
else:
    st.info("No password history available.")

# Footer
st.markdown('<div class="footer">Developed by Abdul Rehman | Built with ❤️ using Streamlit | Secure Passwords Matter! 🔒</div>', unsafe_allow_html=True)

































