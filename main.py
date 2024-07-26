import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
import csv
import os

# Specify the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def select_images():
    # Open file dialog to select multiple images
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_paths:
        for file_path in file_paths:
            extract_text(file_path)

def extract_text(image_path):
    # Load an image from file
    image = Image.open(image_path)

    # Use Tesseract to extract text
    extracted_text = pytesseract.image_to_string(image)

    # Create a CSV file name based on the image file name
    base_name = os.path.basename(image_path)
    csv_file_name = os.path.splitext(base_name)[0] + '.csv'
    csv_file_path = os.path.join(os.path.dirname(image_path), csv_file_name)

    # Save the extracted text to a CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Extracted Text'])
        writer.writerow([extracted_text])

    messagebox.showinfo("Success", f"Extracted text saved to {csv_file_path}")

# Create the main window
root = tk.Tk()
root.title("Image Text Extractor")

# Create and place the button
select_button = tk.Button(root, text="Select Images", command=select_images)
select_button.pack(pady=20)

# Run the application
root.mainloop()
