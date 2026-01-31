FILE = r"C:\Users\after\Desktop_Aila\AI\GenAI\Readings\GenAI-Emebddings_vectorstores_v2.pdf"

from pypdf import PdfReader

reader = PdfReader(FILE)

get_page = 1
# Get the first page (index 0)
page = reader.pages[get_page-1]

# Extract text from the page
text = page.extract_text()
print(text)
