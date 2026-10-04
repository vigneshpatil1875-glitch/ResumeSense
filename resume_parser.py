import re
from PyPDF2 import PdfReader


def extract_resume_text(pdf_path):
    """
    Extract text from a PDF resume.
    """

    reader = PdfReader(pdf_path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)


def clean_text(text):
    """
    Clean unnecessary spaces and blank lines.
    """

    if not text:
        return ""

    # Remove null characters
    text = text.replace("\x00", " ")

    # Replace multiple spaces/tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def get_word_count(text):
    """
    Return number of words in resume.
    """

    if not text:
        return 0

    return len(text.split())


def get_email(text):
    """
    Extract email address from resume.
    """

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group(0)

    return "Not found"


def get_phone(text):
    """
    Extract Indian-style phone number.
    """

    pattern = r"(?:\+91[\s-]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group(0)

    return "Not found"


def get_resume_info(text):
    """
    Return basic information from the resume.
    """

    return {
        "email": get_email(text),
        "phone": get_phone(text),
        "word_count": get_word_count(text)
    }
