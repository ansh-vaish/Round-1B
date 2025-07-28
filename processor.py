import fitz  # PyMuPDF
import os
import json

def extract_text_from_pdf(pdf_path: str) -> list:
    """
    Extracts text from each page of a PDF and returns a list of page texts.
    """
    doc = fitz.open(pdf_path)
    pages = []
    for page in doc:
        text = page.get_text("text").strip()
        cleaned = "\n".join([line.strip() for line in text.splitlines() if line.strip()])
        if cleaned:
            pages.append(cleaned)
    doc.close()
    return pages

def process_input_documents(input_json_path: str, pdf_dir: str):
    with open(input_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    persona = data["persona"]["role"]
    task = data["job_to_be_done"]["task"]
    extracted_pages = {}

    for doc in data["documents"]:
        filename = doc["filename"]
        pdf_path = os.path.join(pdf_dir, filename)
        if os.path.exists(pdf_path):
            pages = extract_text_from_pdf(pdf_path)
            if pages:
                extracted_pages[filename] = pages

    return data, extracted_pages, persona, task
