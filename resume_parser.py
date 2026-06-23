from pypdf import PdfReader
from ai_extractor import extract_resume_data


def parse_resume(file_path):

    text = ""

    reader = PdfReader(file_path)

    for page in reader.pages:
        text += page.extract_text()

    data = extract_resume_data(text)

    return data