import subprocess
import os
import webbrowser
import threading
import time

# ======== Timer Functions ========
timers = {}  # Dictionary to keep track of active timers

def start_timer(name, seconds):
    if name in timers:
        return f"Timer '{name}' is already running!"
    
    def timer_thread():
        time.sleep(seconds)
        print(f"Timer '{name}' finished!")
        timers.pop(name)
    
    t = threading.Thread(target=timer_thread)
    t.start()
    timers[name] = t
    return f"Timer '{name}' started for {seconds} seconds."

# ======== Open Applications ========
def open_app(app_name):
    try:
        if app_name.lower() == "calculator":
            subprocess.Popen("calc.exe")
        elif app_name.lower() == "notepad":
            subprocess.Popen("notepad.exe")
        else:
            return f"No app named '{app_name}' configured."
        return f"Opening {app_name}!"
    except Exception as e:
        return f"Failed to open {app_name}: {str(e)}"

# ======== Open Websites ========
def open_website(url_or_name):
    if not url_or_name.startswith("http"):
        url_or_name = "https://www." + url_or_name
    webbrowser.open(url_or_name)
    return f"Opening {url_or_name}!"