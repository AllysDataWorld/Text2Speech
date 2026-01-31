FILE = r"C:\Users\after\Desktop_Aila\AI\GenAI\Readings\GenAI-Emebddings_vectorstores_v2.pdf"

from pypdf import PdfReader

def extract_text_from_pdf(FILE):
    # Create a PDF reader object
    reader = PdfReader(FILE)
    text = ""
    # Iterate through all the pages and extract text
    for page in reader.pages:
        text += page.extract_text() or "" # Use or "" to handle potential None returns
    return text

# Example usage:
extracted_text = extract_text_from_pdf(FILE)
print(extracted_text)
