apps = ["emacs.Emacs", "gnome-terminal-server.Gnome-terminal"];   

if window.get_active_class() == "VirtualBox Machine.VirtualBox Machine":
    exit
elif window.get_active_class() in apps:
    keyboard.send_keys("<alt>+<shift>+,")
else:
    keyboard.send_keys("<home>")