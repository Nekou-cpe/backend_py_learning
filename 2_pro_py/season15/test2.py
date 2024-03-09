import tkinter as tk

def set_border_color():
    # Change the border color directly using highlightbackground
    label.configure(highlightbackground="blue")

root = tk.Tk()
root.title("Label Border Example")

# Create a Label with no border initially
label = tk.Label(root, text="Hello, Border!", font=("Arial", 12), bd=0)
label.pack(padx=20, pady=20)

# Button to change the border color
button = tk.Button(root, text="Change Border Color", command=set_border_color)
button.pack(pady=10)

root.mainloop()
