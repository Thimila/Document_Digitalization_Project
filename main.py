import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
import csv

# Specify the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def select_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        extract_text(file_path)

def extract_text(image_path):
    # Load an image from file
    image = Image.open(image_path)

    # Use Tesseract to extract text
    extracted_text = pytesseract.image_to_string(image)

    # Define the CSV file path
    csv_file_path = 'extracted_text.csv'

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
select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack(pady=20)

# Run the application
root.mainloop()
