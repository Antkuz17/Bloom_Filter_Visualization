import tkinter as tk
from tkinter import ttk
import sys
sys.path.append('../Logic') # Adjust path as needed
import bloom

# GitHub colors
BG_DARK = '#101411'      # Gray 6 - darkest background
BG_PANEL = '#232925'     # Gray 5 - panels
TEXT = '#F2F5F3'         # Gray 1 - text
GREEN = '#0FBF3E'        # GitHub green
GREEN_LIGHT = '#5FED83'  # Green 3

bf = None

def create_filter():
    global bf
    num_bits = int(bits_var.get())
    num_hashes = int(hash_var.get())
    bf = bloom.BloomFilter(num_bits, num_hashes)
    print(f"Created filter: {num_bits} bits, {num_hashes} hashes")
    draw_grid()

def draw_grid():
    canvas.delete('all')
    
    num_bits = int(bits_var.get())
    
    # 2:1 ratio (twice as wide as tall)
    cols = int((num_bits * 2) ** 0.5)
    rows = (num_bits + cols - 1) // cols
    
    # Rest stays the same...
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    gap = 2
    max_square_w = (canvas_width - gap * cols) // cols
    max_square_h = (canvas_height - gap * rows) // rows
    square_size = min(max_square_w, max_square_h, 15)
    
    grid_width = cols * (square_size + gap)
    grid_height = rows * (square_size + gap)
    offset_x = (canvas_width - grid_width) // 2
    offset_y = (canvas_height - grid_height) // 2
    
    for i in range(num_bits):
        row = i // cols
        col = i % cols
        x1 = offset_x + col * (square_size + gap)
        y1 = offset_y + row * (square_size + gap)
        x2 = x1 + square_size
        y2 = y1 + square_size
        canvas.create_rectangle(x1, y1, x2, y2, fill='#232925', outline='')

def insert_word():
    word = word_entry.get()
    if bf is None:
        print("Create filter first")
        return
    bf.insert(word)
    print(f"Inserted: {word}")
    word_entry.delete(0, tk.END)



# Actual window setup
root = tk.Tk()
root.title("Bloom Filter Visualizer")
root.geometry("800x600") 
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


create_btn = tk.Button(setup_frame, text="Create Filter", 
                       command=create_filter,
                       bg=GREEN, fg=BG_DARK, 
                       font=('Times New Roman', 10, 'bold'),
                       padx=15, pady=5, bd=0)
create_btn.grid(row=0, column=4, padx=20)

canvas = tk.Canvas(root, width=700, height=400, bg=BG_DARK, highlightthickness=0)
canvas.pack(side='bottom', pady=20, fill='both', expand=True)


# Word input section
input_frame = tk.Frame(root, bg=BG_DARK, padx=20, pady=15)
input_frame.pack(fill='x')

word_label = tk.Label(input_frame, text="Input a Word:", bg=BG_DARK, fg=TEXT)
word_label.grid(row=0, column=0, padx=10)

word_entry = tk.Entry(input_frame, width=20)
word_entry.grid(row=0, column=1, padx=10)


insert_btn = tk.Button(input_frame, text="Insert", command=insert_word,
                       bg=GREEN, fg=BG_DARK, font=('Times New Roman', 10))
insert_btn.grid(row=0, column=2, padx=10)


root.mainloop()

