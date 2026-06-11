import pymupdf

def extract_plain_text(pdf_path):
    doc = pymupdf.open(pdf_path)
    full_text = ""
    
    for page in doc:
        # Append text from each page with a newline
        full_text += page.get_text("text") + "\n"
        
    doc.close()
    return full_text  # Return the combined text





