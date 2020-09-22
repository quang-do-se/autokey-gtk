if window.get_active_class() == "VirtualBox Machine.VirtualBox Machine":
    exit   
elif window.get_active_class() == "google-chrome.Google-chrome":
    keyboard.send_keys("<ctrl>+<shift>+<tab>")
else:
    keyboard.send_keys("<ctrl>+[")