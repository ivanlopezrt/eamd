import router_state
import tkinter as tk
import json

def save_settings():
    settings = {
        "Block ChatGPT": var_chatgpt.get(),
        "Block stackoverflow": var_stackoverflow.get(),
        "Block github": var_github.get(),
        "Block strimming platforms": var_streaming.get()
    }
    with open("settings.json", "w") as file:
        json.dump(settings, file)

def block_internet():
    myJSON = json.load(open('mydata.json'))
    myJSON=myJSON['credentials'][0]
def stop_block_internet():
    myJSON = json.load(open('mydata.json'))
    myJSON = myJSON['credentials'][0]

# Create the main window
window = tk.Tk()
window.title("Internet Blocker")

# Create checkboxes
var_chatgpt = tk.IntVar()
chk_chatgpt = tk.Checkbutton(window, text="Block ChatGPT", variable=var_chatgpt)
chk_chatgpt.pack()

var_stackoverflow = tk.IntVar()
chk_stackoverflow = tk.Checkbutton(window, text="Block stackoverflow", variable=var_stackoverflow)
chk_stackoverflow.pack()

var_github = tk.IntVar()
chk_github = tk.Checkbutton(window, text="Block github", variable=var_github)
chk_github.pack()

var_streaming = tk.IntVar()
chk_streaming = tk.Checkbutton(window, text="Block strimming platforms", variable=var_streaming)
chk_streaming.pack()

# Create buttons
btn_block_internet = tk.Button(window, text="Block Internet", command=block_internet)
btn_block_internet.pack()

btn_stop_block_internet = tk.Button(window, text="Stop Block Internet", command=stop_block_internet)
btn_stop_block_internet.pack()

# Save settings when the window is closed
window.protocol("WM_DELETE_WINDOW", save_settings)

# Load settings from the JSON file (if it exists)
try:
    with open("settings.json", "r") as file:
        settings = json.load(file)
        var_chatgpt.set(settings.get("Block ChatGPT", 0))
        var_stackoverflow.set(settings.get("Block stackoverflow", 0))
        var_github.set(settings.get("Block github", 0))
        var_streaming.set(settings.get("Block strimming platforms", 0))
except FileNotFoundError:
    pass

# Start the main event loop
window.mainloop()
