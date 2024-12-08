import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_data_from_pdf(pdf_path):
    """
    Extract data from PDFs using OCR and PyPDF2.
    """
    images = convert_from_path(pdf_path, dpi=300)
    extracted_text = ""

    for page in images:
        extracted_text += pytesseract.image_to_string(page) + "\n"

    reader = PdfReader(pdf_path)
    for page in reader.pages:
        extracted_text += page.extract_text()

    return extracted_text
