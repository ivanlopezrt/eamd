import tkinter as tk

def add_website():
    website = entry.get()
    if website:
        listbox.insert(tk.END, website)
        entry.delete(0, tk.END)

def remove_website():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

def clear_all():
    listbox.delete(0, tk.END)

def save_changes():
    websites = listbox.get(0, tk.END)
    # Save the list of websites to a file or perform other actions

root = tk.Tk()
root.title("Website Blocker")

# Blocked Websites
blocked_frame = tk.LabelFrame(root, text="Blocked Websites")
blocked_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(blocked_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(blocked_frame, yscrollcommand=scrollbar.set)
listbox.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=listbox.yview)

# Options
options_frame = tk.LabelFrame(root, text="Options")
options_frame.pack(padx=10, pady=10)

entry = tk.Entry(options_frame)
entry.pack(pady=5)

add_button = tk.Button(options_frame, text="Add Website", command=add_website)
add_button.pack(pady=5)

remove_button = tk.Button(options_frame, text="Remove Website", command=remove_website)
remove_button.pack(pady=5)

clear_button = tk.Button(options_frame, text="Clear All", command=clear_all)
clear_button.pack(pady=5)

# Save and Cancel buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

save_button = tk.Button(button_frame, text="Save", command=save_changes)
save_button.pack(side=tk.LEFT, padx=5)

cancel_button = tk.Button(button_frame, text="Cancel", command=root.quit)
cancel_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
