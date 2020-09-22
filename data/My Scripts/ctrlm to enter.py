apps = ["emacs.Emacs"];   

if window.get_active_class() == "VirtualBox Machine.VirtualBox Machine":
    exit
elif window.get_active_class() in apps:
    keyboard.send_keys("<ctrl>+m")
else:
    keyboard.send_keys("<enter>")