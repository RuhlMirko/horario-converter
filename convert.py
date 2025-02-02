import fitz  # PyMuPDF
from PIL import Image, ImageDraw, ImageFont
import os

# Function to search for a string and get the next 7 lines
def search_text_in_pdf(pdf_path, search_string='RUHL, MIRKO JOEL', lines_after=7):
    dias = ['Nombre', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    full_str = ''

    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}")
        return None

    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):  # Loop through all pages
        text_lines = doc[page_num].get_text("text").split("\n")  # Split text into lines
        for i, line in enumerate(text_lines):

            if 'Plan de horarios para la semana' in line:
                filename = line.split('semana ', 1)[1].replace('/','-')
                full_str += line + '\n'

            if search_string in line:  # If search string is found

                extracted_lines = text_lines[i: i + lines_after + 1]  # Get the next N lines
                for i in range(8):
                    full_str += extracted_lines[i] + "-" * (50 - len(dias[i]) - len(extracted_lines[i]) - 2) + dias[
                        i] + '\n'
                text_to_image(full_str, output_image_path=f'D:/Descargas/Horarios/{filename}.png')  # Join lines into a single string
    return None  # Return None if not found


# Function to convert text into an image
def text_to_image(text, output_image_path, font_size=15):
    font = ImageFont.truetype("lucon.ttf", font_size)  # Default font
    image = Image.new("RGB", (530, 250), "white")  # Create a blank image
    draw = ImageDraw.Draw(image)

    # Draw text line by line
    y_position = 20
    for line in text.split("\n"):
        draw.text((20, y_position), line, font=font, fill="black")
        y_position += font_size + 5  # Adjust line spacing

    image.save(output_image_path)  # Save the image


# Example usage
# pdf_path = r"C:\PycharmProjects\horarios-converter\test\horarios-test.pdf"
# search_string = "RUHL, MIRKO JOEL"

# found_text = search_text_in_pdf(pdf_path, search_string, lines_after=7)
#
# if found_text:
#     print(f"Extracted Text:\n{found_text}")  # Print the extracted text
#     text_to_image(found_text, "output.png")
#     print("Image saved as output.png.")
# else:
#     print("Text not found in the PDF.")
