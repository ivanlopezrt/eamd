import tkinter as tk
import json
import router_state

#TODO:
#1- call change_state when checkbox is clicked
#2- exit program when window is closed
#3- add change state of router when button is clicked (with Ivan)


def save_settings():
    settings = {
        "Block ChatGPT": var_chatgpt.get(),
        "Block stackoverflow": var_stackoverflow.get(),
        "Block github": var_github.get(),
        "Block strimming platforms": var_streaming.get()
    }
    with open("settings.json", "w") as file:
        json.dump(settings, file)

def change_internet_state():
    if btn_block_internet["text"] == "Block Internet":
        # Block internet logic here
        btn_block_internet["text"] = "Unblock Internet"
    else:
        # Unblock internet logic here
        btn_block_internet["text"] = "Block Internet"



def refresh_state():
    try:
        var_chatgpt.set(router_state.isBlocked(what="chatgpt3"))
        var_stackoverflow.set(router_state.isBlocked(what="stackoverflow"))
        var_github.set(router_state.isBlocked(what="github"))
        var_streaming.set(router_state.isBlocked(what="streaming"))
    except router_state.InexistingRuleException as e:
        print("Exception: " + str(e))
    except Exception as e:
        print("Error connecting to router: Exception: " + str(e))
        isConnected = False
    # Refresh state logic here
    pass


# Create the main window
window = tk.Tk()
window.title("Internet Blocker")
window.geometry("400x300")  # Set the initial window size

isConnected=True

# Create checkboxes
try:
    var_chatgpt = tk.IntVar()
    var_chatgpt.set(router_state.isBlocked(what="chatgpt3"))
    chk_chatgpt = tk.Checkbutton(window, text="Block ChatGPT", variable=var_chatgpt, command=change_internet_state)

    chk_chatgpt.pack(anchor=tk.W)
except router_state.InexistingRuleException as e:
    print("Exception: "+str(e))
except Exception as e:
    print("Error connecting to router: Exception: "+str(e))
    isConnected=False

if isConnected:
    try:
        var_stackoverflow = tk.IntVar()
        var_stackoverflow.set(router_state.isBlocked(what="stackoverflow"))
        chk_chatgpt = tk.Checkbutton(window, text="Block stackoveflow", variable=var_stackoverflow, command=change_internet_state)

        chk_stackoverflow.pack(anchor=tk.W)
    except router_state.InexistingRuleException as e:
        print("Exception: "+str(e))
    except Exception as e:
        print("Error connecting to router: Exception: "+str(e))

    try:
        var_github = tk.IntVar()
        var_github.set(router_state.isBlocked(what="github"))
        chk_chatgpt = tk.Checkbutton(window, text="Block github", variable=var_github, command=change_internet_state)

        chk_github.pack(anchor=tk.W)
    except router_state.InexistingRuleException as e:
        print("Exception: "+str(e))
    except Exception as e:
        print("Error connecting to router: Exception: "+str(e))

    try:
        var_streaming = tk.IntVar()
        var_streaming.set(router_state.isBlocked(what="streaming"))
        chk_streaming = tk.Checkbutton(window, text="Block streaming platforms", variable=var_streaming, command=change_internet_state)


        chk_streaming.pack(anchor=tk.W)
    except router_state.InexistingRuleException as e:
        print("Exception: "+str(e))
    except Exception as e:
        print("Error connecting to router: Exception: "+str(e))

# Create buttons
btn_block_internet = tk.Button(window, text="Block Internet", command=change_internet_state, height=3, width=20)
btn_block_internet.pack(pady=10)

btn_refresh = tk.Button(window, text="Refresh", command=refresh_state, height=3, width=20)
btn_refresh.pack(pady=10)




# Create exceptions textbox
txt_exceptions = tk.Text(window, height=5)
txt_exceptions.pack(fill=tk.BOTH, expand=True)


# Save settings when the window is closed
window.protocol("WM_DELETE_WINDOW", save_settings)
window.protocol("WM_DELETE_WINDOW", window.quit)


# Start the main event loop
window.mainloop()
