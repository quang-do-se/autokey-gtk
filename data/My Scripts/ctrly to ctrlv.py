apps = ["google-chrome.Google-chrome", "zoom.zoom", "Navigator.Firefox"];

if window.get_active_class() == "VirtualBox Machine.VirtualBox Machine":
    exit   
elif window.get_active_class() in apps:
    keyboard.send_keys("<ctrl>+v")
else:
    keyboard.send_keys("<ctrl>+y")