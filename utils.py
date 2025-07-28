import re

def clean_section_title(title: str) -> str:
    """
    Cleans and normalizes section titles extracted from the first line of a PDF page.
    """
    title = re.sub(r'[^a-zA-Z0-9\s\-]', '', title)  # Remove special characters
    title = re.sub(r'\s+', ' ', title).strip()       # Normalize whitespace
    if len(title.split()) < 2 or title.lower() in {"untitled", "title", "contents"}:
        return "Untitled Section"
    return title
