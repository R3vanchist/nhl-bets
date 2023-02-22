import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My GUI")

# Create some widgets
label = tk.Label(root, text="Hello, world!")
button = tk.Button(root, text="Click me!")

# Add the widgets to the main window
label.pack()
button.pack()

# Start the event loop
root.mainloop()
