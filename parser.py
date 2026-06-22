from pypdf import PdfReader
from ai_extractor import extract_resume_data

def parse_resume(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return extract_resume_data(text)