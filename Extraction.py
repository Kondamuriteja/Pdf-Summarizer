import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, output_file):
    doc = fitz.open(pdf_path)
    text = ""
    
    for page_num in range(len(doc)):
        try:
            page = doc.load_page(page_num)
            text += page.get_text("text")
        except Exception as e:
            print(f"Error extracting text from page {page_num + 1}: {e}")
            continue

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text
