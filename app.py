
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog, scrolledtext

# Function to list all files in a directory
def list_files():
    directory = filedialog.askdirectory()
    if directory:
        files = os.listdir(directory)
        result_text.insert(tk.END, f"Files in directory '{directory}':\n")
        for file in files:
            result_text.insert(tk.END, f"- {file}\n")

# Function to read and display data from a CSV file
def read_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        data = pd.read_csv(file_path)
        result_text.insert(tk.END, f"\nData from '{file_path}':\n")
        result_text.insert(tk.END, data.head())  # Display first few rows

# Function to scrape a website and display HTML content
def scrape_website():
    url = url_entry.get()
    if url:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        result_text.insert(tk.END, f"\nHTML content from '{url}':\n")
        result_text.insert(tk.END, soup.prettify())

# Create the main application window
app = tk.Tk()
app.title("Automated Tasks with GUI")

# UI Elements
list_files_button = tk.Button(app, text="List Files in Directory", command=list_files)
list_files_button.pack(pady=10)

read_csv_button = tk.Button(app, text="Read Data from CSV", command=read_csv)
read_csv_button.pack(pady=10)

# Frame for web scraping
scrape_frame = tk.Frame(app)
scrape_frame.pack(pady=10)

url_label = tk.Label(scrape_frame, text="Enter your  URL:")
url_label.grid(row=0, column=0)

url_entry = tk.Entry(scrape_frame, width=50)
url_entry.grid(row=0, column=1)

scrape_button = tk.Button(scrape_frame, text="Scrape Website", command=scrape_website)
scrape_button.grid(row=0, column=2, padx=10)

# Result Display
result_text = scrolledtext.ScrolledText(app, width=80, height=20)
result_text.pack(padx=20, pady=20)

# Start the GUI main loop
app.mainloop()
