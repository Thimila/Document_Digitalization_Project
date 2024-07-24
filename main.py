from PIL import Image
import pytesseract

# Specify the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load an image from file
image_path = '2.jpg'
image = Image.open(image_path)

# Use Tesseract to extract text
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print(extracted_text)
