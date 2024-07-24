from PIL import Image
import pytesseract
import csv

# Specify the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load an image from file
image_path = '2.jpg'
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

print(f"Extracted text saved to {csv_file_path}")
