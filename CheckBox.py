import router_state
import json


with open('mydata.json', 'r') as f:
    json_object = json.loads(f.read())

from tkinter import *

print(router_state.blocked_chatgpt())
def display():
    print("ChatGPT is blocked")
# Create the main window
window = Tk()
x = IntVar()

checkbox = Checkbutton(window, text="Block ChatGPT", variable=x, onvalue=0, command=display)
checkbox.pack()




# Start the main event loop
window.mainloop()
