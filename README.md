# 🛡️ Python Keylogger (Educational Purpose Only)

This is a simple Python-based keylogger script that logs all keystrokes from the keyboard and periodically sends them to a specified email address.

⚠️ **Disclaimer:**  
This tool is strictly for **educational**, **research**, or **ethical hacking practice** on **your own devices**. Unauthorized use to monitor others is **illegal and unethical**.

---

## 🚀 Features

- Captures every key press on the system
- Sends the captured keystrokes to an email every 30 seconds
- Uses Python's `pynput`, `smtplib`, and `threading` modules

---

## 🧩 Requirements

- Python 3.x  
- Install dependencies:
  
```bash
pip install pynput
```

## ⚙️ Usage
Replace user@gmail.com and password with your sender email and app-specific password.

Run the script:
```bash
python keylogger.py
```
⚠️ Gmail may block normal passwords. Enable App Passwords or use a service like Mailtrap for testing.

## 📚 Legal Notice
This script is created for educational and personal use only.
Do not run it on systems or networks you do not own or have explicit permission to monitor.
