import tkinter as tk
import json
import router_state

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
    myJSON = myJSON['credentials'][0]


def stop_block_internet():
    myJSON = json.load(open('mydata.json'))
    myJSON = myJSON['credentials'][0]

def router_status():
    if router_state.isBlocked(what='chatgpt3'):
        return "ChatGPT is blocked"
    else:
        router_state.block(what='chatgpt3')
        return "ChatGPT is now blocked"

# Create the main window
window = tk.Tk()
window.title("Internet Blocker")
window.geometry("400x300")  # Set the initial window size

# Create checkboxes
var_chatgpt = tk.IntVar()
chk_chatgpt = tk.Checkbutton(window, text="Block ChatGPT", variable=var_chatgpt)
chk_chatgpt.pack(anchor=tk.W)

var_stackoverflow = tk.IntVar()
chk_stackoverflow = tk.Checkbutton(window, text="Block stackoverflow", variable=var_stackoverflow)
chk_stackoverflow.pack(anchor=tk.W)

var_github = tk.IntVar()
chk_github = tk.Checkbutton(window, text="Block github", variable=var_github)
chk_github.pack(anchor=tk.W)

var_streaming = tk.IntVar()
chk_streaming = tk.Checkbutton(window, text="Block streaming platforms", variable=var_streaming)
chk_streaming.pack(anchor=tk.W)

# Create buttons
btn_block_internet = tk.Button(window, text="Block Internet", command=block_internet, height=3, width=20)
btn_block_internet.pack(pady=10)

btn_stop_block_internet = tk.Button(window, text="Stop Block Internet", command=stop_block_internet, height=3, width=20)
btn_stop_block_internet.pack()



# Create exceptions textbox
txt_exceptions = tk.Text(window, height=5)
txt_exceptions.pack(fill=tk.BOTH, expand=True)


# Save settings when the window is closed
window.protocol("WM_DELETE_WINDOW", save_settings)

# Start the main event loop
window.mainloop()
