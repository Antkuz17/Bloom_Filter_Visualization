import tkinter as tk
from tkinter import ttk

# GitHub colors
BG_DARK = '#101411'      # Gray 6 - darkest background
BG_PANEL = '#232925'     # Gray 5 - panels
TEXT = '#F2F5F3'         # Gray 1 - text
GREEN = '#0FBF3E'        # GitHub green
GREEN_LIGHT = '#5FED83'  # Green 3


# Actual window setup
root = tk.Tk()
root.title("Bloom Filter Visualizer")
root.geometry("800x600")  # Width x Height
root.config(bg=BG_DARK)

# Setup frame 
setup_frame = tk.Frame(root, bg=BG_PANEL, padx=20, pady=15)
setup_frame.pack(fill='x', side='top')

# Number of bits label and entry
bits_label = tk.Label(setup_frame, text="Number of bits:", bg=BG_PANEL, fg=TEXT, font=('Times New Roman', 10))
bits_label.grid(row=0, column=0, padx=10, sticky='w')

# Dropdown for number of bits
bits_var = tk.StringVar(value="1000")
bits_dropdown = ttk.Combobox(setup_frame, textvariable=bits_var, values=["100", "500", "1000", "5000", "10000"],width=10, state='readonly')
bits_dropdown.grid(row=0, column=1, padx=10)

# Number of hash functions label and entry
hash_label = tk.Label(setup_frame, text="Number of hash functions:", bg=BG_PANEL, fg=TEXT, font=('Times New Roman', 10))
hash_label.grid(row=0, column=2, padx=10, sticky='w')
hash_var = tk.StringVar(value="3")
hash_dropdown = ttk.Combobox(setup_frame, textvariable=hash_var,values=["2", "3", "4", "5"],width=5, state='readonly')
hash_dropdown.grid(row=0, column=3, padx=10)


def create_filter():
    num_bits = int(bits_var.get())
    num_hashes = int(hash_var.get())
    print(f"Creating filter: {num_bits} bits, {num_hashes} hash functions")
    # We'll add bloom filter creation here later

create_btn = tk.Button(setup_frame, text="Create Filter", 
                       command=create_filter,
                       bg=GREEN, fg=BG_DARK, 
                       font=('Times New Roman', 10, 'bold'),
                       padx=15, pady=5, bd=0)
create_btn.grid(row=0, column=4, padx=20)

root.mainloop()

