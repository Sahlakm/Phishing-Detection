import tkinter as tk
from tkinter import messagebox

def search():
    url = entry.get()
    # Perform your search operation with the URL (e.g., open the URL in a browser)
    # For demonstration purposes, we'll display a message box with the entered URL
    messagebox.showinfo("Search", f"Searching for: {url}")

# Create the main window
window = tk.Tk()
window.title("URL Search")

# Create and place the entry widget
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# Create and place the search button
search_button = tk.Button(window, text="Search", command=search)
search_button.pack()

# Start the Tkinter event loop
window.mainloop()
